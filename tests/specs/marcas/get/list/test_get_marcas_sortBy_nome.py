from tests.clients.marcas_client import MarcasClient

def test_get_marcas_sortBy_nome():

    params = {
        "sortBy": "nome",
        "sortOrder": "ASC"
    }

    response_get = MarcasClient.get_marcas(params=params)

    assert response_get["status_code"] == 200

