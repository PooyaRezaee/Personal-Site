from . import admin
from flask import render_template,request,abort,flash,redirect,url_for,session
from .forms import LoginForm,SettingForms,ChangePassowrdForm
from .models import Admin,Settings
from app import db

@admin.route('/',methods=["GET"])
def Dashboard():
    settings = Settings.query.first()
    settingform = SettingForms(obj=settings)
    changepassowrdform = ChangePassowrdForm()

    if session.get('permission') != "yes":
        flash("first Do Login !","success")
        return redirect(url_for('admin.Login_get'))

    return render_template('mod_admin/dashboard.html',setting_form=settingform,changepassowrdform=changepassowrdform)

@admin.route('/<string:command>',methods=["POST"])
def Commands(command):
    settingform = SettingForms()
    changepassowrdform = ChangePassowrdForm(request.form)

    if settingform.validate_on_submit():
        settings = Settings.query.first()

        if command == "s-b":
            settingform.background_image.data.save('static/images/background.jpg')
            flash("Background Image Changed","success")

        elif command == "s-p":
            settingform.profile_image.data.save('static/images/profile.jpg')
            flash("Profile Image Changed","success")

        elif command == "ch-n":
            settings.FullName = settingform.FullName.data
            flash("You'r name Changed","success")

        elif command == "ch-a":
            settings.AboutME = settingform.AboutME.data
            flash("About You Changed","success")
        
        try:
            db.session.commit()
        except :
            flash("Error in Commit Data","danger")

        return redirect(url_for('admin.Dashboard'))
    
    elif changepassowrdform.validate_on_submit():
        if command == "ch-p":
            admin = Admin.query.first()

            if not admin.check_password(changepassowrdform.OldPassowrd.data):
                flash('Password Wrong',"danger")
                return redirect(url_for('admin.Dashboard'))

            if not changepassowrdform.NewPassword.data == changepassowrdform.ConfirmPassword.data:
                flash('passwords not match',"danger")
                return redirect(url_for('admin.Dashboard'))

            admin.Password = changepassowrdform.NewPassword.data
            db.session.commit()
            flash("Password Changed","success")
            return redirect(url_for('admin.Dashboard'))
    
    else:
        return "Has Error"
    
    print('ended')


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
        flash("Form Not Validate","danger")
        return render_template('mod_admin/login.html',form=form)

    admin_target = Admin.query.filter(Admin.UserName.ilike(f"{form.UserName.data}")).first()
    if not admin_target or not admin_target.check_password(form.Password.data):
        flash("UserName or Password is Wrong","danger")
        return render_template('mod_admin/login.html',form=form)
    
    session['permission'] = 'yes'
    return redirect(url_for('admin.Dashboard'))

@admin.route('/logout/')
def logout():
    session.clear()

    return redirect(url_for('Home'))