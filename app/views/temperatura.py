from flask import Blueprint, Response, jsonify, request
from app.models.models import Temperatura
from app.models.schemas import temperatura_schema

temperatura = Blueprint("temperatura", __name__)


@temperatura.get("/listar")
def listar_temperatura():
    lista_temperaturas = Temperatura.get_all()
    json_temperaturas = temperatura_schema.dump(lista_temperaturas, many=True)

    return jsonify({
        "estado": True,
        "message": "datos de temperatura",
        "data": json_temperaturas}
    ), 200


@temperatura.post("/registrar")
def registrar_temperaturas():
    json_data = request.get_json()
    temperatura_model = temperatura_schema.load(json_data)
    temperatura_model.save()
    return Response(status=201)
