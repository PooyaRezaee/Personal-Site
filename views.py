from app import app,db
from flask import render_template,request
from mod_admin.models import Settings,Skills,Work_Sample,Documents,Contact_way,Request

@app.route('/')
def Home():
    settings = Settings.query.first()
    skills = Skills.query.all()
    work_samples = Work_Sample.query.all()
    documents = Documents.query.all()
    Contact_ways = Contact_way.query.all()

    # Register Request in database

    new_request = Request()
    new_request.ip = request.remote_addr
    new_request.method = request.method

    db.session.add(new_request)
    db.session.commit()

    return render_template('home.html',settings=settings,skills=skills,work_samples=work_samples,documents=documents,Contact_ways=Contact_ways)