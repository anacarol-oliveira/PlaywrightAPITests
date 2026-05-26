from faker import Faker
import random

fake = Faker("pt_BR")


def payload_post_marcas():

    return {
        "nome": fake.company(),
        "observacao": "Marca criada via automacao",
        "ativo": random.choice([True, False])
    }

def payload_patch_marcas(ativo_atual):

    return {
        "nome": f"EDITADO {fake.company()}",
        "observacao": "Marca alterada automaticamente",
        "ativo": not ativo_atual
    }
