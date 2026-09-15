# Weather Forecast

A small desktop weather app built with Python and Tkinter. Enter a city to see its current temperature, conditions, and a seven-day forecast.

Forecast data comes from [Open-Meteo](https://open-meteo.com/), so no API key is required. An internet connection is needed when searching for a forecast.

## Run

From this folder:

```powershell
python weather_app.py
```

## Test

The tests use mocked API responses and do not need an internet connection:

```powershell
python -m unittest -v
```

The app uses only Python's standard library, including Tkinter, so no `pip install` step is required.