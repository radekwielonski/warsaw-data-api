from warsaw_data_api.ztm import ZtmSession
from typing import Union


__author__ = "Radoslaw Wielonski"
__version__ = "0.2.1"


# factory functions
def ztm(apikey: Union[str, None]) -> ZtmSession:
    return ZtmSession(apikey=apikey)
