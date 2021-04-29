from app import app
from flask import render_template
from mod_admin.models import Settings,Skills,Work_Sample,Documents,Contat_way

@app.route('/')
def Home():
    settings = Settings.query.first()
    skills = Skills.query.all()
    work_samples = Work_Sample.query.all()
    documents = Documents.query.all()
    contat_ways = Contat_way.query.all()

    return render_template('home.html',settings=settings,skills=skills,work_samples=work_samples,documents=documents,contat_ways=contat_ways)