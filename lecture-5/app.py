import flask

app = flask.Flask(__name__)

#where is the webpage going to live
@app.route("/")
def index():
    print("this is a debug statement") #why did we need this
    #return "Hellow World!"
    return flask.render_template("index.html", name = "RHHRHR") #what is this doing

app.run(debug=True)

