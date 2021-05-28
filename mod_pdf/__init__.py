from flask import Blueprint

pdf = Blueprint("pdf",__name__,url_prefix='/pdf/')

# ============== Views ===========
from .views import download

