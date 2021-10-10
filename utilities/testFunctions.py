from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import requests


def getTemponUI(driver):
    driver.get("https://www.accuweather.com/")
    searchCity = driver.find_element_by_class_name("search-input")
    searchCity.send_keys("Chandigarh, Chandigarh IN")
    searchCity.send_keys(Keys.RETURN)
    element = WebDriverWait(driver, 10).until(
        lambda x: x.find_element_by_class_name("after-temp"))
    temp = (driver.find_element_by_class_name("temp").text).split('°')[0]
    return temp


def getTemponAPI(url):
    resp = requests.get(url)
    assert resp.status_code == 200
    resp_body = resp.json()
    apiTemp = int(resp_body['main']['temp'])
    return apiTemp


def closeBrowser(driver):
    driver.close()
