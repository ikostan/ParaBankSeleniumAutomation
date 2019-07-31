from utils.driver import Driver
from tests.base_test import BaseTestCase
from page_models.home_page_model import HomePageModel
from page_context.home_page_context import HomePageContext


class MyTestCase(BaseTestCase):

	def test_home_page_is_up(self):
		browser = 'chrome'
		self.driver = Driver(browser)
		self.page = HomePageModel(self.driver)
		self.page.go()
		self.assertEqual(HomePageContext.TITLE, self.page.title)

