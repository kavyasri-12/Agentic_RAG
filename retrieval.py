from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class RetrievalAgent:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = None
        self.chunk_map = []

    def embed_chunks(self, chunks):
        embeddings = self.model.encode(chunks)
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(np.array(embeddings))
        self.chunk_map = chunks

    def retrieve(self, query, top_k=3):
        query_vec = self.model.encode([query])
        distances, indices = self.index.search(np.array(query_vec), top_k)
        return [self.chunk_map[i] for i in indices[0]]

    def handle(self, message):
        assert message["type"] == "EMBED_AND_RETRIEVE"
        chunks = message["payload"]["chunks"]
        query = message["payload"]["query"]
        self.embed_chunks(chunks)
        top_chunks = self.retrieve(query)

        return {
            "sender": "RetrievalAgent",
            "receiver": "Coordinator",
            "type": "RETRIEVAL_RESULT",
            "trace_id": message["trace_id"],
            "payload": {
                "top_chunks": top_chunks,
                "query": query
            }
        }
