from tests.clients.base_client import BaseClient

class MarcasClient:

    @staticmethod
    def post_marca(payload):

        return BaseClient.post(
            endpoint="/marcas",
            payload=payload
        )
    
    @staticmethod
    def get_marcas(params=None):

        return BaseClient.get(
            endpoint="/marcas",
            params=params
        )

    @staticmethod
    def get_marca_uuid(uuid):

        return BaseClient.get(
            endpoint=f"/marcas/{uuid}"
        )
    
    @staticmethod
    def patch_marca(uuid, payload):

        return BaseClient.patch(
            endpoint=f"/marcas/{uuid}",
            payload=payload
        )

    @staticmethod
    def delete_marca(uuid):

        return BaseClient.delete(
            endpoint=f"/marcas/{uuid}"
        )