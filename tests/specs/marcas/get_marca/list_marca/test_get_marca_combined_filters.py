from tests.clients.marcas_client import MarcasClient


def test_get_marca_combined_filters():

    response_get = MarcasClient.get_marcas(
        params={
            "ativo": True,
            "search": "a",
            "sortBy": "createdAt",
            "sortOrder": "ASC"
        }
    )

    assert response_get["status_code"] == 200