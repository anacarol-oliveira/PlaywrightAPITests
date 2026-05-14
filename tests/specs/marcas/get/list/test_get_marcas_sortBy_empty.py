from tests.clients.marcas_client import MarcasClient

def test_get_marcas_sortBy_empty():

    params = {
        "sortBy": "",
        "sortOrder": "ASC"
    }

    response_get = MarcasClient.get_marcas(params=params)

    assert response_get["status_code"] == 400
    assert response_get["body"]["message"][0] == "sortBy must be one of the following values: id, nome, createdAt, ativo"
    assert response_get["body"]["error"] == "Bad Request"

