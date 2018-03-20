"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

import os, sys
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from livereload import Server, shell

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['CLASSY_DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# remember to use DEBUG mode for templates auto reload
# https://github.com/lepture/python-livereload/issues/144
app.debug = True

from models import User, ClassyText, ClassyLabel, ClassyJob, ClassyTrainingItem
###
# Routing for your application.
###

@app.route('/')
def home():
    classy_jobs = db.session.query(ClassyJob).all()

    """Render website's home page."""
    return render_template('home.html', classy_jobs=classy_jobs)

@app.route('/classy-text/<int:job_id>', methods=['GET','POST'])
def classy_text(job_id):
    #hard coded user_id for now, will fill in later
    user_id = 17

    if request.method == 'POST':
        label_id = request.form.get('btnLabel')
        classy_text_id = request.form.get('classy_text_id')
        training_item = ClassyTrainingItem(classy_text_id=classy_text_id, user_id=user_id, classy_label_id=label_id)
        db.session.add(training_item)
        db.session.commit()

    classy_labels = db.session.query(ClassyLabel).filter(ClassyLabel.classy_job_id == job_id)

    sub_query = db.session.query(ClassyTrainingItem.classy_text_id).\
        filter(ClassyTrainingItem.user_id == user_id)

    classy_text = db.session.query(ClassyText).\
        filter(ClassyText.id.notin_(sub_query)).\
        filter(ClassyText.classy_job_id == job_id).first()

    classy_job = db.session.query(ClassyJob).get(job_id)

    ##print(classy_text.classification_text, file=sys.stderr)
    return render_template('classy-text.html', classy_job=classy_job, classy_labels=classy_labels, classy_text=classy_text)


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.watch('/Views/*')
    # server.watch
    server.serve()
