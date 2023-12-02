# AccuWeather Python Weather App

This is a simple Python weather app that fetches current weather information using the AccuWeather API. It features a graphical user interface (GUI) built with Tkinter and ttkthemes for a modern look.

## Features

- Fetches current temperature and weather description for a specified city.
- Uses AccuWeather API to get real-time weather data.
- Provides a visually appealing and user-friendly interface.

## Prerequisites

Before running the application, ensure you have the following:

- Python 3.x installed.
- The `requests` library installed (`pip install requests`).
- The `ttkthemes` library installed (`pip install ttkthemes`).

## Getting Started

1. Obtain an API key from [AccuWeather](https://developer.accuweather.com/).
2. Replace `"YOUR_API_KEY"` in the script with your actual API key.

```python
# Replace 'YOUR_API_KEY' with your actual AccuWeather API key
api_key = "YOUR_API_KEY"
```
3. Run the script:
````bash
python weather_app.py
````
4. Enter a city name in the GUI and click "Get Weather" to see the current temperature and weather description.

## Themes
The app uses themes from `ttkthemes`. You can experiment with different themes by changing the `theme` parameter when creating the `ThemedTk` widget.

````python
app = ThemedTk(theme="arc")  # You can experiment with different themes like 'radiance', 'scidblue', etc.
````
