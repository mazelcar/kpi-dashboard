from flask import Flask, jsonify
import boto3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("KPIs")

@app.route("/api/kpis")
def get_kpis():
    response = table.scan()
    return jsonify(response["Items"])

if __name__ == "__main__":
    app.run(debug=True)