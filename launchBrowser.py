from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import requests
from comparatorLogic import comparator, tempdifference
import json

option1 = Options()

### option to disable notification on website
option1.add_argument("--disable-notifications")

driver = webdriver.Chrome(r"/Users/rahul/IdeaProjects/SelTest/Browsers/chromedriver", chrome_options=option1)

driver.get("https://www.accuweather.com/")

searchCity = driver.find_element_by_class_name("search-input")

searchCity.send_keys("Chandigarh, Chandigarh IN")

searchCity.send_keys(Keys.RETURN)

element = WebDriverWait(driver, 10).until(
    lambda x: x.find_element_by_class_name("after-temp"))

temp = (driver.find_element_by_class_name("temp").text).split('°')[0]

driver.close()


### API Test
url = "http://api.openweathermap.org/data/2.5/weather?q=Chandigarh, Chandigarh IN &appid=7fe67bf08c80ded756e598d6f8fedaea&units=metric"

resp = requests.get(url)

# Validate response headers and body contents, e.g. status code.
assert resp.status_code == 200
resp_body = resp.json()

# print response full body as text
apiTemp = int(resp_body['main']['temp'])


## Calculate temp difference
tempDiff = tempdifference(int(temp), apiTemp)

assert (comparator(tempDiff))

print('Test completed')