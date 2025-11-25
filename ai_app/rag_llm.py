import json
import voyageai
from pinecone import Pinecone
from openai import OpenAI

# ---------------------------
# CONFIG
# ---------------------------

PINECONE_API_KEY = "pcsk_5QEXYN_Er83FzNCWsPNRuZwBZJa6jCvRGENPm492YSnGKdyd2CJAbGYKSxjCcyqHEbbsF1"
INDEX_HOST = "https://roadmaps-index-1sn1m1n.svc.aped-4627-b74a.pinecone.io"
NAMESPACE = "roadmaps"

VOYAGE_API_KEY = "pa-XblgTCTX_tytboiRIDrrUvOLprsbYml74761hDsqgHm"

HF_API_KEY = "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"
HF_BASE_URL = "https://z3nwkrihzjv9d9iv.us-east4.gcp.endpoints.huggingface.cloud/v1"
HF_MODEL = "ganeshaMD/roadmap-ai"

TOP_K = 5

# ---------------------------
# INIT CLIENTS
# ---------------------------

pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(host=INDEX_HOST)

vo = voyageai.Client(api_key=VOYAGE_API_KEY)

hf_client = OpenAI(
    base_url=HF_BASE_URL,
    api_key=HF_API_KEY
)


# ---------------------------
# EMBEDDING FUNCTION
# ---------------------------

def embed_query(text: str):
    try:
        res = vo.embed(
            model="voyage-3",
            texts=[text]
        )
        return res.embeddings[0]
    except Exception as e:
        print("Embedding error:", e)
        return None


# ---------------------------
# PINECONE RETRIEVAL
# ---------------------------

def retrieve_context(query: str):
    vector = embed_query(query)
    if vector is None:
        return []

    try:
        results = index.query(
            vector=vector,
            top_k=TOP_K,
            namespace=NAMESPACE,
            include_metadata=True
        )

        contexts = []
        for match in results.matches:
            if "text" in match.metadata:
                contexts.append(match.metadata["text"])
            else:
                contexts.append(json.dumps(match.metadata))

        return contexts

    except Exception as e:
        print("Pinecone Query Error:", e)
        return []


# ---------------------------
# FORMAT CONTEXT
# ---------------------------

def format_context(context_blocks):
    if not context_blocks:
        return "No useful context retrieved."

    return "\n---\n".join(context_blocks)


# ---------------------------
# HF LLM GENERATION
# ---------------------------

def generate_answer(query: str, context_text: str):

    prompt = f"""
You are an expert roadmap generator specializing in creating highly detailed learning plans.

Your task:
Generate a COMPLETE, DAY-WISE roadmap in a flowchart-style sequence. The roadmap must be extremely detailed and cover:
- Every topic
- Every sub-topic
- Tools required
- Concepts to master
- What to practice
- Expected outcomes
- Mini tasks or exercises
- Progression logic (each day builds on the previous)

STRICT FORMAT RULES:
- NO asterisks (*)
- NO markdown (#, **, etc.)
- NO bold/italics
- NO fancy formatting symbols
- Output MUST be clean plain text only

YOUR OUTPUT MUST FOLLOW THIS EXACT STRUCTURE:

Day 1 → Main Topic
  Detailed explanation of what the learner should focus on.
  List of subtopics to cover.
  Tools to install or use.
  Concepts to understand.
  Mini tasks to complete.
  End-of-day outcome.

Day 2 → Next Main Topic
  Detailed explanation.
  Subtopics.
  Tools.
  Tasks.
  Concepts.
  Outcome.

Continue like this for as many days as needed. Each day should feel like a full lesson plan.

ADDITIONAL RULES:
- Make the roadmap extremely clear and easy to follow.
- Include ALL important concepts, even advanced ones when necessary.
- Each day must include actionable tasks (e.g., "Build a small login page", "Write 10 SQL queries", etc.)
- Maintain sequential flow so the learner progresses logically.
- Use simple, readable language.
- The final output must be long, detailed, and structured.

RAG CONTEXT:
{context_text}

USER QUESTION:
{query}

Now generate the complete, highly detailed, day-wise roadmap:
"""


    try:
        resp = hf_client.chat.completions.create(
            model=HF_MODEL,
            messages=[{"role": "user", "content": prompt}]
        )

        return resp.choices[0].message.content

    except Exception as e:
        print("LLM Error:", e)
        return "Error generating LLM answer."


# ---------------------------
# MAIN RAG FUNCTION
# ---------------------------

def rag_answer(query: str):
    try:
        context_blocks = retrieve_context(query)
        context = format_context(context_blocks)

        answer = generate_answer(query, context)

        return answer

    except Exception as e:
        return f"[RAG SYSTEM ERROR] {e}"
