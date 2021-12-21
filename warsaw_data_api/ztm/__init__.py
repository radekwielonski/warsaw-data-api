from .models import ZtmSchedule, ZtmRide, ZtmVehicle, Location
from datetime import datetime
from typing import List, Dict, Union
import requests

from warsaw_data_api.session import Session


class ZtmSession(Session):
    location_endpoint: str
    schedule_endpoint: str

    def __init__(self, apikey: str = None) -> None:
        super().__init__(apikey=apikey)
        self.location_endpoint = (
            "https://api.um.warszawa.pl/api/action/busestrams_get/"
        )
        self.schedule_endpoint = (
            "https://api.um.warszawa.pl/api/action/dbtimetable_get"
        )

    def __parse_vehicle_location_data(
        self, record, vehicle_type: int
    ) -> ZtmVehicle:
        return ZtmVehicle(
            location=Location(
                longitude=float(record["Lon"]), latitude=float(record["Lat"])
            ),
            line=record["Lines"],
            vehicle_number=record["VehicleNumber"],
            time=datetime.strptime(record["Time"], "%Y-%m-%d %H:%M:%S"),
            brigade=int(record["Brigade"]),
            type=vehicle_type,
        )

    def __parse_multiple_vehicle_location_data(
        self, records, vehicle_type: int
    ) -> List[ZtmVehicle]:
        vehicles = []
        for record in records:
            vehicles.append(
                self.__parse_vehicle_location_data(
                    record=record, vehicle_type=vehicle_type
                )
            )

        return vehicles

    def __get_data_from_ztm(self, url, query_params):
        r = requests.get(url=url, params=query_params)
        if r.status_code == requests.codes.ok:
            response = r.json()
        else:
            raise Exception(
                f"Error fetching data from {url}, status: {r.status_code}"
            )

        if response.get("error"):
            raise Exception(response["error"])

        return response["result"]

    def __get_vehicle_location(
        self, vehicle_type: int, line: str = None
    ) -> List[ZtmVehicle]:
        query_params: Dict[str, Union[str, int, None]] = {
            "resource_id": "f2e5503e927d-4ad3-9500-4ab9e55deb59",
            "type": vehicle_type,
            "apikey": self.apikey,
            "line": line,
        }
        response = self.__get_data_from_ztm(
            self.location_endpoint, query_params
        )
        vehicles = self.__parse_multiple_vehicle_location_data(
            response, vehicle_type
        )

        return vehicles

    def get_buses_location(self, line: str = None) -> List[ZtmVehicle]:
        return self.__get_vehicle_location(line=line, vehicle_type=1)

    def get_trams_location(self, line: str = None) -> List[ZtmVehicle]:
        return self.__get_vehicle_location(line=line, vehicle_type=2)

    def __parse_schedule_data(self, schedule) -> ZtmRide:
        return ZtmRide(
            int(schedule["brygada"]),
            schedule["kierunek"],
            schedule["trasa"],
            schedule["czas"],
        )

    def __parse_multiple_schedule_data(self, schedules) -> List[ZtmRide]:
        rides = []
        for record in schedules:
            clean_record = convert_list_to_dict(record["values"])
            rides.append(self.__parse_schedule_data(clean_record))

        return rides

    def get_bus_stop_schedule_by_id(
        self, bus_stop_id: int, bus_stop_nr: str, line: str
    ) -> ZtmSchedule:
        query_params: Dict[str, Union[str, int, None]] = {
            "id": "e923fa0e-d96c-43f9-ae6e-60518c9f3238",
            "apikey": self.apikey,
            "busstopId": bus_stop_id,
            "busstopNr": bus_stop_nr,
            "line": line,
        }
        response = self.__get_data_from_ztm(
            self.schedule_endpoint, query_params
        )
        rides = self.__parse_multiple_schedule_data(response)

        ztm_schedule = ZtmSchedule(line, bus_stop_id, bus_stop_nr, rides)

        return ztm_schedule

    def get_bus_stop_schedule_by_name(
        self, bus_stop_name: str, bus_stop_nr: str, line: str
    ) -> ZtmSchedule:
        query_params: Dict[str, Union[str, int, None]] = {
            "id": "b27f4c17-5c50-4a5b-89dd-236b282bc499",
            "apikey": self.apikey,
            "name": bus_stop_name,
        }
        response = self.__get_data_from_ztm(
            self.schedule_endpoint, query_params
        )
        clean_response = convert_list_to_dict(response[0]["values"])
        return self.get_bus_stop_schedule_by_id(
            clean_response["zespol"], bus_stop_nr, line
        )


# utils
def convert_list_to_dict(input_list):
    output_dict = {}
    for x in input_list:
        output_dict[x["key"]] = x["value"]

    return output_dict
