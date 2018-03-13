from app import db, User, ClassyJob, ClassyText, ClassyLabel
import spacy
import datetime

sent_class_count = db.session.query(ClassyJob.name).filter(ClassyJob.name == 'Sentence Classification Job').count()
if sent_class_count > 0:
    print("Already a job named: 'Sentence Classification Job' ")
    raise SystemExit

sent_job = ClassyJob(name='Sentence Classification Job', s3bucket='')
db.session.add(sent_job)
db.session.commit()

sent = ClassyLabel(name='Sentence', classy_job_id=sent_job.id)
not_sent = ClassyLabel(name='NOT Sentence', classy_job_id=sent_job.id)
ignore = ClassyLabel(name='Ignore', classy_job_id=sent_job.id)
db.session.add(sent)
db.session.add(not_sent)
db.session.add(ignore)
db.session.commit()

print("Loading texts...")
nlp = spacy.load('en')
with open('examples/sentence_classifier/ROI.txt', 'r') as content_file:
    content = content_file.read()
    doc = nlp(content)

    for sent in list(doc.sents):
        classy_text = ClassyText(classification_text=sent.text, classy_job_id=sent_job.id, last_updated=datetime.datetime.now())
        db.session.add(classy_text)

db.session.commit()
