from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("main/index.html")


@app.route("/phishing")
def phishing():
    return render_template("phishing/phishing.html")


@app.route("/malware")
def malware():
    return render_template("malware/malware.html")


@app.route("/passwords")
def passwords():
    return render_template("passwords/passwords.html")


@app.route("/passwords/quiz")
def passwords_quiz():
    return render_template("passwords/passwords_quiz.html")


@app.route("/about")
def about():
    return render_template("main/about.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("error/404.html"), 404


@app.errorhandler(500)
def page_not_found(error):
    return render_template("error/500.html"), 500


if __name__ == '__main__':
    app.run()
