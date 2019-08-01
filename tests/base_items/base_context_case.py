import unittest
from utils.driver import Driver
from page_models.base_page_model import BasePageModel
from utils.screenshot import screenshots_collector
from page_context.base_page_context import BasePageContext


class BaseTestCase(unittest.TestCase):
	"""
	BaseTest
	This class should be the parent class to each unit test.
	It allows for instantiation of the database dynamically,
	and makes sure that it is a new, blank database each time.
	"""

	@classmethod
	def setUpClass(cls):
		cls.page = None

	def setUp(self):
		if self.page is not None:
			self.page.quit()
		self.page = None

	@classmethod
	def tearDownClass(cls):
		if cls.page:
			cls.page.quit()

	def tearDown(self):
		screenshots_collector()
		if self.page:
			self.page.close()

	def solutions_menu_items_test(self):
		self.assertEqual(BasePageContext.LEFT_MENU_ITEMS['Solutions']['text'],
		                 self.page.solutions_menu_text)
		self.assertEqual(BasePageContext.LEFT_MENU_ITEMS['Solutions']['class'],
		                 self.page.solutions_menu_class)

		self.assertEqual(BasePageContext.LEFT_MENU_ITEMS['About Us']['href'],
		                 self.page.about_us_menu_item_formated_href)
		self.assertEqual(BasePageContext.LEFT_MENU_ITEMS['About Us']['text'],
		                 self.page.about_us_menu_item_text)

		self.assertEqual(BasePageContext.LEFT_MENU_ITEMS['Services']['href'],
		                 self.page.services_us_menu_item_formated_href)
		self.assertEqual(BasePageContext.LEFT_MENU_ITEMS['Services']['text'],
		                 self.page.services_us_menu_item_text)

		self.assertEqual(BasePageContext.LEFT_MENU_ITEMS['Products']['href'],
		                 self.page.products_menu_item_formated_href)
		self.assertEqual(BasePageContext.LEFT_MENU_ITEMS['Products']['text'],
		                 self.page.products_menu_item_text)

		self.assertEqual(BasePageContext.LEFT_MENU_ITEMS['Locations']['href'],
		                 self.page.locations_menu_item_formated_href)
		self.assertEqual(BasePageContext.LEFT_MENU_ITEMS['Locations']['text'],
		                 self.page.locations_menu_item_text)

		self.assertEqual(BasePageContext.LEFT_MENU_ITEMS['Admin Page']['href'],
		                 self.page.admin_page_menu_item_formated_href)
		self.assertEqual(BasePageContext.LEFT_MENU_ITEMS['Admin Page']['text'],
		                 self.page.admin_page_menu_item_text)

	def right_menu_buttons_test(self):
		self.assertEqual(BasePageContext.MENU_BUTTONS['home']['href'],
		                 self.page.home_button_formated_href)
		self.assertEqual(BasePageContext.MENU_BUTTONS['home']['text'],
		                 self.page.home_button_text)

		self.assertEqual(BasePageContext.MENU_BUTTONS['about']['href'],
		                 self.page.about_button_formated_href)
		self.assertEqual(BasePageContext.MENU_BUTTONS['about']['text'],
		                 self.page.about_button_text)

		self.assertEqual(BasePageContext.MENU_BUTTONS['contact']['href'],
		                 self.page.contact_button_formated_href)
		self.assertEqual(BasePageContext.MENU_BUTTONS['contact']['text'],
		                 self.page.contact_button_text)

	def parabank_logo_test(self):
		self.assertEqual(BasePageContext.SLOGAN,
		                 self.page.slogan)
		self.assertEqual(BasePageContext.PARA_BANK_LOGO['href'],
		                 self.page.para_bank_logo_formated_href)
		self.assertEqual(BasePageContext.PARA_BANK_LOGO['class'],
		                 self.page.para_bank_logo_img_class)
		self.assertEqual(BasePageContext.PARA_BANK_LOGO['src'],
		                 self.page.para_bank_logo_formated_img_src)
		self.assertEqual(BasePageContext.PARA_BANK_LOGO['alt'],
		                 self.page.para_bank_logo_img_alt)
		self.assertEqual(BasePageContext.PARA_BANK_LOGO['title'],
		                 self.page.para_bank_logo_img_title)

	def parabank_admin_logo_test(self):
		self.assertEqual(BasePageContext.ADMIN_LOGO['href'],
		                 self.page.admin_logo_formated_href)
		self.assertEqual(BasePageContext.ADMIN_LOGO['class'],
		                 self.page.admin_logo_img_class)
		self.assertEqual(BasePageContext.ADMIN_LOGO['src'],
		                 self.page.admin_logo_formated_img_src)

	def customer_login_test(self):

		# Title:
		self.assertEqual(BasePageContext.CUSTOMER_LOGIN['login title'],
		                 self.page.customer_login_title)

		# Username:
		self.assertEqual(BasePageContext.CUSTOMER_LOGIN['username title'],
		                 self.page.username_login_title)
		self.assertEqual(BasePageContext.CUSTOMER_LOGIN['username input']['class'],
		                 self.page.username_input_class)
		self.assertEqual(BasePageContext.CUSTOMER_LOGIN['username input']['type'],
		                 self.page.username_input_type)
		self.assertEqual(BasePageContext.CUSTOMER_LOGIN['username input']['name'],
		                 self.page.username_input_name)

		# Password:
		self.assertEqual(BasePageContext.CUSTOMER_LOGIN['password title'],
		                 self.page.password_login_title)
		self.assertEqual(BasePageContext.CUSTOMER_LOGIN['password input']['class'],
		                 self.page.password_input_class)
		self.assertEqual(BasePageContext.CUSTOMER_LOGIN['password input']['type'],
		                 self.page.password_input_type)
		self.assertEqual(BasePageContext.CUSTOMER_LOGIN['password input']['name'],
		                 self.page.password_input_name)

		# Login Button
		self.assertEqual(BasePageContext.CUSTOMER_LOGIN['login button']['class'],
		                 self.page.login_button_class)
		self.assertEqual(BasePageContext.CUSTOMER_LOGIN['login button']['type'],
		                 self.page.login_button_type)
		self.assertEqual(BasePageContext.CUSTOMER_LOGIN['login button']['value'],
		                 self.page.login_button_value)

		# Forgot Login
		self.assertEqual(BasePageContext.FORGOT_LOGIN['href'],
		                 self.page.forgot_login_formated_href)
		self.assertEqual(BasePageContext.FORGOT_LOGIN['text'],
		                 self.page.forgot_login_text)

		# Register
		self.assertEqual(BasePageContext.REGISTER['href'],
		                 self.page.register_formated_href)
		self.assertEqual(BasePageContext.REGISTER['text'],
		                 self.page.register_text)

	def footer_items_test(self):

		self.assertEqual(BasePageContext.FOOTER['footer_menu']['home']['href'],
		                 self.page.footer_home_formated_href)
		self.assertEqual(BasePageContext.FOOTER['footer_menu']['home']['text'],
		                 self.page.footer_home_text)

		self.assertEqual(BasePageContext.FOOTER['footer_menu']['about us']['href'],
		                 self.page.footer_about_us_formated_href)
		self.assertEqual(BasePageContext.FOOTER['footer_menu']['about us']['text'],
		                 self.page.footer_about_us_text)
