from datetime import date
from flask_bootstrap import Bootstrap5

from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_ckeditor import CKEditor
# from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
import os
import smtplib


app = Flask(__name__)
app.config['SECRET_KEY'] = "fkjdksksdkffkvck4k4l4l3dlldlwlldldflt55"

ckeditor = CKEditor(app)
Bootstrap5(app)


@app.route('/')
def home():
    return render_template("index.html")


# Add a Project to portfolio method to be able to post comments
# @app.route("/post/<int:post_id>", methods=["GET", "POST"])
# def show_post(post_id):
#     requested_post = db.get_or_404(BlogPost, post_id)
#     # Add the CommentForm to the route
#     comment_form = CommentForm()
#     # Only allow logged-in users to comment on posts
#     if comment_form.validate_on_submit():
#         if not current_user.is_authenticated:
#             flash("You need to login or register to comment.")
#             return redirect(url_for("login"))
#
#         new_comment = Comment(
#             text=comment_form.comment_text.data,
#             comment_author=current_user,
#             parent_post=requested_post
#         )
#         db.session.add(new_comment)
#         db.session.commit()
#     return render_template("post.html", post=requested_post, current_user=current_user, form=comment_form)
#
#
# # Use a decorator so only an admin user can create new posts
# @app.route("/new-post", methods=["GET", "POST"])
# @admin_only
# def add_new_post():
#     form = CreatePostForm()
#     if form.validate_on_submit():
#         new_post = BlogPost(
#             title=form.title.data,
#             subtitle=form.subtitle.data,
#             body=form.body.data,
#             img_url=form.img_url.data,
#             author=current_user,
#             date=date.today().strftime("%B %d, %Y")
#         )
#         db.session.add(new_post)
#         db.session.commit()
#         return redirect(url_for("get_all_posts"))
#     return render_template("make-post.html", form=form, current_user=current_user)
#
#
# # Use a decorator so only an admin user can edit a post
# @app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
# def edit_post(post_id):
#     post = db.get_or_404(BlogPost, post_id)
#     edit_form = CreatePostForm(
#         title=post.title,
#         subtitle=post.subtitle,
#         img_url=post.img_url,
#         author=post.author,
#         body=post.body
#     )
#     if edit_form.validate_on_submit():
#         post.title = edit_form.title.data
#         post.subtitle = edit_form.subtitle.data
#         post.img_url = edit_form.img_url.data
#         post.author = current_user
#         post.body = edit_form.body.data
#         db.session.commit()
#         return redirect(url_for("show_post", post_id=post.id))
#     return render_template("make-post.html", form=edit_form, is_edit=True, current_user=current_user)
#
#
# # Use a decorator so only an admin user can delete a post
# @app.route("/delete/<int:post_id>")
# @admin_only
# def delete_post(post_id):
#     post_to_delete = db.get_or_404(BlogPost, post_id)
#     db.session.delete(post_to_delete)
#     db.session.commit()
#     return redirect(url_for('get_all_posts'))
#
#
# @app.route("/about")
# def about():
#     return render_template("about.html", current_user=current_user)
#
#
# @app.route("/contact", methods=["GET", "POST"])
# def contact():
#     return render_template("contact.html", current_user=current_user)

# Optional: You can inclue the email sending code from Day 60:
# DON'T put your email and password here directly! The code will be visible when you upload to Github.
# Use environment variables instead (Day 35)

# MAIL_ADDRESS = os.environ.get("EMAIL_KEY")
# MAIL_APP_PW = os.environ.get("PASSWORD_KEY")

# @app.route("/contact", methods=["GET", "POST"])
# def contact():
#     if request.method == "POST":
#         data = request.form
#         send_email(data["name"], data["email"], data["phone"], data["message"])
#         return render_template("contact.html", msg_sent=True)
#     return render_template("contact.html", msg_sent=False)
#
#
# def send_email(name, email, phone, message):
#     email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(MAIL_ADDRESS, MAIL_APP_PW)
#         connection.sendmail(MAIL_ADDRESS, MAIL_APP_PW, email_message)


if __name__ == "__main__":
    app.run(debug=True, port=5001)


# linki w nowej karcie
# dodać zakładkę home do navbar
# pomyśleć na js