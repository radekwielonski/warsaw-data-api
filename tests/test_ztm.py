from datetime import datetime
import unittest
import requests_mock

import warsaw_data_api
from warsaw_data_api.ztm.models import (
    Location,
    ZtmVehicle,
    ZtmSchedule,
    ZtmRide,
)


class TestZtmLocation(unittest.TestCase):
    def test_get_bus_stop_schedule_by_id(self) -> None:
        ztm = warsaw_data_api.ztm("apikey_for_test")
        url = "http://test.com/api/1/schedule"
        ztm.schedule_endpoint = url
        with requests_mock.Mocker() as m:
            m.register_uri(
                "GET",
                url,
                json={
                    "result": [
                        {
                            "values": [
                                {"value": "null", "key": "symbol_2"},
                                {"value": "null", "key": "symbol_1"},
                                {"value": "7", "key": "brygada"},
                                {"value": "Witolin", "key": "kierunek"},
                                {"value": "TP-OST", "key": "trasa"},
                                {"value": "04:51:00", "key": "czas"},
                            ]
                        },
                        {
                            "values": [
                                {"value": "null", "key": "symbol_2"},
                                {"value": "null", "key": "symbol_1"},
                                {"value": "011", "key": "brygada"},
                                {"value": "Witolin", "key": "kierunek"},
                                {"value": "TP-OST", "key": "trasa"},
                                {"value": "05:11:00", "key": "czas"},
                            ]
                        },
                        {
                            "values": [
                                {"value": "null", "key": "symbol_2"},
                                {"value": "null", "key": "symbol_1"},
                                {"value": "1", "key": "brygada"},
                                {"value": "Witolin", "key": "kierunek"},
                                {"value": "TP-OST", "key": "trasa"},
                                {"value": "05:31:00", "key": "czas"},
                            ]
                        },
                    ]
                },
            )
            result = ztm.get_bus_stop_schedule_by_id("7009", "01", "182")
            rides = [
                ZtmRide(
                    brigade="7",
                    direction="Witolin",
                    route="TP-OST",
                    time="04:51:00",
                ),
                ZtmRide(
                    brigade="011",
                    direction="Witolin",
                    route="TP-OST",
                    time="05:11:00",
                ),
                ZtmRide(
                    brigade="1",
                    direction="Witolin",
                    route="TP-OST",
                    time="05:31:00",
                ),
            ]
            expected_result = ZtmSchedule(
                line="182", bus_stop_id=7009, bus_stop_nr="01", rides=rides
            )

            self.assertEqual(result, expected_result)


class TestZtmSchedule(unittest.TestCase):
    def test_get_buses_location(self) -> None:
        ztm = warsaw_data_api.ztm("apikey_for_test")
        url = "http://test.com/api/1/location"
        ztm.location_endpoint = url
        with requests_mock.Mocker() as m:
            m.register_uri(
                "GET",
                url,
                json={
                    "result": [
                        {
                            "Lines": "130",
                            "Lon": 21.084736,
                            "VehicleNumber": "1000",
                            "Time": "2021-12-20 16:47:03",
                            "Lat": 52.1675208,
                            "Brigade": "1",
                        },
                        {
                            "Lines": "305",
                            "Lon": 21.1429426,
                            "VehicleNumber": "1001",
                            "Time": "2021-12-20 16:47:01",
                            "Lat": 52.1986071,
                            "Brigade": "1",
                        },
                        {
                            "Lines": "213",
                            "Lon": 21.1560425,
                            "VehicleNumber": "1002",
                            "Time": "2021-12-20 16:47:07",
                            "Lat": 52.2140021,
                            "Brigade": "1",
                        },
                    ]
                },
            )
            expected_result = [
                ZtmVehicle(
                    Location(21.084736, 52.1675208),
                    "130",
                    "1000",
                    datetime(2021, 12, 20, 16, 47, 3),
                    "1",
                    1,
                ),
                ZtmVehicle(
                    Location(21.1429426, 52.1986071),
                    "305",
                    "1001",
                    datetime(2021, 12, 20, 16, 47, 1),
                    "1",
                    1,
                ),
                ZtmVehicle(
                    Location(21.1560425, 52.2140021),
                    "213",
                    "1002",
                    datetime(2021, 12, 20, 16, 47, 7),
                    "1",
                    1,
                ),
            ]
            result = ztm.get_buses_location()
            self.assertEqual(result, expected_result)

    def test_get_trams_location(self) -> None:
        self.maxDiff = None
        ztm = warsaw_data_api.ztm("apikey_for_test")
        url = "http://test.com/api/1/location"
        ztm.location_endpoint = url
        with requests_mock.Mocker() as m:
            m.register_uri(
                "GET",
                url,
                json={
                    "result": [
                        {
                            "Lines": "35",
                            "Lon": 21.024065,
                            "VehicleNumber": "1123+1122",
                            "Time": "2021-12-21 10:19:21",
                            "Lat": 52.19707,
                            "Brigade": "14",
                        },
                        {
                            "Lines": "22",
                            "Lon": 21.08282,
                            "VehicleNumber": "1237+1238",
                            "Time": "2021-12-21 10:19:19",
                            "Lat": 52.245193,
                            "Brigade": "10",
                        },
                        {
                            "Lines": "22",
                            "Lon": 21.04736,
                            "VehicleNumber": "1239+1240",
                            "Time": "2021-12-21 10:19:20",
                            "Lat": 52.24682,
                            "Brigade": "1",
                        },
                    ]
                },
            )
            expected_result = [
                ZtmVehicle(
                    Location(21.024065, 52.19707),
                    "35",
                    "1123+1122",
                    datetime(2021, 12, 21, 10, 19, 21),
                    "14",
                    2,
                ),
                ZtmVehicle(
                    Location(21.08282, 52.245193),
                    "22",
                    "1237+1238",
                    datetime(2021, 12, 21, 10, 19, 19),
                    "10",
                    2,
                ),
                ZtmVehicle(
                    Location(21.04736, 52.24682),
                    "22",
                    "1239+1240",
                    datetime(2021, 12, 21, 10, 19, 20),
                    "1",
                    2,
                ),
            ]
            result = ztm.get_trams_location()
            self.assertEqual(result, expected_result)
