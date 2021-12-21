import os
from typing import cast, Union


class Session:
    apikey: Union[str, None]

    def __init__(self, apikey: Union[str, None] = None) -> None:
        if apikey is None:
            self.apikey = cast(str, os.getenv("WARSAW_DATA_API_KEY"))
        else:
            self.apikey = apikey
