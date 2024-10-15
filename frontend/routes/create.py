from os import getenv
from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required
from requests import post
from .. import app


BACKEND_URL = getenv("BACKEND_URL")
@app.get('/create')
@login_required
def create():
    return render_template('create.html')


@app.post('/create')
@login_required
def create_floppa():
    owner = current_user.email
    age = request.form.get("age")
    name = request.form.get("name")
    desc = request.form.get("desc")
    data = {'owner' : owner, 'age' : age, 'name' : name, 'desc' : desc}
    response = post(f"{BACKEND_URL}/create", json=data)
    if response.status_code==200:
        return redirect(url_for('index'))
    else: 
        code = response.status_code
        text = response.text
        return render_template("errors.html", code=code, text=text)