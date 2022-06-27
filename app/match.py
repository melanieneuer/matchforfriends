from flask import Flask, Blueprint, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

#Bootstrap(app)

match = Blueprint('match', __name__)

class match_form(FlaskForm):
    name = StringField('How do you drink your coffee?', validators=[DataRequired()])
    submit = SubmitField('Submit')

@match.route('/match', methods=['GET', 'POST'])
def index():
    names = get_names(COFFEE)
    form = match_form()
    message = ""
    if form.validate_on_submit():
        name = form.name.data
        if name.lower() in names:
            form.name.data = ""
            id = get_id(COFFEE, name)
            return redirect( url_for('coffee', id=id) )
        else:
            message = "I do not know how to drink coffee like that."
    return render_template('match.html', names=names, form=form, message=message)

