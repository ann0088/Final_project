from my_time1 import my_decorator

# url = 'https://www.foxtrot.com.ua/ru/shop/mobilnye_telefony_apple.html'

@my_decorator
def my_parsing (url, domen, d):
    import requests
    from bs4 import BeautifulSoup
    # кол-во страниц с товарами
    for j in range(50):
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
        #price = soup.find_all(class_='price')[i].get_text()
        # чистим от ненужных переходов на новую строку
        #price = price.replace('\n', ' ')

        # ссылка на товар
            link = soup.find_all(class_='listing-link detail-link')[i].get('href')

        # добавляем домен к ссылке
            link = domen + link

        # список со всеми собраными даныыми о товаре
            d.append([product, link])
        return d

d = []
domen = input('Input domen : ')
url = input('Input url : ')
my_parsing(url, domen, d)

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


