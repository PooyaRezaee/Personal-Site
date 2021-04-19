from app import app
from flask import render_template

@app.route('/')
def Home():
    return render_template('home.html')