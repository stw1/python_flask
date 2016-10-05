from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def homepage():
    return render_template("main.html")


if __name__ == "__main__":
    application.run(host='0.0.0.0')