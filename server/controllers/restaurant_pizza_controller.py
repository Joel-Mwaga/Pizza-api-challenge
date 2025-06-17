from flask import Blueprint, request, jsonify
from server.app import db
from server.models.restaurant_pizza import RestaurantPizza
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant

bp = Blueprint('restaurant_pizzas', __name__, url_prefix='/restaurant_pizzas')

@bp.route('', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    if price < 1 or price > 30:
        return jsonify({"errors": ["Price must be between 1 and 30"]}), 400

    new_restaurant_pizza = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
    
    db.session.add(new_restaurant_pizza)
    db.session.commit()

    return jsonify({
        "id": new_restaurant_pizza.id,
        "price": new_restaurant_pizza.price,
        "pizza_id": new_restaurant_pizza.pizza_id,
        "restaurant_id": new_restaurant_pizza.restaurant_id,
        "pizza": {
            "id": new_restaurant_pizza.pizza.id,
            "name": new_restaurant_pizza.pizza.name,
            "ingredients": new_restaurant_pizza.pizza.ingredients
        },
        "restaurant": {
            "id": new_restaurant_pizza.restaurant.id,
            "name": new_restaurant_pizza.restaurant.name,
            "address": new_restaurant_pizza.restaurant.address
        }
    }), 201