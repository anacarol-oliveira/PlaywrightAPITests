from tests.clients.marcas_client import MarcasClient
from tests.payloads.marcas_payload import payload_post_marcas

def test_post_marca_successful():

    payload = payload_post_marcas()

    response = MarcasClient.post_marca(payload)
    print(response)

    assert response["status_code"] == 201
    assert response["body"]["nome"] == payload["nome"]
    assert response["body"]["observacao"] == payload["observacao"]
    assert response["body"]["ativo"] == payload["ativo"]