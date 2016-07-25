from app import db
from models import BlogPost

# create the db and the db tables
db.create_all()

# insert 
db.session.add(BlogPost("Good", "Very clean"))
db.session.add(BlogPost("Nice", "Staff is nice"))

# commit the changes
db.session.commit()