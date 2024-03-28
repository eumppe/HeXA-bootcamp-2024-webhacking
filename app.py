from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/atest")
def for_a_tag():
    return "'a' worked successfully"

@app.route("/posttest",methods=['POST'])
def post_test():
    name=request.form.get("name")
    return "hello, "+name+"!"

@app.route("/gettest", methods=['GET'])
def get_test():
    name=request.args.get("name")
    return "hello, "+name+"! it is 'get' page"

@app.route("/")
def hello_world():
    return render_template("helloWorld.html")

app.run()