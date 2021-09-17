from flask import Flask, render_template

app = Flask(__name__)

favShows = ["Greys Anatomy", "Mr.Robot", "Pinocchio", "Humsafar", "Reign"]
@app.route('/')
def index():
    return render_template("index.html", len = len(favShows), favShows = favShows)



app.run(use_reloader = True, debug = True)