from flask import Blueprint, session, redirect, url_for, render_template
from app.utils.helpers import calcular_tareas, tiempo_transcurrido, calcular_prioridad
from app.models.models import Tareas_db
from datetime import datetime

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard")
def dashboard():
    if "usuario" not in session:
        return redirect(url_for("auth.login"))

    ultimas_tareas = (
        Tareas_db.query.filter_by(usuario_id=session["usuario_id"])
        .order_by(Tareas_db.fecha_creacion.desc())
        .limit(5)
        .all()
    )

    for tarea in ultimas_tareas:
        tarea.tiempo_transcurrido = tiempo_transcurrido(tarea.fecha_creacion)

    ultimas_tareas_pendientes = (
        Tareas_db.query.filter_by(usuario_id=session["usuario_id"], completada=False)
        .order_by(Tareas_db.fecha_creacion.desc())
        .limit(5)
        .all()
    )

    long_tareas, tareas_totales_completadas, tareas_totales_pendientes = (
        calcular_tareas()
    )

    long_alta_prio, long_media_prio, long_baja_prio = calcular_prioridad()

    tareas_creadas_hoy = 0

    tareas = Tareas_db.query.filter_by(usuario_id=session["usuario_id"]).all()

    for tarea in tareas:
        if tarea.fecha_creacion.date() == datetime.now().date():
            tareas_creadas_hoy += 1

    return render_template(
        "dashboard.html",
        long_tareas=long_tareas,
        tareas_totales_completadas=tareas_totales_completadas,
        tareas_totales_pendientes=tareas_totales_pendientes,
        ultimas_tareas=ultimas_tareas,
        ultimas_tareas_pendientes=ultimas_tareas_pendientes,
        tareas_creadas_hoy=tareas_creadas_hoy,
        long_alta_prio=long_alta_prio,
        long_media_prio=long_media_prio,
        long_baja_prio=long_baja_prio,
    )
