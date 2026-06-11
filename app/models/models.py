from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Tareas_db(db.Model):
    __tablename__ = "task"

    id = db.Column(db.Integer, primary_key=True)
    tarea = db.Column(db.String(100), nullable=False)
    completada = db.Column(db.Boolean, default=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    fecha_creacion = db.Column(db.DateTime, default=datetime.now)
    prioridad = db.Column(db.String(20), default="Media")


class Usuarios(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(200), unique=True)
    password_hash = db.Column(db.String(300), nullable=False)
    tareas = db.relationship("Tareas_db", backref="usuario", lazy=True)
