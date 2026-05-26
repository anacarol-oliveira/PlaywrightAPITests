from tests.clients.marcas_client import MarcasClient


def test_get_marca_sort_created_at_asc():

    response_get = MarcasClient.get_marcas(
        params={
            "sortBy": "createdAt",
            "sortOrder": "ASC"
        }
    )

    assert response_get["status_code"] == 200


def test_get_marca_sort_created_at_desc():

    response_get = MarcasClient.get_marcas(
        params={
            "sortBy": "createdAt",
            "sortOrder": "DESC"
        }
    )

    assert response_get["status_code"] == 200