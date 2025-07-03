import openai

class LLMResponseAgent:
    def __init__(self, groq_key):
        openai.api_key = groq_key
        openai.api_base = "https://api.groq.com/openai/v1"

    def generate_answer(self, context_chunks, query):
        context = "\n\n".join(context_chunks)
        prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"

        response = openai.ChatCompletion.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=512
        )

        return response['choices'][0]['message']['content'].strip()

    def handle(self, message):
        assert message["type"] == "CONTEXT_RESPONSE"
        chunks = message["payload"]["top_chunks"]
        query = message["payload"]["query"]
        return self.generate_answer(chunks, query)
