class PromptManager:
    def __init__(self):
        self.system_prompt = """
            You are Aria, an intelligent assistant. 
            Always respond concisely, avoiding unnecessary generic phrases like 'Feel free to ask any questions' or 'I'm here to help.' 
            Respond to the user's input with the best information you have.
            """

    def build_prompt(self, user_input):
        # Include Aria's identity in each prompt to reinforce that Aria knows who she is
        prompt = self.system_prompt + "\nUser: " + user_input + "\nAria:"
        return prompt
