from tests.clients.marcas_client import MarcasClient
from tests.payloads.marcas_payload import payload_post_marcas


def test_delete_marca_successful():

    payload = payload_post_marcas()

    response_post = MarcasClient.post_marca(payload)

    uuid = response_post["body"]["uuid"]

    response_delete = MarcasClient.delete_marca(uuid)

    assert response_delete["status_code"] == 200
