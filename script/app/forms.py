from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FloatField
from wtforms.validators import DataRequired

class Location(FlaskForm):
    starting_point_long = FloatField("From (long)")
    starting_point_lat =  FloatField("From (lat)")
    dest_point_long = FloatField("To (long)")
    dest_point_lat = FloatField("To (lat)")
    submit = SubmitField("Navigate")

class GraphLoc(FlaskForm):
    location = StringField("Location", validators=[DataRequired()])
    transport_mode = StringField("transport Mode", validators=[DataRequired()])
    submit = SubmitField("Graph")