import flask
import random

app = flask.Flask(__name__)

possible_images = [
    "/static/Skeleton.jpeg",
    "/static/pumpkin.jpeg",
    "/static/escape.jpeg",
]

@app.route("/")
def index():
    img = random.choice(possible_images)
    return flask.render_template(
        "index.html",
        spooky_image=img,
    )

@app.route("/pumpkin_patch")
def blah():
    return flask.render_template("pumpkin_patch.html")

app.run()