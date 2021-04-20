from flask import Blueprint

admin = Blueprint("admin",__name__,url_prefix='/admin/')

# ============== Views ===========
from .views import Dashboard
from .views import Login

# ============= Models ===========
from .models import Admin