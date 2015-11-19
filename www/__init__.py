from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/")
def hello():
    user = {'nickname': 'Miguel'}
    return render_template("index.html",
                           title='Home',
                           user=user)


@app.route("/login")
def login():
        return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
