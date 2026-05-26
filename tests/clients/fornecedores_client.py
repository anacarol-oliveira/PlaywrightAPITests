from tests.clients.base_client import BaseClient

class FornecedoresClient:

    @staticmethod
    def post_fornecedor(payload):

        return BaseClient.post(
            endpoint="/fornecedores",
            payload=payload
        )
    
    @staticmethod
    def get_fornecedores(params=None):

        return BaseClient.get(
            endpoint="/fornecedores",
            params=params
        )

    @staticmethod
    def get_fornecedor_uuid(uuid):

        return BaseClient.get(
            endpoint=f"/fornecedores/{uuid}"
        )
    
    @staticmethod
    def patch_fornecedor(uuid, payload):

        return BaseClient.patch(
            endpoint=f"/fornecedores/{uuid}",
            payload=payload
        )

    @staticmethod
    def delete_fornecedor(uuid):

        return BaseClient.delete(
            endpoint=f"/fornecedores/{uuid}"
        )