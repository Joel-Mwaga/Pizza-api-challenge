from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizza'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)

    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas', cascade='all, delete-orphan')
    pizza = db.relationship('Pizza', back_populates='restaurant_pizzas')

    def __init__(self, price, restaurant_id, pizza_id):
        if price < 1 or price > 30:
            raise ValueError("Price must be between 1 and 30")
        self.price = price
        self.restaurant_id = restaurant_id
        self.pizza_id = pizza_id

    def to_dict(self):
        return {
            'id': self.id,
            'price': self.price,
            'pizza_id': self.pizza_id,
            'restaurant_id': self.restaurant_id,
            'pizza': {
                'id': self.pizza.id,
                'name': self.pizza.name,
                'ingredients': self.pizza.ingredients
            },
            'restaurant': {
                'id': self.restaurant.id,
                'name': self.restaurant.name,
                'address': self.restaurant.address
            }
        }