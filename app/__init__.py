from flask import Flask
from config import Config
from .models.models import db
from .routes.tareas_routes import tareas_bp
from .routes.auth_routes import auth_routes_bp
from .routes.dashboard_routes import dashboard_bp
from .routes.perfil_routes import perfil_bp
from .routes.main_routes import main_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(tareas_bp)
    app.register_blueprint(auth_routes_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(perfil_bp)
    app.register_blueprint(main_bp)
    with app.app_context():
        db.create_all()

    return app
