from tests.clients.marcas_client import MarcasClient
from tests.payloads.marcas_payload import payload_post_marcas

def test_post_marca_nome_empty():

    payload = payload_post_marcas()
    payload["nome"] = ""

    response = MarcasClient.post_marca(payload)

    assert response["status_code"] == 400
    assert response["body"]["message"][0] == "nome must be longer than or equal to 2 characters"
    assert response["body"]["error"] == "Bad Request"