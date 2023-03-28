from flask import Flask, render_template, url_for


app = Flask(__name__)
# from redis import Redis
# redis = Redis(host="redis", port=6379)


@app.route("/")
def home():
    # redis.incr("hits")
    # counter = str(redis.get("hits"), "utf-8")
    counter = 10
    return render_template("index.html", counter=counter)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
    # app.run(host="localhost", port=int("3000"), debug=True) [Not working]
    # app.run(host="127.0.0.1", port=3000, debug=True, use_reloader=True) [Not working]
    # app.run(host="192.168.1.5", port=8000, debug=True) [Container Exited]
