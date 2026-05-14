from tests.clients.marcas_client import MarcasClient

def test_get_marcas_sortOrder_desc():

    params = {
        "sortBy": "id",
        "sortOrder": "DESC"
    }

    response_get = MarcasClient.get_marcas(params=params)

    assert response_get["status_code"] == 200

    body = response_get["body"]

    ids = [item["id"] for item in body["data"]]

    assert ids == sorted(ids, reverse=True)


