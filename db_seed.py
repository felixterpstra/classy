from app import db
from models import User

User.query.delete()

matt = User(name='Matt Wright', email='matt@classy.io')
felix = User(name='Felix Terpstra', email='felix@classy.io')
db.session.add(matt)
db.session.add(felix)
db.session.commit()

users = User.query.all()
for user in users:
    print("%s - Created" % user.name)
