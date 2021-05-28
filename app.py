from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app,db)
# =========== Views ===============
from views import Home

# =========== BluePrints ==========
from mod_admin import admin
from mod_pdf import pdf

app.register_blueprint(admin)
app.register_blueprint(pdf)