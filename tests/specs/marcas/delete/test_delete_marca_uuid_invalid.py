from tests.clients.marcas_client import MarcasClient

def test_delete_marca_uuid_invalid():

    response_delete = MarcasClient.delete_marca("123")

    assert response_delete["status_code"] == 400
    assert response_delete["body"]["message"] == "Validation failed (uuid is expected)"
    assert response_delete["body"]["error"] == "Bad Request"
