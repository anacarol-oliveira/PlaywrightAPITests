from tests.clients.marcas_client import MarcasClient
from tests.payloads.marcas_payload import payload_post_marcas

def test_get_marca_uuid_successful():

    payload = payload_post_marcas()

    response_post = MarcasClient.post_marca(payload)

    uuid = response_post["body"]["uuid"]

    response_get_uuid = MarcasClient.get_marca_uuid(uuid)

    assert response_get_uuid["status_code"] == 200

    body = response_get_uuid["body"]

    assert body["uuid"] == uuid
    assert body["nome"] == payload["nome"]