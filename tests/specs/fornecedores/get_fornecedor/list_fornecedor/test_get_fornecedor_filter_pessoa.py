from tests.clients.fornecedores_client import FornecedoresClient

def test_get_fornecedor_filter_pessoa():

    response_get = FornecedoresClient.get_fornecedores(
        params={
            "pessoa": "F"
        }
    )

    assert response_get["status_code"] == 200