from tests.clients.marcas_client import MarcasClient

def test_get_marcas_sortBy_createdAt():

    params = {
        "sortBy": "createdAt",
        "sortOrder": "ASC"
    }

    response_get = MarcasClient.get_marcas(params=params)

    assert response_get["status_code"] == 200

    body = response_get["body"]

    createdAt = [item["createdAt"] for item in body["data"]]

    assert createdAt == sorted(createdAt)    