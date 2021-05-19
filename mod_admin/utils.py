from functools import wraps
from flask import redirect,url_for,session,flash

def only_admin(func):
    @wraps(func)
    def wrapper(*args,**kwargas):
        if session.get('permission') != "yes":
            flash("first Do Login !","success")
            return redirect(url_for('admin.Login_get'))
        else:
            return func(*args,**kwargas)

    return wrapper
