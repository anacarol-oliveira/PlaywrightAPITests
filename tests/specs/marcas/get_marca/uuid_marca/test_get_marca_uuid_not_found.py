from tests.clients.marcas_client import MarcasClient

def test_get_marca_uuid_not_found():

    uuid_fake = "11111111-1111-1111-1111-111111111111"

    response_get_uuid = MarcasClient.get_marca_uuid(uuid_fake)

    assert response_get_uuid["status_code"] == 404
    assert response_get_uuid["body"]["message"] == "Marca não encontrada"
    assert response_get_uuid["body"]["error"] == "Not Found"