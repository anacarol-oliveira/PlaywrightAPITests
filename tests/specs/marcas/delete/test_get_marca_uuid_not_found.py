from tests.clients.marcas_client import MarcasClient

def test_get_marca_uuid_not_found():

    uuid_fake = "11111111-1111-1111-1111-111111111111"

    response_delete = MarcasClient.delete_marca(uuid_fake)

    assert response_delete["status_code"] == 404
    assert response_delete["body"]["message"] == "Marca não encontrada"
    assert response_delete["body"]["error"] == "Not Found"