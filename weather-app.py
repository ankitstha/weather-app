import requests
import tkinter as tk
from tkinter import messagebox
from ttkthemes import ThemedTk

def get_weather(api_key, city):
    base_url = "http://dataservice.accuweather.com/currentconditions/v1/"
    params = {"apikey": api_key, "language": "en-us"}

    try:
        location_url = f"http://dataservice.accuweather.com/locations/v1/cities/search"
        location_params = {"apikey": api_key, "q": city, "language": "en-us"}
        location_response = requests.get(location_url, params=location_params)
        location_data = location_response.json()

        if location_data:
            location_key = location_data[0]["Key"]
            response = requests.get(f"{base_url}{location_key}", params=params)
            weather_data = response.json()

            temperature = weather_data[0]["Temperature"]["Metric"]["Value"]
            description = weather_data[0]["WeatherText"]

            result = f"Temperature: {temperature}°C\nDescription: {description}"
            return result
        else:
            return "City not found"

    except requests.ConnectionError:
        return "Connection error. Please check your internet connection."

def get_weather_button_clicked():
    city_name = city_entry.get()

    if city_name:
        weather_result = get_weather(api_key, city_name)
        messagebox.showinfo("Weather Information", weather_result)
    else:
        messagebox.showwarning("Input Error", "Please enter a city name.")

# Replace 'YOUR_API_KEY' with your actual AccuWeather API key
api_key = 'OsxcSNXMA04JGGd6WpkYxJujK5A8XATK'

# GUI setup using ThemedTk
app = ThemedTk(theme="arc")  
app.title("Weather App (AccuWeather)")

# Widgets
city_label = tk.Label(app, text="Enter City:")
city_label.pack(pady=10)

city_entry = tk.Entry(app, width=30)
city_entry.pack(pady=10)

get_weather_button = tk.Button(app, text="Get Weather", command=get_weather_button_clicked)
get_weather_button.pack(pady=20)

# Run the app
app.mainloop()
