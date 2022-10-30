import traceback
from typing import List

from discogs_client import Client
from discogs_client.exceptions import HTTPError
from discogs_client.models import CollectionItemInstance, Release
from mypy_boto3_secretsmanager.type_defs import GetSecretValueResponseTypeDef

from src.constants.discogs import INVALID_CONSUMER_TOKEN
from src.services.secrets_service import SecretsService


class InventoryService:
    client: Client
    secret: GetSecretValueResponseTypeDef

    def __init__(self):
        secrets_service = SecretsService()
        self.user_token = secrets_service.get_user_token("DiscogsPersonalAccessKey")
        self.client = Client("Wooly/0.1", user_token=self.user_token)

    def get_inventory(self) -> List[Release]:
        """Retrieves the user's inventory"""
        try:
            me = self.client.user("will.kronberg")

            releases: List[Release] = []
            for folder in me.collection_folders:
                item: CollectionItemInstance
                for item in folder.releases:
                    releases.append(item.release)

            return releases
        except HTTPError as error:
            if error.msg == INVALID_CONSUMER_TOKEN:
                raise MissingDiscogsConsumerToken(error)
            else:
                traceback.print_tb(error.__traceback__)
                raise error


class MissingDiscogsConsumerToken(Exception):
    message: str

    def __init__(self, error: HTTPError):
        print(error)
        self.message = error.msg
