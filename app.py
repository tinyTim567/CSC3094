import secrets

from flask import Flask, render_template
from flask_wtf import CSRFProtect

from forms import PasswordsQuestion1Form, PasswordsQuestion2Form

app = Flask(__name__)

app.secret_key = secrets.token_urlsafe(16)
csrf = CSRFProtect(app)


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


@app.route("/passwords/quiz", methods=["GET", "POST"])
def passwords_quiz():
    question1 = PasswordsQuestion1Form()
    question2 = PasswordsQuestion2Form()
    message1 = ""
    message2 = ""
    if question1.validate_on_submit():
        correct_answers = 0
        if question1.common_phrases.data:
            print("1")
            correct_answers = correct_answers + 1
        if question1.significant_dates.data:
            print("2")
            correct_answers = correct_answers + 1
        if not question1.long_passwords.data:
            pass
        if question1.pet_names.data:
            print("4")
            correct_answers = correct_answers + 1
        if not question1.random_words.data:
            pass
        message1 = f"{correct_answers} / 3 correct"

    if question2.validate_on_submit():
        correct_answers = 0
        if question2.password123.data:
            print(" 1")
            correct_answers = correct_answers + 1
        if not question2.calendargrapesmug.data:
            pass
        if question2.numbers.data:
            print(" 3")
            correct_answers = correct_answers + 1
        if question2.bob2005.data:
            print(" 4")
            correct_answers = correct_answers + 1
        if not question2.treefolderbottle.data:
            pass
        message2 = f"{correct_answers} / 3 correct"

    return render_template("passwords/passwords_quiz.html", question1=question1, question2=question2, message1=message1, message2=message2)


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
