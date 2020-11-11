import flask
app = flask.Flask(__name__)

@app.route("/")
def drm():
    return flask.render_template("drm.html")

if __name__ == "__main__":
    app.run(host='localhost')
