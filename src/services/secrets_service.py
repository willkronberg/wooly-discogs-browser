import boto3
from mypy_boto3_secretsmanager import SecretsManagerClient
from mypy_boto3_secretsmanager.type_defs import GetSecretValueResponseTypeDef


class SecretsService:
    session: boto3.Session
    client: SecretsManagerClient

    def __init__(self):
        self.session = boto3.Session
        self.client = boto3.client(
            service_name="secretsmanager", region_name="us-west-2",
        )

    def get_secret_value(self, secret_name: str) -> GetSecretValueResponseTypeDef:
        return self.client.get_secret_value(SecretId=secret_name)
