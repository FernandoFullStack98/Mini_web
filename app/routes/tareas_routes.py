from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models.models import Tareas_db, db, Usuarios
from app.utils.helpers import buscar_tarea, calcular_tareas, tiempo_transcurrido

tareas_bp = Blueprint("tareas", __name__)


@tareas_bp.route("/tareas", methods=["GET", "POST"])
def gestionar_tareas():
    if "usuario" not in session:
        return redirect(url_for("auth.login"))

    busqueda = request.args.get("buscar", "")
    estado = request.args.get("estado", "todas").strip()
    orden = request.args.get("orden", "nuevas")
    tareas = Tareas_db.query.filter_by(usuario_id=session["usuario_id"])

    if estado == "pendientes":
        tareas = tareas.filter_by(completada=False)
    elif estado == "completadas":
        tareas = tareas.filter_by(completada=True)

    if busqueda:
        tareas = tareas.filter(Tareas_db.tarea.like(f"%{busqueda}%"))

    if orden == "nuevas":
        tareas = tareas.order_by(Tareas_db.fecha_creacion.desc())
    elif orden == "antiguas":
        tareas = tareas.order_by(Tareas_db.fecha_creacion.asc())
    elif orden == "az":
        tareas = tareas.order_by(Tareas_db.tarea.asc())
    elif orden == "za":
        tareas = tareas.order_by(Tareas_db.tarea.desc())

    tareas = tareas.all()

    if request.method == "POST":
        tarea = request.form["tarea"].strip()
        prioridad = request.form["prioridad"]
        if tarea:
            nueva_tarea = Tareas_db(
                tarea=tarea, usuario_id=session["usuario_id"], prioridad=prioridad
            )
            db.session.add(nueva_tarea)
            db.session.commit()
            flash("Tarea creada correctamente", "success")
            return redirect(url_for("tareas.gestionar_tareas"))
        else:
            flash("La tarea no se pudo crear", "error")
            return redirect(url_for("tareas.gestionar_tareas"))

    for tarea in tareas:
        tarea.tiempo_transcurrido = tiempo_transcurrido(tarea.fecha_creacion)
    long_tareas, tareas_totales_completadas, tareas_totales_pendientes = (
        calcular_tareas()
    )

    return render_template(
        "tareas.html",
        tareas=tareas,
        long_tareas=long_tareas,
        tareas_totales_pendientes=tareas_totales_pendientes,
        tareas_totales_completadas=tareas_totales_completadas,
        busqueda=busqueda,
        estado=estado,
        orden=orden,
    )


@tareas_bp.route("/eliminar/<int:id>")
def eliminar_tarea(id):
    tarea = buscar_tarea(id)
    if tarea is None:
        return redirect(url_for("tareas.gestionar_tareas"))

    db.session.delete(tarea)
    db.session.commit()
    return redirect(url_for("tareas.gestionar_tareas"))


@tareas_bp.route("/completar/<int:id>")
def completar(id):
    tarea = buscar_tarea(id)
    if tarea is None:
        return redirect(url_for("tareas.gestionar_tareas"))

    if tarea.completada:
        tarea.completada = False
    else:
        tarea.completada = True

    db.session.commit()
    return redirect(url_for("tareas.gestionar_tareas"))


@tareas_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    tarea = buscar_tarea(id)
    if tarea is None:
        return redirect(url_for("tareas.gestionar_tareas"))

    if request.method == "POST":
        nuevo_texto = request.form["tarea"].strip()
        if nuevo_texto:
            tarea.tarea = nuevo_texto
            db.session.commit()
            flash("Tarea actualizada correctamente")
            return redirect(url_for("tareas.gestionar_tareas"))
        else:
            flash("La tarea no se pudo crear", "error")
            return redirect(url_for("tareas.gestionar_tareas"))
    elif request.method == "GET":
        return render_template("editar.html", tarea=tarea)
