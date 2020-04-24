from flask import Flask, render_template, request
# from werkzeug.utils import secure_filename
import myutil.hanb as hanb
import myutil.webtoon as wt
import myutil.goods as goods

app = Flask(__name__)
# app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route("/detailGoods/<no>")
def goodsDetail(no):
    doc =goods.getGoods(int(no))
    print(doc)
    return render_template("goodsDetail.html", doc=doc)


@app.route("/goodsInsert")
def goodsInsert():
    return render_template("goodsInsert.html")

@app.route("/goodsInsertOk",methods=['POST'])
def goodsInsertOk():
    no = int(request.form['no'])
    item = request.form['item']
    qty = int(request.form['qty'])
    price = int(request.form['price'])
    detail = request.form['detail']

    fname = "not.jpg"

    if 'file' in request.files:
        f = request.files["file"]
        f.save("./static/img/"+f.filename)
        fname= f.filename

    doc = {"no":no,"item":item,"qty":qty, "price":price,"fname":fname, "detail":detail}
    _id = goods.insert(doc)
    print(_id)
    return "ok"


@app.route("/goodsList")
def goodList():
    list = goods.listAll()
    return render_template("goodsList.html", list=list)

@app.route("/webtoon")
def webtoon():
    list = wt.getData()
    r = "pro("+  str(list)   +")"
    return r

@app.route("/newBook")
def newBook():
    list = hanb.getNewBook()
    r = "pro("+str(list)+")"
    return r
    # return  render_template("newBook.html", list=list)

@app.route("/")
def index():
    return "<h1>Hello</h1>"

if __name__ == "__main__":
    app.run(host="192.168.0.13", debug=True)

