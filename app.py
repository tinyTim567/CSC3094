import secrets

from flask import Flask, render_template
from flask_wtf import CSRFProtect

from utils.views import pages

app = Flask(__name__)

app.secret_key = secrets.token_urlsafe(16)
csrf = CSRFProtect(app)


@app.route("/")
def index():
    return render_template("main/index.html")


# ERROR HANDLING
@app.errorhandler(400)
def bad_request(error):
    return render_template("error/400.html"), 400


@app.errorhandler(403)
def forbidden(error):
    return render_template("error/403.html"), 403


@app.errorhandler(404)
def page_not_found(error):
    return render_template("error/404.html"), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return render_template("error/405.html"), 405


@app.errorhandler(500)
def internal_server_error(error):
    return render_template("error/500.html"), 500


@app.errorhandler(503)
def service_unavailable(error):
    return render_template("error/503.html"), 503


# BLUEPRINTS
app.register_blueprint(pages)

if __name__ == '__main__':
    app.run()
