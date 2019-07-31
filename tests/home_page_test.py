from utils.driver import Driver
from tests.base_test import BaseTestCase
from page_models.home_page_model import HomePageModel
from page_context.home_page_context import HomePageContext


class HomePageTestCase(BaseTestCase):

	def test_context_base_elements_chrome(self):

		# Open web page
		browser = 'chrome'
		self.driver = Driver(browser)
		self.page = HomePageModel(self.driver)
		self.page.go()

		# Test base context:
		self.assertEqual(HomePageContext.URL, self.page.url)
		self.assertEqual(HomePageContext.SLOGAN, self.page.slogan)
		self.assertEqual(HomePageContext.TITLE, self.page.title)
		self.assertEqual(HomePageContext.ADMIN_LOGO['href'], self.page.admin_logo_formated_href)
		self.assertEqual(HomePageContext.ADMIN_LOGO['class'], self.page.admin_logo_img_class)
		self.assertEqual(HomePageContext.ADMIN_LOGO['src'], self.page.admin_logo_formated_img_src)

