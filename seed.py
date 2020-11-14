from models import db, Pet
from app import app

# Create all tables
db.drop_all()
db.create_all()

# Add sample pets
p1 = Pet(name='Woofly', species='dog', 
         photo_url='https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1649&q=80', age=3, notes='Incredibly adorable.', available=True)

p2 = Pet(name='Porchetta', species='“porcupine',
         photo_url='https://images.unsplash.com/photo-1587722408951-8862b13c039d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1651&q=80', available=True)

p3 = Pet(name='Snargle', species='cat', 
         photo_url='https://images.unsplash.com/photo-1533743983669-94fa5c4338ec?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1583&q=80', available=True)

p4 = Pet(name='happy', species='dog',
         photo_url='https://images.unsplash.com/photo-1527526029430-319f10814151?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1650&q=80', available=True)

p5 = Pet(name='hoogy', species='dog',
         photo_url='https://images.unsplash.com/photo-1561037404-61cd46aa615b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1650&q=80', available=False)


# Add new objects to session, so they'll persist
db.session.add_all([p1, p2, p3, p4, p5])
db.session.commit()

