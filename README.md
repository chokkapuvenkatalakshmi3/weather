
A text entry (city_entry) to input the city name.
A button (weather_button) to trigger the display of the weather forecast.
A frame (frame) to contain the weather graph.
Weather Forecast Data: The program uses mock data for weather forecasts:

days: A list representing the days of the week.
temperatures: A list of mock temperature values (in Celsius) for the 7-day forecast.
humidity: A list of mock humidity values (as percentages) for the same 7-day period.
Plotting the Graph:

Matplotlib is used to plot a graph with temperature and humidity.
The program uses two y-axes:
The first axis (ax1) represents temperature in Celsius.
The second axis (ax2) represents humidity as a percentage.
The graph is displayed using the FigureCanvasTkAgg widget, which embeds the matplotlib plot inside the tkinter window.
User Interaction:

The user enters a city name in the input field.
Clicking the "Get Weather Forecast" button fetches the mock weather data and displays it as a graph in the window.
Key Features:
Interactivity: The user can enter any city name and click the button to view the weather forecast for that city.
Graphical Representation: Both temperature and humidity are displayed on the same graph using two different y-axes.
Easy to Extend: You can extend this program to fetch real-time data by using APIs like OpenWeatherMap.
Example Output:
A simple graph displaying temperature on one y-axis (in red) and humidity on another y-axis (in blue) for the next 7 days, with day names (Mon-Sun) along the x-axis.
Future Enhancements:
Real-Time Data: Connect to a weather API to fetch actual weather data.
Advanced Features: Add more weather parameters (e.g., wind speed, precipitation) and display them in different graphs.
User-friendly Interface: Improve the GUI with additional styling or include weather icons to represent conditions visually (e.g., sunny, cloudy).
This program serves as a basic weather forecast visualizer that can be easily expanded with real-time data.




