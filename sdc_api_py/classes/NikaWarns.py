from .. import _types
from .Lib import Querier


class NikaWarns:

    def __init__(self, token):
        if not token.startswith("SDC "):
            token = f"SDC {token}"
        self.SDC_token = token
        self.querier = Querier()

    async def fetch_warns(self, _id:int):
        _id = _id

        response = await self.querier.execute_get_query(
            f"https://api.server-discord.com/v2/warns/{_id}",
            headers={"Authorization": f"{self.SDC_token}"}
        )

        data = await response.json()

        SdcNikaWarns = _types.SdcNikaWarns()

        SdcNikaWarns.id     = data["id"]
        SdcNikaWarns.type   = data["type"]
        SdcNikaWarns.warns  = data["warns"]

        return SdcNikaWarns
