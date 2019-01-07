import json
import urllib.request
import datetime
import requests
import time

# time stamp: init return issue as of 01/06/18.
# time stamp: runs into exceptions as of 01/17/18
# time stamp: application almost ready
# time stamp: version 1.1 time returns None on all datetimes.



units = 'imperial'

def time_converter(time):
    converted_time = datetime.datetime.fromtimestamp(int(time)).strftime('%Y-%m-%d %H:%M %S')
    print(converted_time)


def site_build(cityname):
	apikey = 'b860b36b88dbccda9c80a6d0b585d70d'
	units = 'imperial'
	sample_url = 'http://api.openweathermap.org/data/2.5/weather?q='
	complete_url = sample_url + cityname + '&mode=json&units=' + units + '&appid=' + apikey
	print(complete_url)
	return complete_url


def fetch_data(complete_url):
	open_site = urllib.request.urlopen(complete_url)
	site_data = open_site.read().decode('utf-8')
	json_data = json.loads(site_data)
	open_site.close()
	return json_data

def data_organizer(raw_api_dict):               # organizes the data using a key and a value (dictionary)

	data = dict(
	    city=raw_api_dict.get('name'),
	    country=raw_api_dict.get('sys').get('country'),
	    temp=raw_api_dict.get('main').get('temp'),
	    temp_max=raw_api_dict.get('main').get('temp_max'),
	    temp_min=raw_api_dict.get('main').get('temp_min'),
	    humidity=raw_api_dict.get('main').get('humidity'),
	    pressure=raw_api_dict.get('main').get('pressure'),
	    description = raw_api_dict['weather'][0]['description'],  # just added.
	    sky=raw_api_dict['weather'][0]['main'],
	    sunrise=time_converter(raw_api_dict.get('sys').get('sunrise')),
	    sunset=time_converter(raw_api_dict.get('sys').get('sunset')),
	    wind=raw_api_dict.get('wind').get('speed'),
	    wind_deg=raw_api_dict.get('deg'),
	    dt=time_converter(raw_api_dict.get("dt")),
	    cloudiness=raw_api_dict.get('clouds').get('all')
	    )
	return data

def output(data):
	celcius_symbol = '\xb0' + 'C'
	farenheit_symbol = '\xb0' + 'F'
	pressure_unit = 'hPa'
	print('---------------------------------------')
	print('Weather in {}, {}:'.format(data['city'], data['country']))
	temperature = (data['temp'], farenheit_symbol)
	print('Max: {}{}, Min: {}{}'.format(data['temp_max'], farenheit_symbol ,data['temp_min'], farenheit_symbol))
	print('Sky Condition: {}'.format(data['sky']))
	print('Wind Speed: {} miles/hr, Degree: {}'.format(data['wind'], data['wind_deg']))
	print('Humidity: {}%'.format(data['humidity']))
	print('Cloudy: {}%'.format(data['cloudiness']))
	print('Pressure: {} {}'.format(data['pressure'], pressure_unit))
	print('Sunrise at: {}'.format(data['sunrise']))
	print('Sunset at: {}'.format(data['sunset']))
	print('')

	if data["dt"] == None:
		print('Last Updated: Not available')
	else:

		print('Recent Update: {}'.format(data['dt']))
	print('Outdoors Look like: {}'.format(data['description']))
	print('---------------------------------------')


def main():

	try:

            with open('weather_data.json', 'w') as outfile:
                json.dump(data_organizer(fetch_data(site_build('New York'))), outfile, indent=4)

	except urllib.request.URLError:
		print("We're unable to connect to the Internet, please check your Internet Connection and try again")

	except NameError:
		print('Invalid Cityname')


main()
