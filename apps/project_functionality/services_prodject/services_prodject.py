# url = [
#     'https://www.enableme.com.ua/ru/article/kontakti-gumanitarnoi-dopomogi-v-ukraini-7456',
#     'https://dp.informator.ua/ru/vo-vseh-rajonah-dnepra-rabotayut-volonterskie-shtaby',
#     'https://suspilne.media/211627-u-dnipri-vidkrivaut-novi-volonterski-stabi-kudi-mozna-prinesti-dopomogu-dla-vijskovih/',
#     'https://dp.informator.ua/ru/poselenie-pereselentsev-v-dnepre-spisok-adresov-i-usloviya-prozhivaniya',
#     'https://svoi.city/articles/207866/gumanitarnaya-pomosch-v-dnepre',
#     'https://dnepr.detivgorode.ua/dnepr/u-dnipri-pratsiuiut-punkty-zboru-dopomogy-dlia-pereselentsiv-ta-zsu/',
#     'https://donpatriot.news/ru/article/u-dnipri-vpo-mozhut-otrimati-dopomogu-adresi-ta-telefoni',
#
# ]
#
#
# response = requests.get(url)
#
# soup = BeautifulSoup(response.content, 'html.parser')
#
# # punkty_pomoshchi = []
# # for punkt in soup.find_all('div', string="Днепр"):
# #     print(punkt)
# urls=[]
# for link_element in soup.find_all("a"):
#     url = link_element.get("href")
#     urls.append(url)
# # nazvanie = punkt.find_all('a href').text
#     # adres = punkt.find('div', class_='adres').text.strip()
#     # telefon = punkt.find('div', class_='telefon').text.strip()
#     # punkty_pomoshchi.append({'nazvanie': nazvanie, 'adres': adres, 'telefon': telefon})
# #     punkty_pomoshchi.append({'nazvanie': nazvanie})
# #
# # print(punkty_pomoshchi)
# print(urls)


import asyncio
import itertools
from typing import TypeAlias

import aiohttp
import bs4

import urllib.parse

T_URL: TypeAlias = str
T_URLS: TypeAlias = list[T_URL]
T_TEXT: TypeAlias = str


async def get_urls_from_text(text: T_TEXT) -> T_URLS:
    soup = bs4.BeautifulSoup(markup=text, features="html.parser")
    urls = []
    for link_element in soup.find_all("a"):
        url = link_element.get("href")
        urls.append(url)
    return list(set(urls))


# выполнить несколько запросов к одному и тому же серверу, используя одно соединение и одну сессию.
# выполняет HTTP-запрос к заданному URL-адресу и возвращает HTML-код ответа в виде текста (T_TEXT).
async def make_request(url: str, session: aiohttp.ClientSession) -> T_TEXT:
    async with session.get(
        url
    ) as response:  # оператор для создания контекста, в котором выполняется асинхронный запрос к URL-адресу
        return await response.text()  # метод .text()  чтобы получить тело ответа в виде текста (T_TEXT).


async def handle_url(url: str, session: aiohttp.ClientSession) -> T_URLS:
    text = await make_request(url=url, session=session)
    temp_urls = await get_urls_from_text(text=text)
    result_urls = []  # получили список сслок, их нажо нормалтзовать
    for temp_url in temp_urls:
        if not temp_url.startswith("http"):  # если начинается со / - то это относительная ссылка
            result_urls.append(urllib.parse.urljoin(base=url, url=temp_url))
        else:
            result_urls.append(temp_url)

    return result_urls


async def make_requests(urls: list[str]) -> T_URLS:
    async with aiohttp.ClientSession() as session:
        tasks = [handle_url(url=url, session=session) for url in urls]
        results = await asyncio.gather(*tasks)
        return list(itertools.chain(*results))  # метод .text()  чтобы получить тело ответа в виде текста (T_TEXT).


async def async_crawler():
    urls_input = [
        "https://www.enableme.com.ua/ru/article/kontakti-gumanitarnoi-dopomogi-v-ukraini-7456",
        # 'https://dp.informator.ua/ru/vo-vseh-rajonah-dnepra-rabotayut-volonterskie-shtaby',
        #
        #
        # 'https://dp.informator.ua/ru/poselenie-pereselentsev-v-dnepre-spisok-adresov-i-usloviya-prozhivaniya',
        # 'https://svoi.city/articles/207866/gumanitarnaya-pomosch-v-dnepre',
        # 'https://dnepr.detivgorode.ua/dnepr/u-dnipri-pratsiuiut-punkty-zboru-dopomogy-dlia-pereselentsiv-ta-zsu/',
        # 'https://donpatriot.news/ru/article/u-dnipri-vpo-mozhut-otrimati-dopomogu-adresi-ta-telefoni',
        "https://freeradio.com.ua/ru/esly-jevakuyrovalys-v-dnepr-hde-poluchyt-pomoshch-edu-zhyle-y-veshchy/",
        "https://github.com/AndrewStetsenko/Support-Ukraine",
    ]

    urls_output = sorted(
        set(await make_requests(urls=urls_input))
    )  # вызывает функцию make_requests, передавая ей список входных URL-адресов, и затем сортирует и удаляет дубликаты
    print(urls_output)


def async_crawler_main():
    asyncio.run(async_crawler())


async_crawler_main()
