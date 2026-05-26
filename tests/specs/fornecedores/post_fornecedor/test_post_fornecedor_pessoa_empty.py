from tests.clients.fornecedores_client import FornecedoresClient
from tests.payloads.fornecedores_payload import payload_post_fornecedores

def test_post_fornecedor_pessoa_empty():

    payload = payload_post_fornecedores()
    payload["pessoa"] = ""

    response = FornecedoresClient.post_fornecedor(payload)

    assert response["status_code"] == 400
    assert response["body"]["message"] == ["pessoa must be one of the following values: F, J", "pessoa must be longer than or equal to 1 characters"]
    assert response["body"]["error"] == "Bad Request"