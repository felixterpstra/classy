from manage import db, app

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class ClassyJob(db.Model):
    __tablename__='classy_job'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    s3bucket = db.Column(db.String(1000))
    texts = db.relationship("ClassyText")
    labels = db.relationship("ClassificationLabel")

class ClassificationLabel(db.Model):
    __tablename__='classy_label'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    classication_label_id = db.Column(db.Integer, db.ForeignKey('classy_job.id'))

class ClassyText(db.Model):
    __tablename__='classy_text'
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(1000))
    file_created = db.Column(db.DateTime())
    classification_text = db.Column(db.Text())
    last_updated = db.Column(db.DateTime())
    classication_label_id = db.Column(db.Integer, db.ForeignKey('classy_label.id'))
    classy_job_id = db.Column(db.Integer, db.ForeignKey('classy_job.id'))
