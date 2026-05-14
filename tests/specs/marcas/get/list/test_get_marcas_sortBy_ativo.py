from tests.clients.marcas_client import MarcasClient  

def test_get_marcas_sortBy_ativo():

    params = {
        "sortBy": "ativo",
        "sortOrder": "ASC"
    }

    response_get = MarcasClient.get_marcas(params=params)

    assert response_get["status_code"] == 200

    body = response_get["body"]

    ativo = [item["ativo"] for item in body["data"]]

    assert ativo == sorted(ativo)


