from tests.clients.fornecedores_client import FornecedoresClient
from tests.payloads.fornecedores_payload import payload_post_fornecedores
from faker import Faker

fake = Faker("pt_BR")

def test_post_fornecedor_cpf_successful():

    payload = payload_post_fornecedores()
    payload["pessoa"] = "F"
    payload["razaoSocial"] = None
    payload["documentoFiscal"] = fake.cpf()
    payload["inscricaoEstadual"] = None

    response = FornecedoresClient.post_fornecedor(payload)
    print(response)
           
    assert response["status_code"] == 201
    assert response["body"]["codigo"] == payload["codigo"]
    assert response["body"]["nome"] == payload["nome"]
    assert response["body"]["pessoa"] == payload["pessoa"]
    assert response["body"]["razaoSocial"] == payload["razaoSocial"]
    assert response["body"]["documentoFiscal"] == payload["documentoFiscal"]
    assert response["body"]["inscricaoEstadual"] == payload["inscricaoEstadual"]
    assert response["body"]["cep"] == payload["cep"]
    assert response["body"]["logradouro"] == payload["logradouro"]
    assert response["body"]["numero"] == payload["numero"]
    assert response["body"]["complemento"] == payload["complemento"]
    assert response["body"]["bairro"] == payload["bairro"]
    assert response["body"]["ibgeCidade"] == payload["ibgeCidade"]
    assert response["body"]["uf"] == payload["uf"]
    assert response["body"]["observacao"] == payload["observacao"]
    assert response["body"]["ativo"] == payload["ativo"]