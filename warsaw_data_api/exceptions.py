# All exceptions in this class should subclass from WarsawDataApiException
class WarsawDataApiException(Exception):
    """Base class for all warsaw-data-api errors."""


class LongitudeOutsideBoundaryException(WarsawDataApiException):
    def __init__(
        self, longitude, message="Longitude is not in (-180, 180) range"
    ):
        self.longitude = longitude
        self.message = message
        super().__init__(self.message)


class LatitudeOutsideBoundaryException(WarsawDataApiException):
    def __init__(self, latitude, message="Latitude is not in (-90, 90) range"):
        self.latitude = latitude
        self.message = message
        super().__init__(self.message)
