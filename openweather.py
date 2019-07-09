This is to find the Temperature of a city in celsius/fahrenheit by using open weather api
open pycharm in your computer
create a project and add new python file eg.weather.py
from settings  import pyowm from project interpreter
start writing the following code in new python file (eg.weather.py)
------------------------******---------------------------
import pyowm

owm=pyowm.OWM('d559feca01e166e5db6eb2a513ac8d00')       #------->This is API from open weathermap

location= owm.weather_at_place('hyderabad')             #------->This the Name of the city e.g:Hyderabad
Weather= location.get_weather()

#location= owm.weather_at_zip_code('500004','IN')       #---->This is to find using ZIP-CODE
#Weather= location.get_weather()

tempC = Weather.get_temperature('celsius')              #------->This is temperature in Celsius
print('The temperature in celsius is',tempC)

tempF = Weather.get_temperature('fahrenheit')           #------->This is temperature in Fahrenheit
print('The temperature in Fahrenheit is',tempF)

humidity= Weather.get_humidity()                        #------->This is to find humidity of a city
print('Humidity is',humidity)

status= Weather.get_status()                            #------->This is to find weather status of a city
print('The weather status is',status)
------------------------------------------********----------------------
After writing the code, go to terminals and RUN the code to get output response
for the above code the output response is shown below

----------------OUTPUT at Terminals--------------
The temperature in celsius is {'temp': 32.2, 'temp_max': 34.0, 'temp_min': 31.0, 'temp_kf': None}
The temperature in Fahrenheit is {'temp': 89.96, 'temp_max': 93.2, 'temp_min': 87.8, 'temp_kf': None}
Humidity is 56
The weather status is Haze
