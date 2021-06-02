from . import admin
from flask import render_template,request,abort,flash,redirect,url_for,session
from .forms import LoginForm,SettingForms,ChangePassowrdForm,SkillForm,WorkSampleForm,DocumentsForm
from .models import Admin,Settings,Skills,Work_Sample,Documents,Request
from app import db
import random
import os
from .utils import only_admin
from datetime import datetime

@admin.route('/',methods=["GET"])
@only_admin
def Dashboard():
    # ============== Data ================
    skills = Skills.query.all()
    settings = Settings.query.first()
    work_samples = Work_Sample.query.all()
    documents = Documents.query.all()
    # ============== FORMS ================
    settingform = SettingForms(obj=settings)
    changepassowrdform = ChangePassowrdForm()
    skillform = SkillForm()
    worksampleform = WorkSampleForm()
    documentsform = DocumentsForm()
    # ============= Chart ================
    requests = Request.query.all()
    # last_month = {}
    # for n in range(0,31):
    #     last_month[f'{n}'] = 0
    
    # for req in requests:
    #     print(req.date.day)
    #     last_month[f'{req.date.day}'] += 1

    last_month = []
    for n in range(0,31):
        last_month.append(0)
    
    for req in requests:
        if req.date.month == int(datetime.now().strftime("%m")):
            last_month[req.date.day] += 1
    
    return render_template('mod_admin/dashboard.html',setting_form=settingform,changepassowrdform=changepassowrdform,skills=skills,skillform=skillform,worksampleform=worksampleform,work_samples=work_samples,documents=documents,documentsform=documentsform,last_month=last_month)

@admin.route('/save_background',methods=["POST"])
@only_admin
def Save_Background():
    settingform = SettingForms()

    if settingform.validate_on_submit():
        settingform.background_image.data.save('static/images/background.jpg')
        flash("Background Image Changed","success")
        db.session.commit()
    else:
        flash("Forms Not Validate",'danger')
    return redirect(url_for('admin.Dashboard'))


@admin.route('/save_profile',methods=["POST"])
@only_admin
def Save_Profile():
    settingform = SettingForms()

    if settingform.validate_on_submit():
        settingform.profile_image.data.save('static/images/profile.jpg')
        flash("Profile Image Changed","success")
        db.session.commit()
    else:
        flash("Forms Not Validate",'danger')

    return redirect(url_for('admin.Dashboard'))


@admin.route('/change_name',methods=["POST"])
@only_admin
def Change_Name():
    settingform = SettingForms()
    settings = Settings.query.first()

    if settingform.validate_on_submit():
        settings.FullName = settingform.FullName.data
        flash("You'r name Changed","success")
        db.session.commit()
    else:
        flash("Forms Not Validate",'danger')
    return redirect(url_for('admin.Dashboard'))


@admin.route('/change_about',methods=["POST"])
@only_admin
def Change_Aboutme():
    settingform = SettingForms()
    settings = Settings.query.first()

    if settingform.validate_on_submit():
        settings.AboutME = settingform.AboutME.data
        flash("About You Changed","success")
        db.session.commit()
    else:
        flash("Forms Not Validate",'danger')
    return redirect(url_for('admin.Dashboard'))

@admin.route('/change_password',methods=["POST"])
@only_admin
def change_password():
    changepassowrdform = ChangePassowrdForm(request.form)
    admin = Admin.query.first()

    if changepassowrdform.validate_on_submit():
        if not admin.check_password(changepassowrdform.OldPassowrd.data):
            flash('Password Wrong',"danger")
            return redirect(url_for('admin.Dashboard'))

        if not changepassowrdform.NewPassword.data == changepassowrdform.ConfirmPassword.data:
            flash('passwords not match',"danger")
            return redirect(url_for('admin.Dashboard'))

        admin.Password = changepassowrdform.NewPassword.data
        db.session.commit()
        flash("Password Changed","success")
    else:
        flash("Forms Not Validate",'danger')

    return redirect(url_for('admin.Dashboard'))

@admin.route('/add_skill',methods=["POST"])
@only_admin
def add_skills():
    skillform = SkillForm(request.form)

    if skillform.validate_on_submit():
        if skillform.Value.data < 0 or skillform.Value.data > 100:
            flash("Percentige can't must between 0 and 100",'warning')
            return redirect(url_for('admin.Dashboard'))
        new_skill = Skills()
        new_skill.Name = skillform.Name.data
        new_skill.Value_skill = skillform.Value.data
        db.session.add(new_skill)
        db.session.commit()

        flash("added Skill","success")
    else:
        flash("Forms Not Validate",'danger')
    
    return redirect(url_for('admin.Dashboard'))


@admin.route('/add_work_sample',methods=["POST"])
@only_admin
def add_work_sample():
    worksampleform = WorkSampleForm()

    if worksampleform.validate_on_submit():
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
        flash("Forms Not Validate",'danger')
    
    return redirect(url_for('admin.Dashboard'))

@admin.route('/add_document',methods=["POST"])
@only_admin
def add_document():
    documentsform = DocumentsForm()

    if documentsform.validate_on_submit():
        new_document = Documents()
        new_document.title = documentsform.Title.data
        new_document.link = documentsform.Link.data

        namefile = f"{random.randint(10000,99999)}_{documentsform.Image.data.filename}"
        path_file = f"static/images/document/{namefile}"
        documentsform.Image.data.save(path_file)
        new_document.url_image = path_file.replace('static/','')
        
        db.session.add(new_document)
        db.session.commit()
        flash('Added Documents',"success")
    else:
        flash("Forms Not Validate",'danger')
    
    return redirect(url_for('admin.Dashboard'))

# TODO Add Func for add contect way

@admin.route('delete/skill/<int:skill_id>')
@only_admin
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
@only_admin
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

@admin.route('delete/document/<int:document_id>')
@only_admin
def delete_document(document_id):
    try:
        document = Documents.query.get_or_404(document_id)
        if document.url_image != None:
            os.remove(f"static/{document.url_image}")
        db.session.delete(document)
        db.session.commit()
        flash('document Deleted','success')
    except :
        flash(f'Has a problem in document => {e}','danger')
    
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