from django.test import TestCase
from stock.models import Stock, Reits

class StockClassTest(TestCase):

    def test_stock_class_definition(self):
        ticker_test = "BBAS3"
        price_test = 27.30
        my_stock = Stock(ticker=ticker_test, price=price_test)
        self.assertEqual(my_stock.ticker, ticker_test)
        self.assertEqual(my_stock.price, price_test)

    def test_reits_class_definition(self):
        ticker_test = "IRDM11"
        price_test = 77.30
        my_reits = Reits(ticker=ticker_test, price=price_test)
        self.assertEqual(my_reits.ticker, ticker_test)
        self.assertEqual(my_reits.price, price_test)