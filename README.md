# AutoZnanium
Код для авто захода на книгу в Znanium раз в 30 минут
## Зависимости
Для работы нужны:
- Python
- Selenium
## Гайд
В auto.py ищете где вписать пароль и почту и пишите.
```python
driver.find_element(By.ID, "loginform-username").send_keys("***") #почта
driver.find_element(By.ID, "loginform-password").send_keys("***") #пароль
```
Замените строчку с сайтом на необходимую книгу:
```python
driver.get("https://znanium.ru/read?id=******")
```
При желании, можно заменить веб драйвер на Firefox, убрав перед этим options. **В Firefox не работает headless, соответственно** :
```python
with webdriver.Chrome(options=options) as driver:
with webdriver.Firefox() as driver:
```
Также (используя ChromeDriver), можно включить/выключить показ окна браузера:
```python
options.add_argument("--headless=new")
```
После, запускается скрипт. Он работает **бесконечно** (или пока сайт не сдохнет). Можно спокойно заменить `while True` на `for i in range(n)`, как удобно
## Примечания
- При множественных одновременных заходах на сайт, сайт отправит вас в тайм аут при попытке захода. За время использования этого не было замечено, но все может быть.
- Если во время работы скрипта зайти на любую другую книгу, то время отката между открытем книги собъется, и сайт *возможно* не засчитает следущий заход. *Возможно*.
