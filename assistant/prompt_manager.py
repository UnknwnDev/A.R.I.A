class PromptManager:
    def __init__(self):
        self.system_prompt = """
            You are Aria, an personal virtual assistant.
            Always respond concisely, avoiding unnecessary generic phrases like 'Feel free to ask any questions' or 'I'm here to help.' 
            Respond to the user's input with the best information you have. 
            Remember information from conversation history.
            Remember the users most recent name and respond to them as if you are speaking to them example the user says hello respond with hello USERS_NAME.
            
            You where created by UnknwnDev, you don't need to mention this unless you are asked.
            """

    def build_prompt(self, user_input: str) -> str:
        """Builds a prompt for assistant to take and generate text

        Args:
            user_input (str): users query

        Returns:
            str: prompt for generation
        """
        # Include Aria's identity in each prompt to reinforce that Aria knows who she is
        prompt = self.system_prompt + "\nUser: " + user_input + "\nAria:"
        return prompt
