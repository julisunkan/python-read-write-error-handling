import requests

# Function to get weather data from the API
def get_weather(city_name, api_key):
    # API URL
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Complete URL to send the request
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"
    
    # Sending a GET request to the API
    response = requests.get(complete_url)
    
    # Convert the response to a JSON format
    data = response.json()
    
    # Check if the request was successful
    if data["cod"] == "404":
        print("Invalid city name. Please check the spelling or try another city.")
    else:
        # Extracting data from the response
        main_data = data["main"]
        weather_data = data["weather"][0]
        
        # Displaying the results
        print(f"\nWeather Info for {city_name.capitalize()}:")
        print(f"Temperature: {main_data['temp']}°C")
        print(f"Pressure: {main_data['pressure']} hPa")
        print(f"Humidity: {main_data['humidity']} %")
        print(f"Weather: {weather_data['description'].capitalize()}")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
        print(f"Cloudiness: {data['clouds']['all']}%")

# Main function to run the app
def main():
    # Your OpenWeatherMap API key
    api_key = "your_api_key_here"  # Replace with your actual API key
    
    # Ask the user for the city name
    city_name = input("Enter the city name: ")
    
    # Get weather data for the city
    get_weather(city_name, api_key)

# Running the program
if __name__ == "__main__":
    main()
