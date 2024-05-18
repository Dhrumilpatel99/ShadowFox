# Dictionary of cities and their corresponding countries
cities_countries = {
    "Sydney": "Australia",
    "Melbourne": "Australia",
    "Brisbane": "Australia",
    "Perth": "Australia",
    "Dubai": "UAE",
    "Abu Dhabi": "UAE",
    "Sharjah": "UAE",
    "Ajman": "UAE",
    "Mumbai": "India",
    "Bangalore": "India",
    "Chennai": "India",
    "Delhi": "India"
}

# Ask the client to enter a city name
city = input("Enter a city name: ")

# Check if the city is in the dictionary
if city in cities_countries:
    country = cities_countries[city]
    print(city, "is in", country)
else:
    print("City not found in the provided list.")
