import uuid
from ingestion import IngestionAgent
from retrieval import RetrievalAgent
from response import LLMResponseAgent

class Coordinator:
    def __init__(self, api_key):
        self.ingestor = IngestionAgent()
        self.retriever = RetrievalAgent()
        self.llm = LLMResponseAgent(api_key)

    def handle(self, files, query):
        trace_id = str(uuid.uuid4())

        # Ingestion Agent
        ingest_msg = {
            "sender": "UI",
            "receiver": "IngestionAgent",
            "type": "DOCUMENT_UPLOAD",
            "trace_id": trace_id,
            "payload": {
                "files": files
            }
        }
        print(f"[MCP][{trace_id}] UI → IngestionAgent | DOCUMENT_UPLOAD")
        chunks = self.ingestor.handle(ingest_msg)

        # Retrieval Agent
        retrieve_msg = {
            "sender": "IngestionAgent",
            "receiver": "RetrievalAgent",
            "type": "EMBED_AND_RETRIEVE",
            "trace_id": trace_id,
            "payload": {
                "chunks": chunks,
                "query": query
            }
        }
        print(f"[MCP][{trace_id}] IngestionAgent → RetrievalAgent | EMBED_AND_RETRIEVE")
        retrieval_response = self.retriever.handle(retrieve_msg)

        # LLM Agent
        llm_msg = {
            "sender": "RetrievalAgent",
            "receiver": "LLMResponseAgent",
            "type": "CONTEXT_RESPONSE",
            "trace_id": trace_id,
            "payload": {
                "top_chunks": retrieval_response["payload"]["top_chunks"],
                "query": query
            }
        }
        print(f"[MCP][{trace_id}] RetrievalAgent → LLMResponseAgent | CONTEXT_RESPONSE")
        answer = self.llm.handle(llm_msg)

        return answer, retrieval_response["payload"]["top_chunks"]
