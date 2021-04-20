from wtforms import StringField,PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    UserName = StringField(validators=[DataRequired()],render_kw={"placeholder":"User Name","class":"input-group filed"})
    Password = PasswordField(validators=[DataRequired()],render_kw={"placeholder":"Password","class":"input-group filed"})