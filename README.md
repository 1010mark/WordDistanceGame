"# WordDistanceGame" 
from flask import FLASK,render_template
@app.route("/")
def index():
    return render_template(index.html)
@app.route("/play")
def play():
    return render_template(play.html)

