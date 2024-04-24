from flask import Flask, jsonify

app = Flask(__name__)

prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


@app.route("/api/prices")
def get_prices():
    return jsonify(prices)


if __name__ == "__main__":
    app.run(debug=True)
