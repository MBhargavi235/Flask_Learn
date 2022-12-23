from flask import Flask,render_template
from home import home 
from users.user import user
from users.register import register
app=Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(user,url_prefix='/user')
app.register_blueprint(register,url_prefix='/register')
"""
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/user')
def user():
    return render_template("user.html")
"""
if __name__=="__main__":
    app.run(debug=True)