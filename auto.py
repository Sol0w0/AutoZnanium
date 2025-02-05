import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
       
options = Options()
options.add_argument("--headless=new") #скрывает окно браузера
options.add_argument("--log-level=3")  
with webdriver.Chrome(options=options) as driver:
    driver.get("https://znanium.ru/site/login")
    print("сайт")
    driver.find_element(By.ID, "loginform-username").send_keys("***") #почта
    driver.find_element(By.ID, "loginform-password").send_keys("***") #пароль
    driver.find_element(By.ID, "loginform-password").send_keys(Keys.RETURN)
    print("вошел в акк")
    time.sleep(1)
    att = 0
    while True:
        driver.get("https://znanium.ru/read?id=******") #книга
        att += 1
        print(att, " заходов")
        time.sleep(2100)
        driver.get("https://znanium.ru")
        time.sleep(3)