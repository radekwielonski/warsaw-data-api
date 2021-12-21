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

ztm = warsaw_data_api.client('ztm', apikey='your_api_key')
buses = ztm.get_buses_location()

for bus in buses:
    print(bus)
```

We can do the same for trams, as a parameter we can set number of tram line

```python
import warsaw_data_api

ztm = warsaw_data_api.client('ztm', apikey='your_api_key')
trams = ztm.get_trams_location(line=17)

for tram in trams:
    print(tram)
```

### Get buses schedule:

We can fetch schedule by using bus stop id:

```python
import warsaw_data_api

ztm = warsaw_data_api.client('ztm', apikey='your_api_key')
schedule = ztm.get_bus_stop_schedule_by_id(7009, "01", "182")
print(schedule)
```

or we can fetch it by using bus stop name:

```python
import warsaw_data_api

ztm = warsaw_data_api.client('ztm', apikey='your_api_key')
schedule = ztm.get_bus_stop_schedule_by_name("Marszałkowska", "01", "182")
print(schedule)

```

### Passing API Key

We can pass API Key in two different ways:

1. Pass API Key to client function as a parameter `ztm = warsaw_data_api.client('ztm', apikey='your_api_key')`
2. Create environment variable called `WARSAW_DATA_API_KEY`

## Running tests:

1. Go to root directory
2. Install packages:

```bash
pip install -r requirements.txt
```

3. Run tests:

```bash
python -m unittest
```
