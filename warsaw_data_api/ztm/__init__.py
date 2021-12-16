from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict, Union
import requests
from warsaw_data_api.exceptions import (
    LongitudeOutsideBoundaryException,
    LatitudeOutsideBoundaryException,
)
from warsaw_data_api.session import Session


@dataclass
class Location:
    longitude: float
    latitude: float

    def __init__(self, longitude: float, latitude: float):
        if longitude >= -180 and longitude <= 180:
            self.longitude = longitude
        else:
            raise LongitudeOutsideBoundaryException(longitude)

        if latitude >= -90 and latitude <= 90:
            self.latitude = latitude
        else:
            raise LatitudeOutsideBoundaryException(latitude)


class ZtmVehicle:
    location: Location
    lines: str
    vehicle_number: str
    time: datetime
    brigade: str
    type: int

    def __init__(
        self,
        location: Location,
        lines: str,
        vehicle_number: str,
        time: datetime,
        brigade: str,
        type: int,
    ):
        self.location = location
        self.lines = lines
        self.vehicle_number = vehicle_number
        self.time = time
        self.brigade = brigade
        self.type = type

    def __str__(self):
        return f"ZtmVehicle(line={self.lines}, type={self.type}, lat={self.location.latitude}, lon={self.location.longitude})"


class ZtmSession(Session):
    def __init__(self, apikey: str = None) -> None:
        super().__init__(apikey=apikey)

    def __parse_vehicle_location_data(self, record, vehicle_type: int) -> ZtmVehicle:
        return ZtmVehicle(
            location=Location(
                longitude=float(record["Lon"]), latitude=float(record["Lon"])
            ),
            lines=record["Lines"],
            vehicle_number=record["VehicleNumber"],
            time=record["Time"],
            brigade=record["Brigade"],
            type=vehicle_type,
        )

    def __get_vehicle_location(
        self, vehicle_type: int, line: int = None
    ) -> List[ZtmVehicle]:
        url = "https://api.um.warszawa.pl/api/action/busestrams_get/"

        query_params: Dict[str, Union[str, int, None]] = {
            "resource_id": "f2e5503e927d-4ad3-9500-4ab9e55deb59",
            "type": vehicle_type,
            "apikey": self.apikey,
            "line": line,
        }

        response = requests.get(url=url, params=query_params).json()
        if response.get("error"):
            raise Exception(response["error"])

        vehicles = []
        for record in response["result"]:
            vehicles.append(
                self.__parse_vehicle_location_data(
                    record=record, vehicle_type=vehicle_type
                )
            )
        return vehicles

    def get_buses_location(self, line: int = None) -> List[ZtmVehicle]:
        return self.__get_vehicle_location(line=line, vehicle_type=1)

    def get_trams_location(self, line: int = None) -> List[ZtmVehicle]:
        return self.__get_vehicle_location(line=line, vehicle_type=2)
