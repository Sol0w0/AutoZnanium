# AutoZnanium
Код для авто захода на книгу в Znanium раз в 35 минут
## Зависимости
Для работы нужны:
- Python
- Selenium
## Гайд
В main.py ищете где вписать пароль и почту и пишите вместо `***`.
```python
driver.find_element(By.ID, "loginform-username").send_keys("***") #Почта
driver.find_element(By.ID, "loginform-password").send_keys("***") #Пароль
```
Замените строчку с сайтом на необходимую книгу в `driver.get("")`:
```python
driver.get("https://znanium.ru/read?id=******")
```
Можно выбрать WebDriver:
```python
with openChrome() as driver:
#Или
with openFirefox() as driver:
```
Можно включить/выключить показ окна браузера:
```python
options.add_argument("--headless=new") #Chrome
options.add_argument("-headless") #Firefox
```
После, запускается скрипт. Можно выйти из скрипта в любой момент нажав Enter.
## Примечания
- При множественных одновременных заходах на сайт, сайт отправит вас в тайм аут при попытке захода. За время использования этого не было замечено, но все может быть.
- Если во время работы скрипта зайти на любую другую книгу, то время отката между открытем книги собъется, и сайт *возможно* не засчитает следущий заход. *Возможно*.
