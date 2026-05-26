from faker import Faker
import random

fake = Faker("pt_BR")


def payload_post_fornecedores():

    return {
        "codigo": random.randint(1000, 9999),
        "nome": fake.name(),
        "pessoa": "J",
        "razaoSocial": fake.company(),
        "documentoFiscal": fake.cnpj(),
        "inscricaoEstadual": str(fake.random_number(digits=7, fix_len=True)),
        "cep": fake.postcode(),
        "logradouro": fake.street_name(),
        "numero": str(fake.building_number()),
        "complemento": fake.text(max_nb_chars=100),
        "bairro": fake.bairro(),
        "ibgeCidade": str(fake.random_number(digits=7, fix_len=True)),
        "uf": fake.estado_sigla(),
        "observacao": "Fornecedor criado automaticamente",
        "ativo": random.choice([True, False])
    }

def payload_patch_fornecedores(ativo_atual):

    return {
        "codigo": random.randint(1000, 9999),
        "nome": f"EDITADO {fake.name()}",
        "pessoa": "F",
        "razaoSocial": f"EDITADO {fake.company()}",
        "documentoFiscal": fake.cpf(),
        "inscricaoEstadual": f"EDITADO {str(fake.random_number(digits=7, fix_len=True))}",
        "cep": fake.postcode(),
        "logradouro": f"EDITADO {fake.street_name()}",
        "numero": f"EDITADO {str(fake.building_number())}",
        "complemento": f"EDITADO {fake.text(max_nb_chars=100)}",
        "bairro": f"EDITADO {fake.bairro()}",
        "ibgeCidade": str(fake.random_number(digits=7, fix_len=True)),
        "uf": fake.estado_sigla(),
        "observacao": "Fornecedor alterado automaticamente",
        "ativo": not ativo_atual
    }
