from app.models.models import Tareas_db
from flask import flash, session
from datetime import datetime


def buscar_tarea(id):
    tarea = Tareas_db.query.filter_by(id=id, usuario_id=session["usuario_id"]).first()
    if tarea is None:
        flash("No existe la tarea", "Error")
        return None
    return tarea


def calcular_tareas():
    tareas = Tareas_db.query.filter_by(usuario_id=session["usuario_id"]).all()
    long_tareas = len(tareas)
    tareas_pendiente = Tareas_db.query.filter_by(
        usuario_id=session["usuario_id"], completada=False
    ).all()
    tareas_totales_pendientes = len(tareas_pendiente)
    tareas_completadas = Tareas_db.query.filter_by(
        usuario_id=session["usuario_id"], completada=True
    ).all()
    tareas_totales_completadas = len(tareas_completadas)
    return long_tareas, tareas_totales_completadas, tareas_totales_pendientes


def tiempo_transcurrido(fecha_creacion):
    ahora = datetime.now()
    diferencia = ahora - fecha_creacion
    segundos = int(diferencia.total_seconds())
    minuto = int(segundos // 60)
    hora = int(segundos // 3600)
    dia = int(segundos // 86400)
    if segundos < 60:
        if segundos == 1:
            return f"Hace {segundos} segundo"
        else:
            return f"Hace {segundos} segundos"
    elif segundos < 3600:
        if minuto == 1:
            return f"Hace {minuto} minuto"
        else:
            return f"Hace {minuto} minutos"
    elif segundos < 86400:
        if hora == 1:
            return f"Hace {hora} hora"
        else:
            return f"Hace {hora} horas"
    else:
        if dia == 1:
            return f"Hace {dia} dia"
        else:
            return f"Hace {dia} dias"
