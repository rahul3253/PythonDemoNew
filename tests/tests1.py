from utilities import testFunctions, launchBrowser, comparatorLogic

apiKey = "7fe67bf08c80ded756e598d6f8fedaea"
city = "Chandigarh, Chandigarh IN"
weatherFormat = "metric"
url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + apiKey + "&units=" + weatherFormat
tempDifferenceAllowed = 2
print(url)