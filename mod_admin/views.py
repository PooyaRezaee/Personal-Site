from . import admin
from flask import render_template,request,abort,flash,redirect,url_for,session
from .forms import LoginForm,SettingForms
from .models import Admin,Settings
from app import db

@admin.route('/',methods=["GET"])
def Dashboard():
    settings = Settings.query.first()
    settingform = SettingForms(obj=settings)

    if session.get('permission') != "yes":
        flash("first Do Login !")
        return redirect(url_for('admin.Login_get'))

    return render_template('mod_admin/dashboard.html',setting_form=settingform)

@admin.route('/<string:command>',methods=["POST"])
def Commands(command):
    settingform = SettingForms()

    if settingform.validate_on_submit:
        settings = Settings.query.first()

        if command == "s-b":
            settingform.background_image.data.save('static/images/background.jpg')
            flash("Background Image Changed")

        elif command == "s-p":
            settingform.profile_image.data.save('static/images/profile.jpg')
            flash("Profile Image Changed")

        elif command == "ch-n":
            settings.FullName = settingform.FullName.data
            flash("You'r name Changed")

        elif command == "ch-a":
            settings.AboutME = settingform.AboutME.data
            flash("About You Changed")
        
        try:
            db.session.commit()
        except :
            flash("Error in Commit Data")

        return redirect(url_for('admin.Dashboard'))

    else:
        return "form not validate"

@admin.route('/login/',methods=["GET"])
def Login_get():
    if session.get('permission') == "yes":
        return redirect(url_for('admin.Dashboard'))
    form = LoginForm()

    return render_template('mod_admin/login.html',form=form)

@admin.route('/login/',methods=["POST"])
def Login_post():
    if session.get('permission') == "yes":
        return redirect(url_for('admin.Dashboard'))
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

@admin.route('/logout/')
def logout():
    session.clear()

    return redirect(url_for('Home'))