# AutoZnanium
Код для авто захода на книгу в Znanium раз в 35 минут
## Зависимости
Для работы нужны:
- Python
- Selenium
## Гайд
В main.py ищете где вписать пароль, почту и ссылку на книгу и пишите вместо `***` подходящие значения:
```python
mail = "***"
password = "***"
link = "https://znanium.ru/read?id=******"
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
После, запускается скрипт. Можно выйти из скрипта в любой момент нажав Enter (если скрипт открыт в консоли).
## Примечания
- При множественных одновременных заходах на сайт, сайт отправит вас в тайм аут при попытке захода. За время использования этого не было замечено, но все может быть.
- Если во время работы скрипта зайти на любую другую книгу, то время отката между открытем книги собъется, и сайт *возможно* не засчитает следущий заход. *Возможно*.
