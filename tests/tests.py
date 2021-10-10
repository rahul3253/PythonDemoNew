from utilities import launchBrowser
from utilities.comparatorLogic import comparator, tempdifference
# from utilities.launchBrowser import launchbrowser
from utilities.testFunctions import getTemponUI, getTemponAPI, closeBrowser
import utilities.launchBrowser

apiKey = "7fe67bf08c80ded756e598d6f8fedaea"
city = "Chandigarh, Chandigarh IN"
weatherFormat = "metric"
url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + apiKey + "&units=" + weatherFormat
tempDifferenceAllowed = 2
print(url)


# def compareTempOnChrome():
# def __init__(self):
#     launchbrowser('chrome')

driver = launchBrowser.cdriver
print(driver.title)
# driver = driverLaunch.launchbrowser('chrome')
uiTemp = getTemponUI(driver)
closeBrowser(driver)
apiTemp = getTemponAPI(url)
tempDiff = tempdifference(int(uiTemp), apiTemp)
print(tempDiff)
assert comparator(tempDiff, tempDifferenceAllowed), "Temperature difference more then permitable limit"
print('Test completed')


# compareTempOnChrome()
