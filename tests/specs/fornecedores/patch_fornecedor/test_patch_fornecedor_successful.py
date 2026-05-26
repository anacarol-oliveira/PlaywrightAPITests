from tests.clients.fornecedores_client import FornecedoresClient
from tests.payloads.fornecedores_payload import (
    payload_post_fornecedores,
    payload_patch_fornecedores
)

def test_patch_fornecedor_successful():

    payload_create = payload_post_fornecedores()

    response_create = FornecedoresClient.post_fornecedor(payload_create)

    assert response_create["status_code"] == 201

    uuid = response_create["body"]["uuid"]

    ativo_atual = response_create["body"]["ativo"]

    payload_update = payload_patch_fornecedores(ativo_atual)

    response_patch = FornecedoresClient.patch_fornecedor(
        uuid=uuid,
        payload=payload_update
    )
    print(response_patch)

    assert response_patch["status_code"] == 200
    assert response_patch["body"]["codigo"] == payload_update["codigo"]
    assert response_patch["body"]["nome"] == payload_update["nome"]
    assert response_patch["body"]["pessoa"] == payload_update["pessoa"]
    assert response_patch["body"]["razaoSocial"] == payload_update["razaoSocial"]
    assert response_patch["body"]["documentoFiscal"] == payload_update["documentoFiscal"]
    assert response_patch["body"]["inscricaoEstadual"] == payload_update["inscricaoEstadual"]
    assert response_patch["body"]["cep"] == payload_update["cep"]
    assert response_patch["body"]["logradouro"] == payload_update["logradouro"]
    assert response_patch["body"]["numero"] == payload_update["numero"]
    assert response_patch["body"]["complemento"] == payload_update["complemento"]
    assert response_patch["body"]["bairro"] == payload_update["bairro"]
    assert response_patch["body"]["ibgeCidade"] == payload_update["ibgeCidade"]
    assert response_patch["body"]["uf"] == payload_update["uf"]
    assert response_patch["body"]["observacao"] == payload_update["observacao"]
    assert response_patch["body"]["ativo"] == payload_update["ativo"]