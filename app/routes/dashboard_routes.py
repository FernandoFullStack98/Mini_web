from flask import Blueprint, session, redirect, url_for, render_template
from app.utils.helpers import calcular_tareas
from app.models.models import Tareas_db
from app.utils.helpers import tiempo_transcurrido
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
    long_tareas, tareas_totales_completadas, tareas_totales_pendientes = (
        calcular_tareas()
    )

    ultimas_tareas_pendientes = (
        Tareas_db.query.filter_by(usuario_id=session["usuario_id"], completada=False)
        .order_by(Tareas_db.fecha_creacion.desc())
        .limit(5)
        .all()
    )

    long_tareas, tareas_totales_completadas, tareas_totales_pendientes = (
        calcular_tareas()
    )

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
    )
