🤖 Agentic RAG Chatbot with MCP
A multi-format document Question-Answering chatbot built using an agent-based RAG architecture with Model Context Protocol (MCP) message passing.
This chatbot can answer user questions using uploaded documents in PDF, DOCX, PPTX, TXT, CSV formats.
PLEASE CREATE YOUR OWN GROQ API KEY TO CHECK THE DEMO BELOW. DUE TO PRIVACY CONCERNS, I’M UNABLE TO SHARE MY PERSONAL GROQ API KEY.
DEMO LINK: https://agenticrag-goylcvnmn3s4ugugsazfwn.streamlit.app/

📌 Features
✅ Upload documents in PDF, DOCX, PPTX, TXT, CSV
✅ Agentic architecture with 3 core agents:

IngestionAgent: Parses and chunks documents
RetrievalAgent: Embeds and retrieves semantically similar chunks
LLMResponseAgent: Generates the final answer using Groq LLaMA 3

✅ Communication follows MCP protocol (JSON-based structured messages)
✅ Powered by Groq API (OpenAI-compatible) for ultra-fast LLM inference
✅ Built using Streamlit UI
✅ Shows source context chunks for traceability

🧠 Agentic Workflow (MCP)

User Upload → CoordinatorAgent →
   ↳ IngestionAgent (Parse, Chunk)
   ↳ RetrievalAgent (Embed, FAISS Search)
   ↳ LLMResponseAgent (LLM Answering via Groq)
→ Final Answer + Source Context

📦 MCP Message Example
{
  "type": "RETRIEVAL_RESULT",
  "sender": "RetrievalAgent",
  "receiver": "LLMResponseAgent",
  "trace_id": "rag-457",
  "payload": {
    "retrieved_context": ["slide 3: revenue up", "doc: Q1 summary..."],
    "query": "What KPIs were tracked in Q1?"
  }
}


⚙️ Tech Stack

Frontend: Streamlit
LLM: Groq API (LLaMA 3 via OpenAI-style endpoint)
Embeddings: all-MiniLM-L6-v2 (HuggingFace)
Vector DB: FAISS
MCP Messaging: In-memory JSON message passing
Document Parsers: PyMuPDF, python-docx, python-pptx, pandas

📁 Folder Structure
├── main.py
├── coordinator.py
├── ingestion_agent.py
├── retrieval_agent.py
├── response_agent.py
├── requirements.txt

🔑 Setup Instructions
1️⃣ Clone & Install Dependencies
git clone https://github.com/kavyasri-12/agentic-rag-chatbot.git
cd agentic-rag-chatbot
pip install -r requirements.txt
2️⃣ Important: Pin openai Version
openai==0.28.1
Required for compatibility with Groq's OpenAI-style API.
3️⃣** Run the App **
streamlit run main.py
4️⃣ Add Your Groq API Key
Use your key starting with gsk_...
Set it in the Streamlit input field or load via .env

🚧 Challenges Faced
❗ Groq model deprecation and version mismatch
⚠️ Repetitive chunks from low-informational content
🧩 Format parsing edge cases (e.g., tables in PPTX or malformed CSVs)

🚀 Future Scope
🖼 Add OCR support for scanned PDFs/images
💬 Introduce memory for follow-up questions
📄 Export conversation history (PDF/Markdown)
☁️ Deploy to Streamlit Cloud or Hugging Face Spaces

👤 Author
Kavyasri Kammari
AI Developer passionate about Generative AI & real-world LLM applications.
📧 kammarikavyasri11@gmail.com
