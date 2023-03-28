from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
    # app.run(host="localhost", port=int("3000"), debug=True) [Not working]
    # app.run(host="127.0.0.1", port=3000, debug=True) [Not working]
    # app.run(host="192.168.1.5", port=8000, debug=True) [Container Exited]
