from tests.clients.marcas_client import MarcasClient
from tests.payloads.marcas_payload import (
    payload_post_marcas,
    payload_patch_marcas
)

def test_patch_marca_successful():

    payload_create = payload_post_marcas()

    response_create = MarcasClient.post_marca(payload_create)

    assert response_create["status_code"] == 201

    uuid = response_create["body"]["uuid"]

    ativo_atual = response_create["body"]["ativo"]

    payload_update = payload_patch_marcas(ativo_atual)

    response_patch = MarcasClient.patch_marca(
        uuid=uuid,
        payload=payload_update
    )
    print(response_patch)

    assert response_patch["status_code"] == 200
    assert response_patch["body"]["nome"] == payload_update["nome"]
    assert response_patch["body"]["observacao"] == payload_update["observacao"]
    assert response_patch["body"]["ativo"] == payload_update["ativo"]