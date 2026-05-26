from tests.clients.fornecedores_client import FornecedoresClient

def test_get_fornecedor_filter_search():

    response_get = FornecedoresClient.get_fornecedores(
        params={
            "search": "a"
        }
    )

    assert response_get["status_code"] == 200