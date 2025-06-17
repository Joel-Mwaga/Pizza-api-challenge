from flask_sqlalchemy import SQLAlchemy
from server.app import db

db = SQLAlchemy()

class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ingredients = db.Column(db.String, nullable=False)

    restaurant_pizzas = db.relationship(
        "RestaurantPizza",  # Use string, not class
        backref="pizza"
    )