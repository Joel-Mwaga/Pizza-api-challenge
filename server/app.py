from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from server.extensions import db

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pizza.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # Import models so SQLAlchemy knows about them
    from server.models import Restaurant, Pizza, RestaurantPizza

    migrate.init_app(app, db)

    from server.controllers.restaurant_controller import bp as restaurant_bp
    from server.controllers.pizza_controller import bp as pizza_bp
    from server.controllers.restaurant_pizza_controller import bp as restaurant_pizza_bp

    app.register_blueprint(restaurant_bp)
    app.register_blueprint(pizza_bp)
    app.register_blueprint(restaurant_pizza_bp)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)