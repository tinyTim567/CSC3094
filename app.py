from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("main/index.html")


@app.route("/phishing")
def phishing():
    return render_template("phishing/phishing.html")


@app.route("/phishing/quiz")
def phishing_quiz():
    return render_template("phishing/phishing_quiz.html")


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


@app.errorhandler(400)
def bad_request(error):
    return render_template("error/400.html"), 400


@app.errorhandler(403)
def forbidden(error):
    return render_template("error/403.html"), 403


@app.errorhandler(404)
def page_not_found(error):
    return render_template("error/404.html"), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template("error/500.html"), 500


@app.errorhandler(503)
def service_unavailable(error):
    return render_template("error/503.html"), 503


if __name__ == '__main__':
    app.run()
