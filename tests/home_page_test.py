from utils.driver import Driver
from tests.base_test import BaseTestCase
from page_models.home_page_model import HomePageModel
from page_context.home_page_context import HomePageContext


class HomePageTestCase(BaseTestCase):

	def test_context_base_elements_chrome(self):

		# Open web page
		browser = 'chrome'
		self.driver = Driver(browser)
		self.page = HomePageModel(driver=self.driver, implicit_wait_time=5)
		self.page.go()

		# Test base context:
		self.assertEqual(HomePageContext.URL, self.page.url)
		self.assertEqual(HomePageContext.SLOGAN, self.page.slogan)
		self.assertEqual(HomePageContext.TITLE, self.page.title)

		self.assertEqual(HomePageContext.ADMIN_LOGO['href'], self.page.admin_logo_formated_href)
		self.assertEqual(HomePageContext.ADMIN_LOGO['class'], self.page.admin_logo_img_class)
		self.assertEqual(HomePageContext.ADMIN_LOGO['src'], self.page.admin_logo_formated_img_src)

		self.assertEqual(HomePageContext.PARA_BANK_LOGO['href'], self.page.para_bank_logo_formated_href)
		self.assertEqual(HomePageContext.PARA_BANK_LOGO['class'], self.page.para_bank_logo_img_class)
		self.assertEqual(HomePageContext.PARA_BANK_LOGO['src'], self.page.para_bank_logo_formated_img_src)
		self.assertEqual(HomePageContext.PARA_BANK_LOGO['alt'], self.page.para_bank_logo_img_alt)
		self.assertEqual(HomePageContext.PARA_BANK_LOGO['title'], self.page.para_bank_logo_img_title)


