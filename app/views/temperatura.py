from flask import Blueprint, Response, jsonify, request
from app.models.models import Temperatura
from app.models.schemas import temperatura_schema

temperatura = Blueprint("temperatura", __name__)


@temperatura.get("/listar")
def listar_temperatura():
    lista_temperaturas = Temperatura.get_all()
    json_temperaturas = temperatura_schema.dump(lista_temperaturas, many=True)
    return jsonify(json_temperaturas), 200


@temperatura.post("/registrar")
def registrar_temperaturas():
    json_data = request.get_json()
    temperatura = temperatura_schema.load(json_data)
    temperatura.save()
    return Response(status=201)
