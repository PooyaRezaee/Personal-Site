from . import admin
from flask import render_template

@admin.route('/')
def Dashboard():
    return render_template('mod_admin/dashboard.html')

@admin.route('/login/')
def Login():
    return render_template('mod_admin/login.html')