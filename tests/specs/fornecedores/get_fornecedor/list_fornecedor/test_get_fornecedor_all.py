from tests.clients.fornecedores_client import FornecedoresClient

def test_get_fornecedores_all():


    response_get = FornecedoresClient.get_fornecedores()

    assert response_get["status_code"] == 200
