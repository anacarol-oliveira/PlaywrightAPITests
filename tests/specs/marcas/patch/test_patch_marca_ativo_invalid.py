from tests.clients.marcas_client import MarcasClient
from tests.payloads.marcas_payload import (
    payload_post_marcas,
    payload_patch_marcas
)

def test_patch_marca_ativo_invalid():

    payload_create = payload_post_marcas()

    response_create = MarcasClient.post_marca(payload_create)

    assert response_create["status_code"] == 201

    uuid = response_create["body"]["uuid"]

    payload_update = payload_patch_marcas()
    payload_update["ativo"] = "banana"

    response_patch = MarcasClient.patch_marca(
        uuid=uuid,
        payload=payload_update
    )
    print(response_patch)

    assert response_patch["status_code"] == 400
    assert response_patch["body"]["message"][0] == "ativo must be a boolean value"
    assert response_patch["body"]["error"] == "Bad Request"