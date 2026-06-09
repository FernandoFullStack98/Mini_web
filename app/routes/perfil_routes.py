from flask import Blueprint, request, render_template, session, redirect, url_for, flash
from app.models.models import Usuarios, db
from app.utils.helpers import calcular_tareas
from werkzeug.security import check_password_hash, generate_password_hash

perfil_bp = Blueprint("perfil", __name__)


@perfil_bp.route("/perfil", methods=["GET", "POST"])
def perfil():
    if "usuario" not in session:
        return redirect(url_for("auth.login"))
    else:
        usuario = Usuarios.query.filter_by(id=session["usuario_id"]).first()
        long_tareas, tareas_totales_completadas, tareas_totales_pendientes = (
            calcular_tareas()
        )
        if request.method == "POST":
            if "email_new" in request.form:
                email = request.form["nuevo_mail"].strip()
                if email:
                    usuario.email = email
                    db.session.commit()
                    flash("Email actualizado correctamente", "success")
                    return redirect(url_for("perfil.perfil"))
                else:
                    flash("No ha actiualizado el email", "error")
                    return redirect(url_for("perfil.perfil"))
            elif "password_new" in request.form:
                contraseña_nueva = request.form["password_nueva"].strip()
                contraseña_repetida = request.form["password_repetida"].strip()
                contraseña_antigua = request.form["password_actual"].strip()
                if contraseña_nueva == contraseña_repetida:
                    if check_password_hash(usuario.password_hash, contraseña_antigua):
                        hash_new_password = generate_password_hash(contraseña_nueva)
                        usuario.password_hash = hash_new_password
                        db.session.commit()
                        flash("Contraseña cambiada correctamente", "success")
                        return redirect(url_for("perfil.perfil"))
                    else:
                        flash("Contraseña antigua no coincide", "error")
                        return redirect(url_for("perfil.perfil"))
                else:
                    flash("La contraseña no coincide", "error")
                    return redirect(url_for("perfil.perfil"))

        return render_template(
            "perfil.html",
            usuario=usuario,
            long_tareas=long_tareas,
            tareas_totales_completadas=tareas_totales_completadas,
            tareas_totales_pendientes=tareas_totales_pendientes,
        )
