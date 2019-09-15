import requests
import time

# подключила BeautifulSoup
from bs4 import BeautifulSoup

# переменная для хранения инфы о товарах
d = []

# кол-во страниц с товарами
for j in range(50):
    # указываем url (сайт) и get параметры запроса
    url = 'https://www.foxtrot.com.ua/ru/shop/mobilnye_telefony_apple.html'
    # указываем get параметр для определения номера страницы товаров
    par = {'p': j}
    # записываем ответ в переменную r
    r = requests.get(url, params=par)
    # объект  BeautifulSoup записываем в переменную soup
    soup = BeautifulSoup(r.text, 'html.parser')
    # перебераем товары из страниц и получаем необходимую инфу
    for i in range(20):
        # название товара
        product = soup.find_all(class_='listing-item__info')[i].get_text()
        # чистим от ненужных переходов на новую строку
        product = product.replace('\n', '')

        # цена товара
        price = soup.find_all(class_='price')[i].get_text()
        # чистим от ненужных переходов на новую строку
        price = price.replace('\n', ' ')

        # ссылка на товар
        link = soup.find_all(class_='listing-link detail-link')[i].get('href')

        # добавляем домен к ссылке
        link = 'www.foxtrot.com.ua' + link

        # список со всеми собраными даныыми о товаре
        d.append([product, price, link])

# открываем файл для записи нашей инфы
with open('/home/anya/PycharmProjects/Final_project/text.txt', 'w') as ouf:
    # перебираем элементы списка d
    for i in d:
        # преобразуем элемент списка в строку
        i = str(i)
        # очищаем строку от ненужных символов
        i = i.replace("\'", "")
        i = i.replace("[", "")
        i = i.replace("]", "")
        # записываем строку в файл
        ouf.write(i + '\n')

# подсчитываем время выполнения программы
start_time = time.time()
print('Time : {} seconds.'.format(time.time() - start_time))
