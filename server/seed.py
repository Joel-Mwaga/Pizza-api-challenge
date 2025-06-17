from server.app import db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

def seed_data():
    # Create restaurants
    restaurant1 = Restaurant(name="Kiki's Pizza", address="123 Pizza St")
    restaurant2 = Restaurant(name="Emma's Pizzeria", address="456 Dough Ave")
    
    # Create pizzas
    pizza1 = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Cheese")
    pizza2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    
    # Create restaurant_pizza relationships
    restaurant_pizza1 = RestaurantPizza(price=10, restaurant=restaurant1, pizza=pizza1)
    restaurant_pizza2 = RestaurantPizza(price=12, restaurant=restaurant1, pizza=pizza2)
    restaurant_pizza3 = RestaurantPizza(price=8, restaurant=restaurant2, pizza=pizza1)
    
    # Add to session
    db.session.add(restaurant1)
    db.session.add(restaurant2)
    db.session.add(pizza1)
    db.session.add(pizza2)
    db.session.add(restaurant_pizza1)
    db.session.add(restaurant_pizza2)
    db.session.add(restaurant_pizza3)
    
    # Commit the session
    db.session.commit()

if __name__ == "__main__":
    seed_data()