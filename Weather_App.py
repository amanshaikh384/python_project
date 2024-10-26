from bs4 import BeautifulSoup
import requests
import tkinter as tk
from tkinter import messagebox

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def get_weather(city):
    city = city.replace(" ", "+")
    res = requests.get(
        f'https://www.google.com/search?q={city}+weather', headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    location_elem = soup.select('.BNeawe.iBp4i.AP7Wnd')[0]
    location = location_elem.text.strip()

    weather_elem = soup.select('.BNeawe.tAd8D.AP7Wnd')[0]
    weather_info = weather_elem.text.strip()

    temperature_elem = soup.select('.BNeawe.iBp4i.AP7Wnd')[1]
    temperature = temperature_elem.text.strip()

    messagebox.showinfo("Weather Information",
                        f"City: {location}\nWeather: {weather_info}\nTemperature: {temperature}")

def show_weather():
    city = city_entry.get()
    if city:
        get_weather(city)
        city_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a city.")

# GUI
root = tk.Tk()
root.title("Weather App")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label = tk.Label(frame, text="Enter a city:")
label.pack()

city_entry = tk.Entry(frame)
city_entry.pack()

button = tk.Button(frame, text="Get Weather", command=show_weather)
button.pack()

root.mainloop()