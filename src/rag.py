import os
from dotenv import load_dotenv
from google import genai
import chromadb

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

chroma_client = chromadb.PersistentClient(path="chroma_db")

collection = chroma_client.get_or_create_collection(
    name="support_docs"
)


def get_embedding(text):

    text = text.strip()

    if len(text) == 0:
        return None

    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )

    return response.embeddings[0].values


def load_documents():

    folder = "data"

    for file_name in os.listdir(folder):

        if not file_name.endswith(".txt"):
            continue

        file_path = os.path.join(folder, file_name)

        with open(file_path, "r", encoding="utf-8") as file:

            text = file.read().strip()

            print("\nProcessing:", file_name)
            print("Length:", len(text))

            if len(text) == 0:
                print("Skipped Empty File")
                continue

            embedding = get_embedding(text)

            if embedding is None:
                print("Embedding Failed")
                continue

            try:
                collection.add(
                    ids=[file_name],
                    documents=[text],
                    embeddings=[embedding],
                    metadatas=[
                        {
                            "source": file_name
                        }
                    ]
                )

                print("Added Successfully")

            except Exception as e:
                print("Skipped:", e)

    print("\nDocument Loading Completed")


def search_documents(query):

    query_embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    return results


if __name__ == "__main__":

    load_documents()

    print("\nSearching...\n")

    result = search_documents(
        "How can I reset my password?"
    )

    print(result)
def get_context(query):

    results = search_documents(query)

    documents = results["documents"][0]

    sources = []

    context = ""

    for doc in documents:

        context += doc + "\n\n"

    for item in results["metadatas"][0]:

        sources.append(item["source"])

    score = 1 - results["distances"][0][0]

    return context, sources, score