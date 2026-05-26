from tests.clients.fornecedores_client import FornecedoresClient


def test_get_fornecedor_invalid_sort():

    response_get = FornecedoresClient.get_fornecedores(
        params={
            "sortBy": "campoInvalido",
            "sortOrder": "ASC"
        }
    )

    assert response_get["status_code"] == 400
    assert response_get["body"]["message"][0] == "sortBy must be one of the following values: id, codigo, nome, razaoSocial, createdAt, ativo, pessoa"
    assert response_get["body"]["error"] == "Bad Request"