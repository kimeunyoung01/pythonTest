import flask
import myutil.kma as kma
import json

app = flask.Flask(__name__)

@app.route("/dept")
def dept():
    data = {"dno":10, "dname":"개발팀", "dloc":"서울"}
    str = "myCallback("+ json.dumps(data)+")"
    return str

@app.route("/kma")
def listkma():
    list = kma.getData()
    print(list)
    return flask.render_template("kma.html", list=list)

@app.route("/insert")
def insert():
    name = "이순신"
    return flask.render_template("insert.html", name=name )

@app.route("/list")
def list():
    return "<h2>게시물 목록</h2>"

@app.route("/")
def index():
    return "<h1>Hello Flask!!</h1>"

if __name__ == "__main__":
    app.run(host='192.168.0.13', debug=True)