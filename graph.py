import requests
import matplotlib.pyplot as plt
from datetime import datetime

# Get the weather data for a specific city
def get_weather_data(city, api_key):
    url = f'http://api.openweathermap.org/data/2.5/forecast/daily?q={city}&cnt=7&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    
    if response.status_code != 200:
        print("Error fetching data:", data.get("message"))
        return None
    
    return data['list']

# Process the weather data to extract dates, temperatures, and weather descriptions
def process_weather_data(weather_data):
    dates = []
    temperatures = []
    descriptions = []
    
    for day in weather_data:
        date = datetime.utcfromtimestamp(day['dt']).strftime('%Y-%m-%d')
        temp = day['temp']['day']
        description = day['weather'][0]['description']
        
        dates.append(date)
        temperatures.append(temp)
        descriptions.append(description)
    
    return dates, temperatures, descriptions

# Plotting the weather data
def plot_weather_data(dates, temperatures, descriptions):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(dates, temperatures, marker='o', color='b', label='Temperature (°C)')
    ax.set_title('Weekly Weather Forecast', fontsize=16)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Temperature (°C)', fontsize=12)
    
    # Rotate dates for better readability
    plt.xticks(rotation=45)
    
    # Add a text label for the weather description
    for i, txt in enumerate(descriptions):
        ax.annotate(txt, (dates[i], temperatures[i]), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=8)
    
    # Show the grid and plot
    ax.grid(True)
    plt.tight_layout()
    plt.legend()
    plt.show()

# Main function to ask user for city and fetch weather forecast
def main():
    city = input("Enter the city name: ")
    api_key = "c21ae2fe94b797f685708910c40b98ef"  # Replace with your OpenWeatherMap API key
    
    # Fetch and process the data
    weather_data = get_weather_data(city, api_key)
    
    if weather_data:
        dates, temperatures, descriptions = process_weather_data(weather_data)
        
        # Plot the data
        plot_weather_data(dates, temperatures, descriptions)

if __name__ == "__main__":
    main()
