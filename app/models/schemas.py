from app.ext import ma
from marshmallow import post_load
from app.models.models import Temperatura


class TemperaturaSchema(ma.Schema):
    class Meta:
        fields = ("id", "temperatura", "fecha", "codigo")
        ordered = True

    @post_load
    def create_temperatura(self, data, **kwargs):
        return Temperatura(**data)

temperatura_schema = TemperaturaSchema()


