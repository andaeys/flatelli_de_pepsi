from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    # return jsonify({"Choo Choo": "Welcome to your Flask app anda disini"})
    return jsonify({"message": "di sini ayah pepsi",
                    "kucing": {
                        "calico": ["pepsi", "cokelat", "tompey"],
                        "oyen": ["momo"]
                    }
                    })

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
