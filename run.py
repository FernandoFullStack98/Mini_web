from flask import Flask
from app.models.models import db
from app.routes.tareas_routes import tareas_bp
from app.routes.auth_routes import auth_routes_bp
from app.routes.dashboard_routes import dashboard_bp
from app.routes.perfil_routes import perfil_bp
from app.routes.main_routes import main_bp
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
db.init_app(app)
app.register_blueprint(tareas_bp)
app.register_blueprint(auth_routes_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(perfil_bp)
app.register_blueprint(main_bp)


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
