from tests.clients.marcas_client import MarcasClient

def test_get_marca_uuid_invalid():

    response_get_uuid = MarcasClient.get_marca_uuid("123")

    assert response_get_uuid["status_code"] == 400
    assert response_get_uuid["body"]["message"] == "Validation failed (uuid is expected)"
    assert response_get_uuid["body"]["error"] == "Bad Request"
