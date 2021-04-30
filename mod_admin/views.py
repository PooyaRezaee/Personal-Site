from . import admin
from flask import render_template,request,abort,flash,redirect,url_for,session
from .forms import LoginForm,SettingForms,ChangePassowrdForm,SkillForm,WorkSampleForm
from .models import Admin,Settings,Skills,Work_Sample
from app import db
import random
import os

@admin.route('/',methods=["GET"])
def Dashboard():
    # ============== Data ================
    skills = Skills.query.all()
    settings = Settings.query.first()
    work_samples = Work_Sample.query.all()
    # ============== FORMS ================
    settingform = SettingForms(obj=settings)
    changepassowrdform = ChangePassowrdForm()
    skillform = SkillForm()
    worksampleform = WorkSampleForm()

    if session.get('permission') != "yes":
        flash("first Do Login !","success")
        return redirect(url_for('admin.Login_get'))

    return render_template('mod_admin/dashboard.html',setting_form=settingform,changepassowrdform=changepassowrdform,skills=skills,skillform=skillform,worksampleform=worksampleform,work_samples=work_samples)

@admin.route('/<string:command>',methods=["POST"])
def Commands(command):
    settingform = SettingForms()
    changepassowrdform = ChangePassowrdForm(request.form)
    skillform = SkillForm(request.form)
    worksampleform = WorkSampleForm()

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

    elif skillform.validate_on_submit():
        if command == "a-s":
            new_skill = Skills()
            new_skill.Name = skillform.Name.data
            new_skill.Value_skill = skillform.Value.data
            db.session.add(new_skill)
            db.session.commit()

            flash("added Skill","success")

    elif worksampleform.validate_on_submit():
        if command == "a-ws":
            new_work_sample = Work_Sample()
            new_work_sample.title = worksampleform.title.data
            new_work_sample.link = worksampleform.link.data

            namefile = f"{random.randint(10000,99999)}_{worksampleform.image.data.filename}"
            path_file = f"static/images/work_samples/{namefile}"
            worksampleform.image.data.save(path_file)
            new_work_sample.url_image = path_file.replace('static/','')
            
            db.session.add(new_work_sample)
            db.session.commit()
            flash('Added Work Sample',"success")


    else:
        return "Has Error"
    
    return redirect(url_for('admin.Dashboard'))

@admin.route('delete/skill/<int:skill_id>')
def delete_skill(skill_id):
    try:
        skill = Skills.query.get_or_404(skill_id)
        db.session.delete(skill)
        db.session.commit()
        flash('Skill Deleted','success')
    except:
        flash('Has a problem in Delete Skill','danger')
    
    return redirect(url_for('admin.Dashboard'))

@admin.route('delete/worksample/<int:work_sample_id>')
def delete_work_sample(work_sample_id):
    try:
        work_sample = Work_Sample.query.get_or_404(work_sample_id)
        if work_sample.url_image != None:
            os.remove(f"static/{work_sample.url_image}")
        db.session.delete(work_sample)
        db.session.commit()
        flash('Work Sample Deleted','success')
    except:
        flash('Has a problem in Work Sample','danger')
    
    return redirect(url_for('admin.Dashboard'))

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