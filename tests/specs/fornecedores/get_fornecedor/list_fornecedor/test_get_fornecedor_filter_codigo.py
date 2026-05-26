from tests.clients.fornecedores_client import FornecedoresClient

def test_get_fornecedor_codigo():

    response_get = FornecedoresClient.get_fornecedores(
        params={
            "codigo": 1
        }
    )

    assert response_get["status_code"] == 200