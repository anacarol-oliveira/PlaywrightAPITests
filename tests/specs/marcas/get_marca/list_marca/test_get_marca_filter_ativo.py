from tests.clients.marcas_client import MarcasClient


def test_get_marca_filter_ativo_true():

    response_get = MarcasClient.get_marcas(
        params={
            "ativo": True
        }
    )

    assert response_get["status_code"] == 200


def test_get_marca_filter_ativo_false():

    response_get = MarcasClient.get_marcas(
        params={
            "ativo": False
        }
    )

    assert response_get["status_code"] == 200