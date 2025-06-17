from flask import Blueprint, jsonify
from server.models.pizza import Pizza

bp = Blueprint('pizzas', __name__, url_prefix='/pizzas')

@bp.route('', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([{'id': pizza.id, 'name': pizza.name, 'ingredients': pizza.ingredients} for pizza in pizzas])