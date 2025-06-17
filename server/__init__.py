from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('server.config.Config')
    
    db.init_app(app)

    with app.app_context():
        from server.controllers.restaurant_controller import restaurant_bp
        from server.controllers.pizza_controller import pizza_bp
        from server.controllers.restaurant_pizza_controller import restaurant_pizza_bp
        
        app.register_blueprint(restaurant_bp)
        app.register_blueprint(pizza_bp)
        app.register_blueprint(restaurant_pizza_bp)

        db.create_all()

    return app