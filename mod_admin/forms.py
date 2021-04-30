from wtforms import StringField,PasswordField,TextAreaField,FileField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    UserName = StringField(validators=[DataRequired()],render_kw={"placeholder":"User Name","class":"input-group filed"})
    Password = PasswordField(validators=[DataRequired()],render_kw={"placeholder":"Password","class":"input-group filed"})


class SettingForms(FlaskForm):
    FullName = StringField(validators=[DataRequired()],render_kw={"placeholder":"Your Name","class":"w-100 p-1 mb-4"})
    profile_image = FileField(validators=[DataRequired()],render_kw={"class":"w-100 p-1 mb-4 border-0"})
    background_image = FileField(validators=[DataRequired()],render_kw={"class":"w-100 p-1 mb-4 border-0"})
    AboutME = TextAreaField(validators=[DataRequired()],render_kw={"placeholder":"About You","class":"w-100 p-1 mb-4"})

class ChangePassowrdForm(FlaskForm):
    OldPassowrd = PasswordField(validators=[DataRequired()],render_kw={"placeholder":"old Password"})
    NewPassword = PasswordField(validators=[DataRequired()],render_kw={"placeholder":"new Password"})
    ConfirmPassword = PasswordField(validators=[DataRequired()],render_kw={"placeholder":"confirm password"})