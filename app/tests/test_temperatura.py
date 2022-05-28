import json

ENDPOINT = "/api/temperatura"


def test_api_temperatura_list(test_client):
    response = test_client.get(f"{ENDPOINT}/listar")

    assert response.status_code == 200
    assert response.json["data"] == []


def test_api_temperatura_save(test_client):
    temperatura = {
        "temperatura": "35",
        "fecha": "2022-06-18T05:30:00",
        "codigo": "AAA01",
    }

    response = test_client.post(
        f"{ENDPOINT}/registrar",
        data=json.dumps(temperatura),
        content_type="application/json",
    )

    assert response.status_code == 201
