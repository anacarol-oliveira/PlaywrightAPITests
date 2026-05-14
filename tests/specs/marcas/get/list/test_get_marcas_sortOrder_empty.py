from tests.clients.marcas_client import MarcasClient

def test_get_marcas_sortOrder_empty():

    params = {
        "sortBy": "id",
        "sortOrder": ""
    }

    response_get = MarcasClient.get_marcas(params=params)

    assert response_get["status_code"] == 400
    assert response_get["body"]["message"][0] == "sortOrder must be one of the following values: ASC, DESC"
    assert response_get["body"]["error"] == "Bad Request"

