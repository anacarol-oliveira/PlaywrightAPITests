from tests.clients.marcas_client import MarcasClient

def test_get_marca_all():

    response_get = MarcasClient.get_marcas()

    assert response_get["status_code"] == 200
