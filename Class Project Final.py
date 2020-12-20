import requests

#Connect to web and get weather data for display
def WEATHER_REPORT(query):
    
    
    api_key = "19ed4e48a38b314f4b8b7160f9806731"

    try:
        WEATHER_json = requests.get("http://api.openweathermap.org/data/2.5/weather?" + query + ",us&appid=" + api_key + "&units=metric").json()

        print("Weather: " + WEATHER_json["weather"]["description"])
        print("Temperature: " + str(WEATHER_json["main"]["temp"]) + " celsius")
        print("Humidity: " + str(WEATHER_json["main"]["humidity"]))
        print("Visibility: " + str(WEATHER_json["visibility"]))
        print("Wind: " + str(WEATHER_json["wind"]["speed"]) + " at " + str(weather_json["wind"]["deg"]) + " degrees")
    except requests.exceptions.HTTPError as err:
        print("Connection Error:", err)
   


#Find out weather by zip code
    
def WEATHER_BY_ZIP():
    
    try:
        zip_code = int(input("Enter zip code: "))
        WEATHER_REPORT("zip=" + zip_code)
    except:
        print("Input Error: Zip code is required and should be numeric.")


#Find out  weather by city
    
def WEATHER_BY_CITY():

    city = input("Enter US city: ").strip()

    if city == "":
        print("Input Error: A city name is required.")
        return

    WEATHER_REPORT("q=" + city)


#Main function of the program
   
def main():
  
    while True:
        print("Menu")
        print("[1] Get weather by Zip Code")
        print("[2] Get weather by City Name")
        print("[3] Exit")
        option = input("Option: ")

        if option == "1":
            WEATHER_BY_ZIP()
        elif option == "2":
            WEATHER_BY_CITY()
        elif option == "3":
            break
        else:
            print("Option Error: Invalid entry")

        print()


main()
