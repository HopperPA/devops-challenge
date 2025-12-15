from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "timestamp": str(datetime.datetime.utcnow()),
        "ip": request.remote_addr
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
