from os import getenv
from flask import render_template, redirect, url_for
from flask_login import current_user
from requests import post
from .. import app


BACKEND_URL = getenv("BACKEND_URL")


@app.get('/info/<int:floppa_id>')
def info(floppa_id):
    email = current_user.email
    data = {'email' : email}
    floppa = post(f"{BACKEND_URL}/floppa/{floppa_id}", json=data)
    if floppa.status_code==200:
        return redirect(url_for('index'))