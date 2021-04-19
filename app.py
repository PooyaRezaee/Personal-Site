from flask import Flask

app = Flask(__name__)

# =========== Views ===============
from views import Home

# =========== BluePrints ==========
from mod_admin import admin

app.register_blueprint(admin)