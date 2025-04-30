from flask import Flask, render_template, request, jsonify


class App:
    @property
    def app(self) -> Flask:
        return self._app

    @app.setter
    def app(self, app: Flask):
        self._app = app

    def __init__(self, name, assistant):
        self._app = Flask(
            name, template_folder="frontend/templates", static_folder="frontend/static"
        )
        self.assistant = assistant
        self.add_routes()

    def add_routes(self):
        # Route for the chat interface
        @self.app.route("/")
        def chatpage():
            return render_template("chat.html")

        # API route to handle chat messages
        @self.app.route("/response", methods=["POST"])
        def response():
            user_message = request.json.get("message")  # type: ignore
            bot_response = self.assistant.get_resonse(user_message)
            # bot_response = f"You said: {user_message}"
            return jsonify({"response": bot_response})

    def run(self, **kwargs):
        self.app.run(**kwargs)
