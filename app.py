from flask import Flask, request, jsonify
from main import summerycalc
from hug import summeryCalc2
import json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

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



@app.route("/send_data2", methods=["POST"])
def reciveData():
    try:
        data = request.json["data"]
        res = summeryCalc2(data)
        return jsonify(summery=res),200
    except KeyError:
      return jsonify({"error":"Invalid formate"})




if __name__ == "__main__":

    app.run(port=5000)
