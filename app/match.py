from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'verysecretkey'

Bootstrap(app)

class NameForm(FlaskForm):
    name = StringField('How do you drink your coffee?', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    names = get_names(COFFEE)
    form = NameForm()
    message = ""
    if form.validate_on_submit():
        name = form.name.data
        if name.lower() in names:
            form.name.data = ""
            id = get_id(COFFEE, name)
            return redirect( url_for('coffee', id=id) )
        else:
            message = "I do not know how to drink coffee like that."
    return render_template('index.html', names=names, form=form, message=message)

