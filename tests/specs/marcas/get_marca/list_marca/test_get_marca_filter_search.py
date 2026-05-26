from tests.clients.marcas_client import MarcasClient


def test_get_marca_filter_search():

    response_get = MarcasClient.get_marcas(
        params={
            "search": "Viana"
        }
    )

    assert response_get["status_code"] == 200