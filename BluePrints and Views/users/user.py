from flask import Blueprint,render_template,request

user=Blueprint('user',__name__,static_folder='static',template_folder='templates')

@user.route("/")
def user_page():
    return render_template("user.html")
