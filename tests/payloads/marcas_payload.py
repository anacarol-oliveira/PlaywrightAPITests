from faker import Faker

fake = Faker("pt_BR")


def payload_post_marcas():

    return {
        "nome": fake.company(),
        "observacao": "Marca criada via automacao",
        "ativo": True
    }

def payload_patch_marcas():

    return {
        "nome": f"EDITADO {fake.company()}",
        "observacao": "Marca alterada automaticamente",
        "ativo": False
    }
