from flask import Flask, render_template, request
from app.models.models import db
from app.routes.tareas_routes import tareas_bp
from app.routes.auth_routes import auth_routes_bp
from app.routes.dashboard_routes import dashboard_bp
from app.routes.perfil_routes import perfil_bp
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


with app.app_context():
    db.create_all()


@app.route("/")
def inicio():
    nombre = "Fernando"
    habilidades = ["Python", "HTML", "CSS", "Flask"]
    proyectos = [
        {
            "titulo": "Calculadora",
            "descripcion": "Una calculadora básica hecha con Python.",
        },
        {
            "titulo": "Agenda de contactos",
            "descripcion": "Una app de consola para guardar y ver contactos.",
        },
        {
            "titulo": "Página personal",
            "descripcion": "Una web sencilla creada con HTML, CSS y Flask.",
        },
    ]
    mostrar_proyectos = True

    return render_template(
        "index.html",
        nombre=nombre,
        habilidades=habilidades,
        proyectos=proyectos,
        mostrar_proyectos=mostrar_proyectos,
    )


@app.route("/sobre-mi")
def sobre_mi():
    return render_template("sobre-mi.html")


@app.route("/contacta")
def contacta():
    return render_template("contacta.html")


@app.route("/saludo", methods=["GET", "POST"])
def saludo():
    nombre = None
    error = None
    if request.method == "POST":
        nombre_formulario = request.form["name"].strip()
        if nombre_formulario == "":
            error = "Debes escribir un nombre"
        else:
            nombre = nombre_formulario

    return render_template("saludo.html", nombre=nombre, error=error)


if __name__ == "__main__":
    app.run(debug=True)
