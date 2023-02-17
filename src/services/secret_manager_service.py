from google.cloud import secretmanager

class SecretManagerService():
    client = secretmanager.SecretManagerServiceClient()

    def __init__(self, project_id) -> None:
        self.project_id = project_id

    def get_secret_version(self, secret_id, version_id="latest"):
        name = f'projects/{self.project_id}/secrets/{secret_id}/versions/{version_id}'

        response = self.client.access_secret_version(name=name)

        return response.payload.data.decode("UTF-8")