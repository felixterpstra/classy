# classy
Simple text classification for machine learning training data, done with grace and style.

The goal is to dump training data into an s3 bucket (or Google Drive or Dropbox) then label it and output a file that can be to be consumed by a machine learning model.

Run it locally or in the cloud, instructions for running on Heroku are below.

There are other solutions to this problem, but we wanted something that was super lightweight, totally minimized the number of clicks to tag training data and also allowed multiple people to tag the same data so later you can only choose the data that has consensus extract as training data. Oh...it has to work on mobile and tablet too so you can label that training data while for the bus, or train while you train.  

Shout outs to the excellent : [Flask App Template](github.com/zachwill/flask_heroku) from Zach Williams which this app is based on.

You'll need the following environment variables set up (assuming you want to use Postgres on Heroku here)
```
DATABASE_URL="postgresql://localhost/classy_dev"
```
### Setup

Setup Postgress (or any other RMDS, but we'll use postgresql from here on in as our example)

run
```
psql
```

at the command line and create a database:

```
create database classy_dev;
```

Now install all the python packages in the asual way:
```
pip install -r requirements.txt
```

Now initialize the schema and run the migrations
:
```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

### Try an exmaple out

We've provided an example of a simple binary classifier, seeking to

### Run locally

```
FLASK_APP=app.py FLASK_DEBUG=1 python -m flask run
```

or

```
heroku local
```
as you prefer.

### Other potential solutions:
- https://prodi.gy looks pretty good actually, but is paid for. Worth a look though.

### Heroku Deployment:
Instructions here

### TODO:
- Add user authentication
- Add google drive integration
- Add dropbox integration
- Add support for different classification types (Image etc)
