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
        data = request.json["data"]
        # print(data)
        response_data = {"message": "Data received successfully"}
        # data_string = json.dumps(data)
        # Assuming 'summerycalc' is defined and imported properly
        # summery, doc, orig_word_count, summery_word_count = summerycalc(data)
        summery,swc,dwc = summerycalc(data)
        # print(summery)
        return jsonify( summery=summery,swc=swc,dwc=dwc), 200
    except KeyError:
        return jsonify({"error": "Invalid data format"}), 400




if __name__ == "__main__":
    app.run(port=5000)
