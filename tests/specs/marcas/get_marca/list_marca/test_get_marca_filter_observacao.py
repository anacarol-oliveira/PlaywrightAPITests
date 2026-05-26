from tests.clients.marcas_client import MarcasClient


def test_get_marca_filter_observacao():

    response_get = MarcasClient.get_marcas(
        params={
            "observacao": "teste"
        }
    )

    assert response_get["status_code"] == 200