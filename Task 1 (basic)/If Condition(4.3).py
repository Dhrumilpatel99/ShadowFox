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

# Ask the user to enter two cities
city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

# Check if both cities are in the dictionary and if they belong to the same country
if city1 in cities_countries and city2 in cities_countries:
    country1 = cities_countries[city1]
    country2 = cities_countries[city2]
    if country1 == country2:
        print("Both cities are in", country1)
    else:
        print("They don't belong to the same country")
else:
    print("One or both cities are not found in the provided list.")
