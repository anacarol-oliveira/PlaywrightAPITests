from tests.clients.fornecedores_client import FornecedoresClient


def test_get_fornecedor_sort_asc():

    response_get = FornecedoresClient.get_fornecedores(
        params={
            "sortBy": "razaoSocial",
            "sortOrder": "ASC"
        }
    )

    assert response_get["status_code"] == 200


def test_get_fornecedor_sort_desc():

    response_get = FornecedoresClient.get_fornecedores(
        params={
            "sortBy": "razaoSocial",
            "sortOrder": "DESC"
        }
    )

    assert response_get["status_code"] == 200