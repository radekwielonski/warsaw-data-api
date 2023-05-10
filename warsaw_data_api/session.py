import os
from typing import Optional, cast


class Session:
    apikey: Optional[str]

    def __init__(self, apikey: Optional[str] = None) -> None:
        if apikey is None:
            self.apikey = cast(str, os.getenv("WARSAW_DATA_API_KEY"))
        else:
            self.apikey = apikey
