from flask import Flask, request
from checker import checker

import os
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True

template_dir = os.path.join(os.path.dirname(__file__),
    'templates')

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(template_dir))

@app.route('/', methods=['POST'])
def check():
    template = jinja_env.get_template('user-signup.html')
    username = str(request.args.get("username"))
    password = str(request.args.get("password"))
    confirm = str(request.args.get("confirm"))
    email = str(request.args.get("email"))
    
    checkvals = checker(username,password,confirm,email)

    error = checkvals["error"]
    uname = username
    unameerror = checkvals["unameerror"]
    passerror = checkvals["passerror"]
    confirmerror = checkvals["confirmerror"]
    mail = email
    emailerror = checkvals["emailerror"]

    if error:
        return template.render(uname = uname,unameerror = unameerror,passerror = passerror,confirmerror = confirmerror,mail = mail,emailerror = emailerror)
    else:
        template = jinja_env.get_template('welcome.html')
        return template.render(username)

@app.route("/")
def index():
    template = jinja_env.get_template('user-signup.html')
    return template.render(
        uname="", 
        unameerror="",
        passerror="",
        confirmerror="",
        mail="",
        emailerror=""
    )

app.run()