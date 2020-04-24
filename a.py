import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    return "hello flask"

@app.route("/hello")
def hello():
    print("hello 요청됨")
    return flask.render_template("start.html")

if __name__ == "__main__":
    app.run(host="192.168.0.13",debug=True)