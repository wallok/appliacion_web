from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired

class HonorariosFroms(FlaskForm):
    honorarios = DecimalField("Honorarios",validators=[DataRequired()])
    submit = SubmitField("Calcular")
