from flask import Blueprint,render_template,request

register=Blueprint('register',__name__,static_folder='static',template_folder='templates')

@register.route("/",methods=['POST'])
def register_page():
    username=request.form['username']
    password=request.form['password']
    return "user registered "+username