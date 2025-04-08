import os
import flask

app = flask.Flask(__name__)

@app.route("/")
def home():
    password = os.getenv("SECRET_PASSWORD")
    return "Welcome to vulnerable app!"

@app.route("/admin")
def admin():
    # Just to simulate sensitive route
    return "Admin access granted", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
