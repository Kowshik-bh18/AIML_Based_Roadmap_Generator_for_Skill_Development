import json
from endee import Endee
from sentence_transformers import SentenceTransformer

# ---------------------------
# CONFIG
# ---------------------------

INDEX_NAME = "RoadmapAI"

# Local embedding model (recommended)
model = SentenceTransformer("BAAI/bge-small-en")

# Initialize Endee client
client = Endee()
client.set_base_url("http://localhost:9090/api/v1")


index = client.get_index(name=INDEX_NAME)


# ---------------------------
# EMBEDDING FUNCTION
# ---------------------------

def embed_text(text):
    return model.encode(text).tolist()


# ---------------------------
# LOAD DATASET
# ---------------------------

with open("dataset.json", "r", encoding="utf-8") as f:
    dataset = json.load(f)


# ---------------------------
# INSERT DATA
# ---------------------------

vectors_to_insert = []

for item in dataset:

    vector = embed_text(item["embedding_text"])

    vectors_to_insert.append({
        "id": item["id"],
        "vector": vector,
        "meta": {
            "text": item["embedding_text"],
            **item["metadata"]
        }
    })


# Batch insert (much faster)
index.upsert(vectors_to_insert)

print("Successfully inserted vectors!")
