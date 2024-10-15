from os import getenv
from flask_login import current_user, login_required
from flask import render_template,redirect,url_for
from requests import get
from .. import app

BACKEND_URL = getenv("BACKEND_URL")

@app.get("/")
@login_required
def index():
    email = current_user.email
    data = {
        "email": email
    }
    floppas = {
        "floppas": get(f"{BACKEND_URL}/default", json=data).json() 
    }

    nickname = ""

    if current_user.is_authenticated:
        nickname = current_user.email.split('@')[0]
    else:
        return redirect(url_for("register"))
    
    return render_template("index.html", **floppas, nickname=nickname)
