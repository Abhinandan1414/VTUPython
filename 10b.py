# import required modules
import requests, json

api_key = "360396a690bbdadea6dafcdfecd8df66"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

#https://api.openweathermap.org/data/2.5/weather?q=London&appid=360396a690bbdadea6dafcdfecd8df66


entered_city = input("Enter city name : ")

complete_url = base_url + "q=" + entered_city +"&appid=" + api_key

response = requests.get(complete_url)

x = response.json()

#print(x)


if x["cod"] != "404":

    temperature = x["main"]["temp"]
    pressure = x["main"]["pressure"]
    humidity = x["main"]["humidity"]
    weather = x["weather"]	
    weather_description = weather[0]["description"]
    print('\033[1m' + "Weather description is: "+str(weather_description) + '\033[0m')
    print("Additional Weather description is follows:\n")
    print("\n\n Temparature is = " +
					str(temperature) +
		"\n Atmospheric pressure  = " +
					str(pressure) +
		"\n Humidity  = " +
					str(humidity)) 
else:
	print(" Please enter valid city name ")

  