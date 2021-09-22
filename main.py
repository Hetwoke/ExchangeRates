import requests
from bs4 import BeautifulSoup
import time

class Currency:
    EUR_RUB = "https://www.google.com/search?q=курс+евро+к+рублю&client=opera-gx&hs=9RC&ei=oo9LYa6TIeiErwS2zqzQBA&oq=курс+евро+к+рублю&gs_lcp=Cgdnd3Mtd2l6EAxKBAhBGABQAFgAYJ4faABwAngAgAEAiAEAkgEAmAEA&sclient=gws-wiz&ved=0ahUKEwiu7MfDs5PzAhVowosKHTYnC0oQ4dUDCA4"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 OPR/78.0.4093.214"}

    current_converted_price = 0
    difference = 5

    def __init__(self):
        self.current_converted_price = float(self.get_currency_price())

    def get_currency_price(self):
        full_page = requests.get(self.EUR_RUB, headers=self.headers)

        soup = BeautifulSoup(full_page.content, "html.parser")

        convert = soup.findAll("span", {"class": "DFlifde", "class": "SwHCTb", "data-precision": 2})
        return convert[0].test

    def check_currency(self):
        currency = float(self.get_currency_price().replace(",", "."))
        if currency >= self.current_converted_price + self.difference:
            print("Cours very high, we need to do sth.")
        elif currency <= self.current_converted_price - self.difference:
            print("Cours very low, we need to do sth.")
        print("Now cours: 1 eur = " + str(currency))
        time.sleep(5)
        self.check_currency()


currency = Currency()
currency.check_currency()
