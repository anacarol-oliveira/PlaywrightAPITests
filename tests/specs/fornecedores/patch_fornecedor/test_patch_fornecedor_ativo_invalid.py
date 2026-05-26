from tests.clients.fornecedores_client import FornecedoresClient
from tests.payloads.fornecedores_payload import (
    payload_post_fornecedores,
    payload_patch_fornecedores
)

def test_patch_fornecedor_nome_empty():

    payload_create = payload_post_fornecedores()

    response_create = FornecedoresClient.post_fornecedor(payload_create)

    assert response_create["status_code"] == 201

    uuid = response_create["body"]["uuid"]

    ativo_atual = response_create["body"]["ativo"]

    payload_update = payload_patch_fornecedores(ativo_atual)
    payload_update["ativo"] = "banana"

    response_patch = FornecedoresClient.patch_fornecedor(
        uuid=uuid,
        payload=payload_update
    )
    print(response_patch)

    assert response_patch["status_code"] == 400
    assert response_patch["body"]["message"][0] == "ativo must be a boolean value"
    assert response_patch["body"]["error"] == "Bad Request"