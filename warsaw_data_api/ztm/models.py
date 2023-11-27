from dataclasses import dataclass
from datetime import datetime
from typing import List
from warsaw_data_api.exceptions import (
    LongitudeOutsideBoundaryException,
    LatitudeOutsideBoundaryException,
)


@dataclass
class Location:
    longitude: float
    latitude: float

    def __init__(self, longitude: float, latitude: float) -> None:
        if longitude >= -180 and longitude <= 180:
            self.longitude = longitude
        else:
            raise LongitudeOutsideBoundaryException(longitude)

        if latitude >= -90 and latitude <= 90:
            self.latitude = latitude
        else:
            raise LatitudeOutsideBoundaryException(latitude)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Location):
            raise NotImplementedError
        return self.__dict__ == other.__dict__


class ZtmVehicle:
    location: Location
    line: str
    vehicle_number: str
    time: datetime
    brigade: str
    type: int

    def __init__(
        self,
        location: Location,
        line: str,
        vehicle_number: str,
        time: datetime,
        brigade: str,
        type: int,
    ) -> None:
        self.location = location
        self.lines = line
        self.vehicle_number = vehicle_number
        self.time = time
        self.brigade = brigade
        self.type = type

    def __str__(self) -> str:
        return (
            f"ZtmVehicle(line={self.lines}, type={self.type}, "
            f"lat={self.location.latitude}, lon={self.location.longitude})"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ZtmVehicle):
            raise NotImplementedError
        return self.__str__() == other.__str__()


@dataclass
class ZtmRide:
    brigade: str
    direction: str
    route: str
    time: str

    def __init__(self, brigade: str, direction: str, route: str, time: str) -> None:
        self.brigade = brigade
        self.direction = direction
        self.route = route
        self.time = time

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ZtmRide):
            raise NotImplementedError
        return self.__dict__ == other.__dict__


class ZtmSchedule:
    line: str
    bus_stop_id: int
    bus_stop_nr: str
    rides: List[ZtmRide]

    def __init__(
        self,
        line: str,
        bus_stop_id: int,
        bus_stop_nr: str,
        rides: List[ZtmRide],
    ) -> None:
        self.line = line
        self.bus_stop_id = bus_stop_id
        self.bus_stop_nr = bus_stop_nr
        self.rides = rides

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ZtmSchedule):
            raise NotImplementedError
        return self.__dict__ == other.__dict__
