# server/__init__.py
from flask import Flask
from server.extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object('server.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from server.controllers.restaurant_controller import restaurant_bp
        from server.controllers.pizza_controller import pizza_bp
        from server.controllers.restaurant_pizza_controller import restaurant_pizza_bp

        app.register_blueprint(restaurant_bp)
        app.register_blueprint(pizza_bp)
        app.register_blueprint(restaurant_pizza_bp)

    return app
