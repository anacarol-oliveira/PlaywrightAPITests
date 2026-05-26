from tests.clients.fornecedores_client import FornecedoresClient

def test_get_fornecedor_filter_uf():

    response = FornecedoresClient.get_fornecedores(
        params={
            "uf": "SP"
        }
    )

    assert response["status_code"] == 200