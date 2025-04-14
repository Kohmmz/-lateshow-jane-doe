import os
from app import app, db
from models import Episode, Guest, Appearance
from faker import Faker

fake = Faker()

# Set up the app in development mode and configure the database URI
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lateshow.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create the tables if they don't exist
with app.app_context():
    db.create_all()

    # Generate and add some Episode data
    for _ in range(5):  # Generate 5 episodes
        episode = Episode(date=fake.date(), number=fake.random_int(min=1, max=10))
        db.session.add(episode)

    # Generate and add some Guest data
    for _ in range(5):  # Generate 5 guests
        guest = Guest(name=fake.name(), occupation=fake.job())
        db.session.add(guest)

    # Commit the episode and guest data to the database
    db.session.commit()

    # Get all episodes and guests after commit
    episodes = Episode.query.all()
    guests = Guest.query.all()

    # Generate and add some Appearance data (linking episodes and guests)
    for _ in range(10):  # Generate 10 appearances
        appearance = Appearance(
            rating=fake.random_int(min=1, max=5),
            episode_id=fake.random_element(elements=episodes).id,
            guest_id=fake.random_element(elements=guests).id
        )
        db.session.add(appearance)

    # Commit the appearances to the database
    db.session.commit()

    print("Seed data has been successfully added.")
