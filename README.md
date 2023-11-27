# Pythonic way to use Warsaw data API

This package allow to fetch data from API provided by "UM Warszawa" - https://api.um.warszawa.pl/

## Current features

- Fetch ZTM buses and trams real-time location
- Fetch Schedule for bus stop for certain bus line

## Getting Started

## Installation

```
pip install warsaw-data-api
```

## Using ZTM module

### Get buses/trams locations:

We can fetch all location data for buses:

```python
import warsaw_data_api

ztm = warsaw_data_api.ztm(apikey='your_api_key') # you can get API KEY on the https://api.um.warszawa.pl/ after you register
buses = ztm.get_buses_location()

for bus in buses:
    print(bus)
```

We can do the same for trams, as a parameter we can set number of tram line

```python
import warsaw_data_api

ztm = warsaw_data_api.ztm(apikey='your_api_key')
trams = ztm.get_trams_location(line=17)

for tram in trams:
    print(tram)
```

### Get buses schedule:

We can fetch schedule by using bus stop id:

```python
import warsaw_data_api

ztm = warsaw_data_api.ztm(apikey='your_api_key')
schedule = ztm.get_bus_stop_schedule_by_id("7009", "01", "182")
print(schedule.rides)
```

or we can fetch it by using bus stop name:

```python
import warsaw_data_api

ztm = warsaw_data_api.ztm(apikey='your_api_key')
schedule = ztm.get_bus_stop_schedule_by_name("Marszałkowska", "01", "182")
print(schedule.rides)

```

if you would like to retrieve all buses for the bus stop you can use this:

```python
import warsaw_data_api

ztm = warsaw_data_api.ztm(apikey='your_api_key')
lines = ztm.get_lines_for_bus_stop_id("7009", "01")
print(lines)
```

### Passing API Key

We can pass API Key in two different ways:

1. Pass API Key to factory function (`ztm()` in this case) as a parameter `ztm = warsaw_data_api.ztm(apikey='your_api_key')`
2. Create environment variable called `WARSAW_DATA_API_KEY`
