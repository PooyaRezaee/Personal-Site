from flask.helpers import send_file
from . import pdf
import pdfkit
from flask import render_template

@pdf.route('/',methods=["GET"])
def download():

    options = {
    'page-size': 'A4',
    'margin-top': '0',
    'margin-right': '0',
    'margin-bottom': '0',
    'margin-left': '0',
    }

    html_file = render_template('CV_for_pdf.html') # TODO MAKE UI FOR CV PDF
    pdfkit.from_string(html_file,'mod_pdf/cv.pdf',options=options)

    return send_file('mod_pdf/cv.pdf',as_attachment=True,attachment_filename='cv.pdf')
