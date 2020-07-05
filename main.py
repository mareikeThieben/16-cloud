from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, SmartNinja!"

@app.route("/about")
def index():
    return render_template("about.html")


if __name__ == '__main__':
    app.run()