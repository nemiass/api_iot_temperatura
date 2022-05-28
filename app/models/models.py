from app.db import db
from app.db import BaseModelMixin


class Temperatura(db.Model, BaseModelMixin):

    __tablename__ = "temperatura_historial"

    id = db.Column(db.Integer, primary_key=True)
    temperatura = db.Column(db.String(50), nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    codigo = db.Column(db.String(50), nullable=False)

    def __init__(self, temperatura: str, fecha: str, codigo: str) -> None:
        self.temperatura = temperatura
        self.fecha = fecha
        self.codigo = codigo
