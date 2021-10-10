from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utilities.comparatorLogic import comparator, tempdifference
from utilities.testFunctions import getTemponUI, getTemponAPI, closeBrowser


def launchbrowser(browserType):
    if browserType == 'chrome':
        option1 = Options()
        option1.add_argument("--disable-notifications")
        wdriver = webdriver.Chrome(r"/Users/rahul/IdeaProjects/SelTest/Browsers/chromedriver", chrome_options=option1)
        return wdriver
    if browserType == 'firefox':
        wdriver = webdriver.Firefox()
        return wdriver


apiKey = "7fe67bf08c80ded756e598d6f8fedaea"
city = "Chandigarh, Chandigarh IN"
weatherFormat = "metric"
url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + apiKey + "&units=" + weatherFormat
tempDifferenceAllowed = 2
print(url)


driver = launchbrowser('chrome')
uiTemp = getTemponUI(driver)
closeBrowser(driver)
apiTemp = getTemponAPI(url)
tempDiff = tempdifference(int(uiTemp), apiTemp)
print(tempDiff)
assert comparator(tempDiff, tempDifferenceAllowed), "Temperature difference more then permitable limit"
print('Test completed')
