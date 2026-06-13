from flask import Blueprint, render_template, request

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
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


@main_bp.route("/sobre-mi")
def sobre_mi():
    return render_template("sobre-mi.html")


@main_bp.route("/contacta")
def contacta():
    return render_template("contacta.html")


@main_bp.route("/saludo", methods=["GET", "POST"])
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
