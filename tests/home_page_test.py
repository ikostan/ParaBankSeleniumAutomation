from tests.base_test import BaseTestCase
from utils.driver import Driver
from page_models.home_page_model import HomePageModel
from page_context.home_page_context import HomePageContext


class MyTestCase(BaseTestCase):

	def test_something(self):
		browser = 'chrome'
		self.driver = Driver(browser)
		self.page = HomePageModel(self.driver)
		self.page.go()
		self.assertEqual(HomePageContext.TITLE, self.page.title)

