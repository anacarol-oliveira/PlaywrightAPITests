from tests.clients.fornecedores_client import FornecedoresClient


def test_get_fornecedores_filter_ativo_true():

    response_get = FornecedoresClient.get_fornecedores(
        params={
            "ativo": True
        }
    )

    assert response_get["status_code"] == 200


def test_get_fornecedores_filter_ativo_false():

    response_get = FornecedoresClient.get_fornecedores(
        params={
            "ativo": False
        }
    )

    assert response_get["status_code"] == 200