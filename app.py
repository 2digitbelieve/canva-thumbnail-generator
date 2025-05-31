from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Canva App is alive!"})

@app.route("/api/canva", methods=["POST"])
def canva_api():
    data = request.json
    print(data)
    return jsonify({"status": "received"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
