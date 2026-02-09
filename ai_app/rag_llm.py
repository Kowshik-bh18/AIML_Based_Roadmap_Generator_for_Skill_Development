import json
import requests
from endee import Endee
from sentence_transformers import SentenceTransformer

# ---------------------------
# CONFIG
# ---------------------------

ENDEE_BASE_URL = "http://localhost:9090/api/v1"
INDEX_NAME = "RoadmapAI"

# NGROK endpoint from Colab
LLM_API_URL = "https://recent-eura-undesignedly.ngrok-free.dev/generate"

TOP_K = 5

# ---------------------------
# INIT CLIENTS
# ---------------------------

# Endee Vector DB
client = Endee()
client.set_base_url(ENDEE_BASE_URL)
index = client.get_index(INDEX_NAME)

# Embedding model (local)
embed_model = SentenceTransformer("BAAI/bge-small-en")

# ---------------------------
# EMBEDDING FUNCTION
# ---------------------------

def embed_query(text: str):
    try:
        return embed_model.encode(text).tolist()
    except Exception as e:
        print("Embedding error:", e)
        return None


# ---------------------------
# VECTOR SEARCH (RAG RETRIEVAL)
# ---------------------------

def retrieve_context(query: str):

    vector = embed_query(query)
    if vector is None:
        return []

    try:
        results = index.query(vector=vector, top_k=TOP_K)

        contexts = []
        for item in results:
            if "meta" in item and "text" in item["meta"]:
                contexts.append(item["meta"]["text"])
            else:
                contexts.append(json.dumps(item))

        return contexts

    except Exception as e:
        print("Endee Query Error:", e)
        return []


# ---------------------------
# CONTEXT FORMAT
# ---------------------------

def format_context(context_blocks):

    if not context_blocks:
        return "No useful context retrieved."

    return "\n---\n".join(context_blocks)


# ---------------------------
# LLM CALL (NGROK ENDPOINT)
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
        response = requests.post(
            LLM_API_URL,
            json={"query": prompt},
            timeout=600
        )

        return response.json().get("response", "No response from LLM.")

    except Exception as e:
        print("LLM API Error:", e)
        return "LLM connection failed."


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


# ---------------------------
# TEST RUN
# ---------------------------

if __name__ == "__main__":
    q = input("Ask something: ")
    print(rag_answer(q))
