#from tests.clients.fornecedores_client import fornecedoresClient
#from tests.payloads.fornecedores_payload import payload_post_fornecedores

#def test_post_fornecedor_nome_empty():

#    payload = payload_post_fornecedores()
#    payload["codigo"] = ""

#    response = fornecedoresClient.post_fornecedor(payload)

#    assert response["status_code"] == 400
#    assert response["body"]["message"][0] == ""
#    assert response["body"]["error"] == "Bad Request"