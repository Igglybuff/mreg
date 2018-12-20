from flask import Flask, Response

app = Flask(__name__)


@app.route("/healthcheck")
def healthcheck():
    return "OK"


@app.route("/")
def index():
    resp = "foo"
    return Response(resp, mimetype='text/plain')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

