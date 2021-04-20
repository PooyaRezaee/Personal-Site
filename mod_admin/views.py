from . import admin
from flask import render_template,request,abort,flash,redirect,url_for,session
from .forms import LoginForm
from .models import Admin

@admin.route('/')
def Dashboard():
    return render_template('mod_admin/dashboard.html')

@admin.route('/login/',methods=["GET"])
def Login_get():
    form = LoginForm()

    return render_template('mod_admin/login.html',form=form)

@admin.route('/login/',methods=["POST"])
def Login_post():
    form = LoginForm(request.form)

    if not form.validate_on_submit():
        flash("Form Not Validate")
        return render_template('mod_admin/login.html',form=form)

    admin_target = Admin.query.filter(Admin.UserName.ilike(f"{form.UserName.data}")).first()
    if not admin_target or not admin_target.check_password(form.Password.data):
        flash("UserName or Password is Wrong")
        return render_template('mod_admin/login.html',form=form)
    
    session['permission'] = 'yes'
    return redirect(url_for('admin.Dashboard'))