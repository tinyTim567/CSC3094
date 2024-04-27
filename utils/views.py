from flask import Blueprint, render_template

from utils.forms import PasswordsQuestion1Form, PasswordsQuestion2Form

pages = Blueprint("page", __name__, template_folder="templates")


@pages.route("/phishing")
def phishing():
    return render_template("phishing/phishing.html")


@pages.route("/phishing/quiz")
def phishing_quiz():
    return render_template("phishing/phishing_quiz.html")


@pages.route("/malware")
def malware():
    return render_template("malware/malware.html")


@pages.route("/passwords")
def passwords():
    return render_template("passwords/passwords.html")


@pages.route("/passwords/quiz", methods=["GET", "POST"])
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

    return render_template("passwords/passwords_quiz.html", question1=question1, question2=question2, message1=message1,
                           message2=message2)


@pages.route("/about")
def about():
    return render_template("main/about.html")
