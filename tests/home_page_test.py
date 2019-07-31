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

	def test_context_base_elements_edge(self):

		self.open_web_browser('edge')

		# Test base context:
		self.verify_page_url_title()
		self.verify_parabank_admin_logo()
		self.verify_parabank_logo()
		self.verify_right_menu_buttons()

	def test_context_base_elements_mozilla(self):

		self.open_web_browser('mozilla')

		# Test base context:
		self.verify_page_url_title()
		self.verify_parabank_admin_logo()
		self.verify_parabank_logo()
		self.verify_right_menu_buttons()

	def verify_right_menu_buttons(self):
		self.assertEqual(HomePageContext.MENU_BUTTONS['home']['href'],
		                 self.page.home_button_formated_href)
		self.assertEqual(HomePageContext.MENU_BUTTONS['home']['text'],
		                 self.page.home_button_text)

		self.assertEqual(HomePageContext.MENU_BUTTONS['about']['href'],
		                 self.page.about_button_formated_href)
		self.assertEqual(HomePageContext.MENU_BUTTONS['about']['text'],
		                 self.page.about_button_text)

		self.assertEqual(HomePageContext.MENU_BUTTONS['contact']['href'],
		                 self.page.contact_button_formated_href)
		self.assertEqual(HomePageContext.MENU_BUTTONS['contact']['text'],
		                 self.page.contact_button_text)

	def verify_parabank_logo(self):
		self.assertEqual(HomePageContext.SLOGAN,
		                 self.page.slogan)
		self.assertEqual(HomePageContext.PARA_BANK_LOGO['href'],
		                 self.page.para_bank_logo_formated_href)
		self.assertEqual(HomePageContext.PARA_BANK_LOGO['class'],
		                 self.page.para_bank_logo_img_class)
		self.assertEqual(HomePageContext.PARA_BANK_LOGO['src'],
		                 self.page.para_bank_logo_formated_img_src)
		self.assertEqual(HomePageContext.PARA_BANK_LOGO['alt'],
		                 self.page.para_bank_logo_img_alt)
		self.assertEqual(HomePageContext.PARA_BANK_LOGO['title'],
		                 self.page.para_bank_logo_img_title)

	def verify_parabank_admin_logo(self):
		self.assertEqual(HomePageContext.ADMIN_LOGO['href'],
		                 self.page.admin_logo_formated_href)
		self.assertEqual(HomePageContext.ADMIN_LOGO['class'],
		                 self.page.admin_logo_img_class)
		self.assertEqual(HomePageContext.ADMIN_LOGO['src'],
		                 self.page.admin_logo_formated_img_src)

	def verify_page_url_title(self):
		self.assertEqual(HomePageContext.URL,
		                 self.page.url)
		self.assertEqual(HomePageContext.TITLE,
		                 self.page.title)

	def open_web_browser(self, browser):
		# Open web page
		driver = Driver(browser)
		self.page = HomePageModel(driver=driver, implicit_wait_time=5, explicit_wait_time=10)
		self.page.go()
