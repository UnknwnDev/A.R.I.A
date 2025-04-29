from assistant.ollama_llm import OllamaLLM


class IntentManager:
    def __init__(self) -> None:
        self.system_prompt = """
            You are Aria, an intelligent assistant. 
            You are to classify the users input as either "command", "chat", "question".
            Respond with only one word: 'command', 'chat', 'question'.
            Note questions will not have '?' in them.
            commands are usually for things like system tasks or web searching.
            """
        self.ollama = OllamaLLM()

    def get_intent(self, user_input: str) -> str:
        prompt = self.system_prompt + "\nUser: " + user_input + "\nAria:"
        return self.ollama.get_response(prompt)
