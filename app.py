from flask import Flask, request, jsonify
from main import summerycalc
import json

app = Flask(__name__)

@app.route("/game")
def get_data():
    return {"data": "value1", "data2": "value2", "data3": "value3"}

@app.route("/")
def get_msg():
    return {"msg":"Server is running perfect :)"}


@app.route("/send_data", methods=["POST"])

def receive_data():
    try:
        data = request.json.get("data")  # Use get() to safely access the "data" key
        if data is None:
            return jsonify({"error": "Invalid data format"}), 400

        # Assuming 'summerycalc' is defined and imported properly
        summery, swc, dwc = summerycalc(data)
        return jsonify(summery=summery, swc=swc, dwc=dwc), 200

    except Exception as e:
        # Handle any other unexpected exceptions
        return jsonify({"error": str(e)}), 500




if __name__ == "__main__":
    app.run(port=5000)
