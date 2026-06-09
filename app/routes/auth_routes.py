from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from app.models.models import Usuarios, db
from werkzeug.security import generate_password_hash, check_password_hash

auth_routes_bp = Blueprint("auth", __name__)


@auth_routes_bp.route("/register", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        usuario = request.form["usuario"]
        email = request.form["email"]
        password = request.form["password"]
        password_hash = generate_password_hash(password)
        usuario_existente = Usuarios.query.filter_by(usuario=usuario).first()
        email_existente = Usuarios.query.filter_by(email=email).first()
        if usuario_existente or email_existente:
            flash("Ya existe el usaurio", "error")
            return redirect(url_for("auth.registro"))
        else:
            nuevo_usuario = Usuarios(
                usuario=usuario, email=email, password_hash=password_hash
            )
            db.session.add(nuevo_usuario)
            db.session.commit()
            flash("Usuario registrado correctamente", "success")
            return redirect(url_for("auth.login"))

    return render_template("registro.html")


@auth_routes_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        password = request.form["password"]
        usuario_encontrado = Usuarios.query.filter_by(usuario=usuario).first()
        if usuario_encontrado:
            if check_password_hash(usuario_encontrado.password_hash, password):
                session["usuario"] = usuario_encontrado.usuario
                session["usuario_id"] = usuario_encontrado.id
                return redirect(url_for("tareas.gestionar_tareas"))
            else:
                flash("Usuario o contraseña incorrectos", "error")
        else:
            flash("Usuario o contraseña incorrectos", "error")

    return render_template("login.html")


@auth_routes_bp.route("/logout")
def cerrar_sesion():
    session.pop("usuario")
    return redirect(url_for("auth.login"))
