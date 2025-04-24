from ollama import chat, Options
from config.settings import MODEL_NAME

class OllamaLLM:
    def __init__(self):
        self.model = MODEL_NAME

    def get_response(self, prompt, history):
        # format history as chat format for Ollama
        full_history = [{"role": "system", "content": "You are a helpful assistant."}]
        full_history += history
        full_history.append({"role": "user", "content": prompt})

        response = chat(
            model=self.model,
            messages=full_history,
            options=Options(temperature=0.7)
        )
        return response['message']['content']
