from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField, StringField, IntegerField, TextAreaField, RadioField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional



class AddPet(FlaskForm):
    """form for adding new pet"""

    name = StringField("Pet name", validators=[InputRequired()])
    species = SelectField("Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")], validators=[InputRequired()])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes", validators=[Optional()])



class EditPet(FlaskForm):
    """form for editing existing pet"""

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Notes", validators=[Optional()])
    # available = SelectField("Available", choices=[(True, "Yes"), (False, "No")], validators=[Optional()])
    available = BooleanField("Available")
