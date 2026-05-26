from tests.clients.fornecedores_client import FornecedoresClient
from tests.payloads.fornecedores_payload import payload_post_fornecedores


def test_delete_fornecedor_successful():

    payload = payload_post_fornecedores()

    response_post = FornecedoresClient.post_fornecedor(payload)

    uuid = response_post["body"]["uuid"]

    response_delete = FornecedoresClient.delete_fornecedor(uuid)

    assert response_delete["status_code"] == 200
