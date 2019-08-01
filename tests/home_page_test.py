import unittest
from utils.driver import Driver
from utils.screenshot import screenshot_on_fail
from tests.base_test import BaseTestCase
from page_models.home_page_model import HomePageModel
from page_context.home_page_context import HomePageContext


@screenshot_on_fail()
class HomePageTestCase(BaseTestCase):

	def test_context_base_elements_chrome(self):

		self.open_web_browser('chrome')

		# Test base context:
		self.verify_page_url_title()
		self.verify_parabank_admin_logo()
		self.verify_parabank_logo()
		self.verify_right_menu_buttons()
		self.verify_solutions_menu_items()

	@unittest.skip('N/A')
	def test_context_base_elements_edge(self):

		self.open_web_browser('edge')

		# Test base context:
		self.verify_page_url_title()
		self.verify_parabank_admin_logo()
		self.verify_parabank_logo()
		self.verify_right_menu_buttons()

	@unittest.skip('N/A')
	def test_context_base_elements_mozilla(self):

		self.open_web_browser('mozilla')

		# Test base context:
		self.verify_page_url_title()
		self.verify_parabank_admin_logo()
		self.verify_parabank_logo()
		self.verify_right_menu_buttons()

	def open_web_browser(self, browser):
		# Open web page
		driver = Driver(browser)
		self.page = HomePageModel(driver=driver, implicit_wait_time=5, explicit_wait_time=10)
		self.page.go()

	def verify_page_url_title(self):
		self.assertEqual(HomePageContext.URL,
		                 self.page.url)
		self.assertEqual(HomePageContext.TITLE,
		                 self.page.title)
