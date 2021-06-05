from typing import Set
from flask.helpers import send_file
from . import pdf
import pdfkit
from flask import render_template
from mod_admin.models import Contact_way, Settings,Skills,Work_Sample,Documents

@pdf.route('/',methods=["GET"])
def download():
    #============ Data ==========
    name = Settings.query.first().FullName
    about = Settings.query.first().AboutME
    skills = Skills.query.all()
    work_samples = Work_Sample.query.all()
    documents = Documents.query.all()
    contact_ways = Contact_way.query.all()

    options = {
    'page-size': 'A5',
    'margin-top': '0',
    'margin-right': '0',
    'margin-bottom': '0',
    'margin-left': '0',
    }

    html_file = render_template('CV_for_pdf.html',name=name,about=about,skills=skills,work_samples=work_samples,documents=documents,contact_ways=contact_ways)
    pdfkit.from_string(html_file,'mod_pdf/cv.pdf',options=options)

    name_file = f'{name}_CV.pdf'

    return send_file('mod_pdf/cv.pdf',as_attachment=True,attachment_filename=name_file)