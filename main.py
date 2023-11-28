from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, redirect, url_for, request, session
from flask_ckeditor import CKEditor
import os
import smtplib

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("FLASK_KEY")

ckeditor = CKEditor(app)
Bootstrap5(app)

MAIL_ADDRESS = os.environ.get("MAIL_KEY")
MAIL_APP_PW = os.environ.get("PASSWORD_KEY")


# Send e-mail function
def send_email(name, email, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MAIL_ADDRESS, password=MAIL_APP_PW)
        connection.sendmail(from_addr=MAIL_ADDRESS, to_addrs=MAIL_ADDRESS, msg=email_message)


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["message"])
        session['message'] = "Form submission successful!"
        session['msg_sent'] = True
        return redirect(url_for("home"))
    message = session.pop('message', None)
    msg_sent = session.pop('msg_sent', False)
    return render_template("index.html", msg_sent=msg_sent, message=message)


if __name__ == "__main__":
    app.run(debug=False, port=5001)
