# Pythonic way to use Warsaw data API
This package allow to fetch data from API provided by "UM Warszawa" - https://api.um.warszawa.pl/

## Quick start

### Instalation

TODO

### Using ZTM module 

We can fetch all location data for buses:

```
import warsaw_data_api

ztm = warsaw_data_api.client('ztm', apikey='your_api_key')
buses = ztm.get_buses_location()

for bus in buses:
    print(bus)
```

We can do the same for trams, as a parameter we can set number of tram line 
```
import warsaw_data_api

ztm = warsaw_data_api.client('ztm', apikey='your_api_key')
trams = ztm.get_trams_location(lines=17)

for tram in trams:
    print(tram)
```