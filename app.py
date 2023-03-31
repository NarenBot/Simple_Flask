from flask import Flask, render_template
import os

app = Flask(__name__)
count = 0


@app.route("/")
def home():
    global count
    count += 1
    return render_template("index.html", counter=count)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)), debug=True)


# app.run(host="localhost", port=int("3000"), debug=True) [Not working]
# app.run(host="127.0.0.1", port=3000, debug=True, use_reloader=True) [Not working]
# app.run(host="192.168.1.5", port=8000, debug=True) [Container Exited]
