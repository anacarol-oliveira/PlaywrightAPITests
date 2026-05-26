from tests.clients.marcas_client import MarcasClient
from tests.payloads.marcas_payload import payload_post_marcas

def test_post_marca_ativo_invalid():

    payload = payload_post_marcas()
    payload["ativo"] = "banana"

    response = MarcasClient.post_marca(payload)

    assert response["status_code"] == 400
    assert response["body"]["message"][0] == "ativo must be a boolean value"
    assert response["body"]["error"] == "Bad Request"