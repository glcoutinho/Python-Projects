from flask import Flask, render_template, redirect, url_for, request, flash
# wtf and bootstrap
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
Bootstrap(app)


class Todo(FlaskForm):
    task = StringField('Write your todo', validators=[DataRequired()])


# CREATE DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Create Table
class task_force(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(250), unique=True, nullable=False)


# db.create_all()
# todo 1: Build the language in flask framework
# nav bar
# bootstrap color
# create a section for input and output
# todo 2: build the input
# wtf class
# use of csv write and read and loop
# pass variable to html with flask
# import wtd
# align with-left and padding
# todo 3: identify the task
# verify and delete tasks
# create and pass id to function
# use try to allow to generate file
# use stack overwflow why to get a lsit
# use if "casa" in item: to find words in list
# find a way to pass the word to cross
# todo 4: addition of sql
# reverse enginer

@app.route("/", methods=['GET', 'POST'])
def home():
    form = Todo()
    if form.validate_on_submit():
        post = task_force(task=form.task.data)

        db.session.add(post)
        db.session.commit()

    result = task_force.query.all()
    return render_template('index.html', form=form, tasks=result)


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    delete = task_force.query.get(task_id)
    db.session.delete(delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
