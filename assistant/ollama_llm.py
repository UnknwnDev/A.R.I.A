from ollama import chat, Options
from config.settings import MODEL_NAME


class OllamaLLM:
    def __init__(self):
        self.model = MODEL_NAME

    def get_response(self, prompt: str, history: list = []) -> str:
        """Generates a response from the olama_llm model

        Args:
            prompt (str): structured system and user promt and input for generation
            history (list): list of previous user input and response

        Returns:
            str: response to the users input
        """
        # format history as chat format for Ollama
        full_history = []
        full_history += history
        full_history.append({"role": "user", "content": prompt})

        response = chat(
            model=self.model, messages=full_history, options=Options(temperature=0.7)
        )
        return response["message"]["content"]
