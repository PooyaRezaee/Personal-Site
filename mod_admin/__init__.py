from flask import Blueprint

admin = Blueprint("admin",__name__,url_prefix='/admin/')

# ============== Views ===========
from .views import Dashboard
from .views import Login_get
from .views import Login_post
from .views import logout

# ============= Models ===========
from .models import Admin