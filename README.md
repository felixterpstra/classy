# classy
Simple text classification for machine learning training data, done with grace and style.

The goal is to dump training data into an s3 bucket (or Google Drive or Dropbox) then label it and output a file that can be to be consumed by a machine learning model.

Run it locally or in the cloud, instructions for running on Heroku are below.

There are other solutions to this problem, but we wanted something that was super lightweight, totally minimized the number of clicks to tag training data and also allowed multiple people to tag the same data so later you can only choose the data that has consensus extract as training data. Oh...it has to work on mobile and tablet too so you can label that training data while for the bus, or train while you train.  

Shout outs to the excellent : [Flask App Template](github.com/zachwill/flask_heroku) from Zach Williams which this app is based on.

You'll need the following environment variables set up (assuming you want to use Postgres on Heroku here)
```
DATABASE_URL:"postgresql://localhost/classy_dev"
AWS_S3_ACCESS_KEY=<your_key_goes_here>
AWS_SECRET_KEY=<your_secret_goes_here>
```
### Setup


### Run locally



### Other potential solutions:
- https://prodi.gy looks pretty good actually, but is paid for. Worth a look though.

### Heroku Deployment:
Instructions here

### TODO:
- Add user authentication
- Add google drive integration
- Add dropbox integration
- Add support for different classification types (Image)
