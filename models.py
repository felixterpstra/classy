from manage import db, app

class ClassyTrainingItem(db.Model):
    __tablename__="classy_training_items"
    classy_text_id = db.Column(db.Integer, db.ForeignKey('classy_texts.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    classy_label_id = db.Column(db.Integer, db.ForeignKey('classy_labels.id'), primary_key=True)
    classy_user = db.relationship("User")
    classy_label = db.relationship("ClassyLabel")

class ClassyText(db.Model):
    __tablename__='classy_texts'
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(1000))
    file_created = db.Column(db.DateTime())
    classification_text = db.Column(db.Text())
    last_updated = db.Column(db.DateTime())
    classy_job_id = db.Column(db.Integer, db.ForeignKey('classy_jobs.id'))
    training_items = db.relationship("ClassyTrainingItem")

class ClassyLabel(db.Model):
    __tablename__='classy_labels'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    classy_job_id = db.Column(db.Integer, db.ForeignKey('classy_jobs.id'))

class ClassyJob(db.Model):
    __tablename__='classy_jobs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    s3bucket = db.Column(db.String(1000))
    texts = db.relationship("ClassyText")
    labels = db.relationship("ClassyLabel")

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(200), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.name)
