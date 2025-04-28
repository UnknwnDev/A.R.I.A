from assistant.speech import Speech
from assistant.prompt_manager import PromptManager
from assistant.ollama_llm import OllamaLLM
from assistant.memory import Memory


class Assistant:
    def __init__(self, use_voice=False):
        self.llm = OllamaLLM()
        self.prompter = PromptManager()
        self.speaker = Speech()
        self.memory = Memory()
        self.history = []
        self.voice_enabled = use_voice

        # load history
        data = self.memory.load_data()
        self.history = data if data else []

    def chat_loop(self):
        """Runs loop for user to speak with agent"""
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

            self.memory.store_data(self.history[-2:])

            print(f"Assistant: {response}\n")
            self.speaker.speak(response)
