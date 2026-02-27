from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("hud.html")

def send_update(data):
    socketio.emit("update", data)

if __name__ == "__main__":
    socketio.run(app, host="192.30.0.35", port=7556)