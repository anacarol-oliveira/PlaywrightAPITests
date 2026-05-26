from tests.clients.fornecedores_client import FornecedoresClient
from tests.payloads.fornecedores_payload import payload_post_fornecedores

def test_post_fornecedor_ativo_invalid():

    payload = payload_post_fornecedores()
    payload["ativo"] = "banana"

    response = FornecedoresClient.post_fornecedor(payload)

    assert response["status_code"] == 400
    assert response["body"]["message"][0] == "ativo must be a boolean value"
    assert response["body"]["error"] == "Bad Request"