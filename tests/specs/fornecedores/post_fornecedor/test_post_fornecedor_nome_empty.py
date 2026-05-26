from tests.clients.fornecedores_client import FornecedoresClient
from tests.payloads.fornecedores_payload import payload_post_fornecedores

def test_post_fornecedor_nome_empty():

    payload = payload_post_fornecedores()
    payload["nome"] = ""

    response = FornecedoresClient.post_fornecedor(payload)

    assert response["status_code"] == 400
    assert response["body"]["message"][0] == "nome must be longer than or equal to 2 characters"
    assert response["body"]["error"] == "Bad Request"