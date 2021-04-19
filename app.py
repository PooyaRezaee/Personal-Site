from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# =========== Views ===============
from views import Home

# =========== BluePrints ==========
from mod_admin import admin

app.register_blueprint(admin)