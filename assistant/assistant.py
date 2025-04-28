from assistant.speech import Speech
from assistant.prompt_manager import PromptManager
from assistant.ollama_llm import OllamaLLM
from assistant.memory import Memory
from assistant.intent_manager import IntentManager


class Assistant:
    def __init__(self, use_voice=False):
        self.llm = OllamaLLM()
        self.prompter = PromptManager()
        self.intent_manager = IntentManager()
        self.speaker = Speech()
        self.memory = Memory()
        self.history = []
        self.voice_enabled = use_voice

        # load history
        data = self.memory.load_data()
        self.history = data if data else []

    def chat_loop(self) -> None:
        """Runs loop for user to speak with agent"""
        print("Voice Assistant is live! Say 'exit' or 'quit' to stop.\n")

        while True:
            user_input = input("You: ")

            if user_input.lower() in ("exit", "quit"):
                self.chat("goodbye aria")
                break

            if not user_input.strip():
                continue

            intent = self.intent_manager.get_intent(user_input)
            if "command" in intent:
                self.speaker.speak(f"This is a {intent}")
            else:
                self.chat(user_input)

    def chat(self, user_input: str) -> None:
        prompt = self.prompter.build_prompt(user_input)
        response = self.llm.get_response(prompt, self.history)

        self.history.append({"role": "user", "content": user_input})
        self.history.append({"role": "assistant", "content": response})

        self.memory.store_data(self.history[-2:])

        print(f"Assistant: {response}\n")
        self.speaker.speak(response)
