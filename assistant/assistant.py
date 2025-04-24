from assistant.speech import Speech
from assistant.prompt_manager import PromptManager
from assistant.ollama_llm import OllamaLLM

class Assistant:
    def __init__(self, use_voice=False):
        self.llm = OllamaLLM()
        self.prompter = PromptManager()
        self.speaker = Speech()
        self.history = []
        self.voice_enabled = use_voice

    def chat_loop(self):
        print("Voice Assistant is live! Say 'exit' or 'quit' to stop.\n")

        while True:
            user_input = input("You: ")

            if user_input.lower() in ("exit", "quit"):
                break

            if not user_input.strip():
                continue

            prompt = self.prompter.build_prompt(user_input)
            response = self.llm.get_response(prompt, self.history)

            self.history.append({"role": "user", "content": user_input})
            self.history.append({"role": "assistant", "content": response})

            print(f"Assistant: {response}\n")
            self.speaker.speak(response)
