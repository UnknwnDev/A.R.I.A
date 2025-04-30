from assistant.assistant import Assistant
from frontend.app import App

if __name__ == "__main__":
    assistant = Assistant()
    # assistant.chat_loop()
    app = App(__name__, assistant)
    app.run(debug=True)
