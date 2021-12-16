import os
from typing import cast


class Session:
    apikey: str

    def __init__(self, apikey: str = None) -> None:
        if apikey is None:
            self.apikey = cast(str, os.getenv("WARSAW_DATA_API_KEY"))
        else:
            self.apikey = apikey
