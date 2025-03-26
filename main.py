import time
import random
import threading
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as firefoxOptions
from selenium.webdriver.chrome.options import Options as chromeOptions

mail = "***"
password = "***"
link = "https://znanium.ru/read?id=******"
       
def openFirefox():
    options = firefoxOptions()
    options.add_argument("-headless")
    options.set_preference("media.peerconnection.enabled", False)
    options.set_preference("permissions.default.image", 2)
    options.set_preference("browser.cache.disk.enable", False)
    options.set_preference("dom.ipc.processCount", 1)
    options.set_preference("browser.cache.memory.enable", False)
    options.set_preference("javascript.enabled", False)
    options.set_preference("toolkit.telemetry.enabled", False)
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    return driver
    
def openChrome():
    options = chromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument("--headless=new")
    options.add_argument("--log-level=3")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--disable-extensions")
    options.add_argument("--blink-settings=imagesEnabled=false")
    options.add_argument("--mute-audio")
    driver = webdriver.Chrome(options=options)
    return driver
    
def fastExit():
    input("Чтобы выйти из программы нажмите Enter\n")
    print("Программа остановлена")
    driver.get("https://znanium.ru/site/logout")
    driver.quit()
    os._exit(0)
    
thread = threading.Thread(target=fastExit, daemon=True)
thread.start()
 
with openFirefox() as driver:
    driver.get("https://znanium.ru/site/login")
    print("Открыт сайт логина")
    driver.find_element(By.ID, "loginform-username").send_keys(mail) 
    driver.find_element(By.ID, "loginform-password").send_keys(password)
    driver.find_element(By.ID, "loginform-password").send_keys(Keys.RETURN)
    print("Получен доступ к аккаунту")
    time.sleep(5)
    att = 0
    try:
        while True:
            driver.get(link)
            time.sleep(5)
            try:
                page = driver.find_element(By.ID,"page")
                page.clear()
                page.send_keys(random.randint(1,int(page.get_attribute("max"))))
                page.send_keys(Keys.RETURN)
            except:
                print("Программа не смогла рандомизировать страницу.\nЕсли вас и так устраивает, не обращайте внимания :)")
            att += 1
            print("Кол-во заходов: %d" % att, end="\r")
            time.sleep(2100)
            driver.get("https://znanium.ru")
            time.sleep(3)  
    except:
        print("Программа остановлена по неизвестной причине")