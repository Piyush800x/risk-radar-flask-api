from flask import Flask, request, jsonify
from processes import get_high_critical

app = Flask(__name__)


@app.route("/api/sort/", methods=["POST"])
def sort():
    response = request.get_json()
    # print(response)
    data = get_high_critical(response)
    print(data)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
