from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL

class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""
    # TODO: Add the following fields to the form class:
    # - title - StringField
    # - address - StringField
    # - submit button
    title = StringField('Title', validators=[
        DataRequired()
    ])
    address = StringField('Address', validators=[
        DataRequired()
    ])
    submit = SubmitField('Submit')

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    # TODO: Add the following fields to the form class:
    # - name - StringField
    # - price - FloatField
    # - category - SelectField (specify the 'choices' param)
    # - photo_url - StringField
    # - store - QuerySelectField (specify the `query_factory` param)
    # - submit button
    name = StringField('Name', validators=[
        DataRequired()
    ])
    price = FloatField('Price', validators=[
        DataRequired()
    ])
    category = SelectField('Category', validators=[
        DataRequired()
    ])
    photo_url = StringField('Photo URL', validators=[
        DataRequired()
    ])
    store = QuerySelectField('Store', query_factory= ) # fix later
    submit = SubmitField('Submit')
