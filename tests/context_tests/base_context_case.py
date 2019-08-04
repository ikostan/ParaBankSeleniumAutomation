import allure
import unittest
from expected_results.page_context.base_page_context import BasePageContext


@allure.feature("Base Page")
# @allure.story('Base Context')
class TestBaseContextCase(unittest.TestCase):
	"""
	BaseTest
	This class should be the parent class to each test case class.
	"""

	@classmethod
	def setUpClass(cls):
		cls.page = None

	def setUp(self):
		with allure.step("""
		setUp: 
			1. Close current browser tab. 
			2. Set webdriver to None.
		"""):
			if self.page is not None:
				self.page.quit()
			self.page = None

	@classmethod
	def tearDownClass(cls):
		if cls.page:
			cls.page.quit()

	def tearDown(self):

		with allure.step("tearDown: close current browser tab"):
			# screenshots_collector()
			if self.page:
				self.page.close()

	def solutions_menu_items_test(self):

		with allure.step("Test 'Solutions' menu title: text + css"):
			self.assertEqual(BasePageContext.LEFT_MENU_ITEMS['Solutions']['text'],
			                 self.page.solutions_menu_text)

			self.assertEqual(BasePageContext.LEFT_MENU_ITEMS['Solutions']['class'],
			                 self.page.solutions_menu_class)

		with allure.step("Test 'Solutions' menu > 'About Us': text + href"):
			self.assertEqual(BasePageContext.LEFT_MENU_ITEMS['About Us']['href'],
			                 self.page.about_us_menu_item_formated_href)
			self.assertEqual(BasePageContext.LEFT_MENU_ITEMS['About Us']['text'],
			                 self.page.about_us_menu_item_text)

		with allure.step("Test 'Solutions' menu > 'Services': text + href"):
			self.assertEqual(BasePageContext.LEFT_MENU_ITEMS['Services']['href'],
			                 self.page.services_us_menu_item_formated_href)
			self.assertEqual(BasePageContext.LEFT_MENU_ITEMS['Services']['text'],
			                 self.page.services_us_menu_item_text)

		with allure.step("Test 'Solutions' menu > 'Products': text + href"):
			self.assertEqual(BasePageContext.LEFT_MENU_ITEMS['Products']['href'],
			                 self.page.products_menu_item_formated_href)
			self.assertEqual(BasePageContext.LEFT_MENU_ITEMS['Products']['text'],
			                 self.page.products_menu_item_text)

		with allure.step("Test 'Solutions' menu > 'Locations': text + href"):
			self.assertEqual(BasePageContext.LEFT_MENU_ITEMS['Locations']['href'],
			                 self.page.locations_menu_item_formated_href)
			self.assertEqual(BasePageContext.LEFT_MENU_ITEMS['Locations']['text'],
			                 self.page.locations_menu_item_text)

		with allure.step("Test 'Solutions' menu > 'Admin Page': text + href"):
			self.assertEqual(BasePageContext.LEFT_MENU_ITEMS['Admin Page']['href'],
			                 self.page.admin_page_menu_item_formated_href)
			self.assertEqual(BasePageContext.LEFT_MENU_ITEMS['Admin Page']['text'],
			                 self.page.admin_page_menu_item_text)

	def right_menu_home_button_test(self):

		with allure.step('Do "Home" button verification > verify button href. Expected: {}.'.format(
				BasePageContext.MENU_BUTTONS['home']['href'])):
			self.assertEqual(BasePageContext.MENU_BUTTONS['home']['href'],
			                 self.page.home_button_formated_href)

		with allure.step('Do "Home" button verification > verify button label. Expected: {}.'.format(
				BasePageContext.MENU_BUTTONS['home']['text'])):
			self.assertEqual(BasePageContext.MENU_BUTTONS['home']['text'],
			                 self.page.home_button_text)

	def right_menu_about_button_test(self):

		with allure.step('Do "About" button verification > verify button href. Expected: {}.'.format(
				BasePageContext.MENU_BUTTONS['about']['href'])):
			self.assertEqual(BasePageContext.MENU_BUTTONS['about']['href'],
			                 self.page.about_button_formated_href)

		with allure.step('Do "About" button verification > verify button label. Expected: {}.'.format(
				BasePageContext.MENU_BUTTONS['about']['text'])):
			self.assertEqual(BasePageContext.MENU_BUTTONS['about']['text'],
			                 self.page.about_button_text)

	def right_menu_contact_button_test(self):

		with allure.step('Do "Contact" button verification > verify button href. Expected: {}.'.format(
				BasePageContext.MENU_BUTTONS['contact']['href'])):
			self.assertEqual(BasePageContext.MENU_BUTTONS['contact']['href'],
			                 self.page.contact_button_formated_href)

		with allure.step('Do "Contact" button verification > verify button href. Expected: {}.'.format(
				BasePageContext.MENU_BUTTONS['contact']['text'])):
			self.assertEqual(BasePageContext.MENU_BUTTONS['contact']['text'],
			                 self.page.contact_button_text)

	def parabank_logo_test(self):

		with allure.step("Test 'ParaBank' logo > slogan"):
			self.assertEqual(BasePageContext.SLOGAN,
			                 self.page.slogan)

		with allure.step("Test 'ParaBank' logo > href"):
			self.assertEqual(BasePageContext.PARA_BANK_LOGO['href'],
			                 self.page.para_bank_logo_formated_href)

		with allure.step("Test 'ParaBank' logo > class"):
			self.assertEqual(BasePageContext.PARA_BANK_LOGO['class'],
			                 self.page.para_bank_logo_img_class)

		with allure.step("Test 'ParaBank' logo > src"):
			self.assertEqual(BasePageContext.PARA_BANK_LOGO['src'],
			                 self.page.para_bank_logo_formated_img_src)

		with allure.step("Test 'ParaBank' logo > alt"):
			self.assertEqual(BasePageContext.PARA_BANK_LOGO['alt'],
			                 self.page.para_bank_logo_img_alt)

		with allure.step("Test 'ParaBank' logo > title"):
			self.assertEqual(BasePageContext.PARA_BANK_LOGO['title'],
			                 self.page.para_bank_logo_img_title)

	def parabank_admin_logo_test(self):

		with allure.step("Test 'Admin' logo > href"):
			self.assertEqual(BasePageContext.ADMIN_LOGO['href'],
			                 self.page.admin_logo_formated_href)

		with allure.step("Test 'Admin' logo > class"):
			self.assertEqual(BasePageContext.ADMIN_LOGO['class'],
			                 self.page.admin_logo_img_class)

		with allure.step("Test 'Admin' logo > src"):
			self.assertEqual(BasePageContext.ADMIN_LOGO['src'],
			                 self.page.admin_logo_formated_img_src)

	def customer_login_test(self):

		# Title:
		with allure.step("Test 'Customer Login' logo > title"):
			self.assertEqual(BasePageContext.CUSTOMER_LOGIN['login title'],
			                 self.page.customer_login_title)

		# Username:
		with allure.step("Test 'Customer Login' > Username title > title"):
			self.assertEqual(BasePageContext.CUSTOMER_LOGIN['username title'],
			                 self.page.username_login_title)
		with allure.step("Test 'Customer Login' logo > Username field > class"):
			self.assertEqual(BasePageContext.CUSTOMER_LOGIN['username input']['class'],
			                 self.page.username_input_class)
		with allure.step("Test 'Customer Login' logo > Username field > type"):
			self.assertEqual(BasePageContext.CUSTOMER_LOGIN['username input']['type'],
			                 self.page.username_input_type)
		with allure.step("Test 'Customer Login' logo > Username field > name"):
			self.assertEqual(BasePageContext.CUSTOMER_LOGIN['username input']['name'],
			                 self.page.username_input_name)

		# Password:
		with allure.step("Test 'Customer Login' > Password title > title"):
			self.assertEqual(BasePageContext.CUSTOMER_LOGIN['password title'],
			                 self.page.password_login_title)
		with allure.step("Test 'Customer Login' > Password field > class"):
			self.assertEqual(BasePageContext.CUSTOMER_LOGIN['password input']['class'],
			                 self.page.password_input_class)
		with allure.step("Test 'Customer Login' > Password field > type"):
			self.assertEqual(BasePageContext.CUSTOMER_LOGIN['password input']['type'],
			                 self.page.password_input_type)
		with allure.step("Test 'Customer Login' > Password field > name"):
			self.assertEqual(BasePageContext.CUSTOMER_LOGIN['password input']['name'],
			                 self.page.password_input_name)

		# Login Button
		with allure.step("Test 'Customer Login' > Login button > class"):
			self.assertEqual(BasePageContext.CUSTOMER_LOGIN['login button']['class'],
			                 self.page.login_button_class)
		with allure.step("Test 'Customer Login' > Login button > class"):
			self.assertEqual(BasePageContext.CUSTOMER_LOGIN['login button']['type'],
			                 self.page.login_button_type)
		with allure.step("Test 'Customer Login' > Login button > class"):
			self.assertEqual(BasePageContext.CUSTOMER_LOGIN['login button']['value'],
			                 self.page.login_button_value)

		# Forgot Login
		with allure.step("Test 'Customer Login' > Forgot Login > href"):
			self.assertEqual(BasePageContext.FORGOT_LOGIN['href'],
			                 self.page.forgot_login_formated_href)
		with allure.step("Test 'Customer Login' > Forgot Login > text"):
			self.assertEqual(BasePageContext.FORGOT_LOGIN['text'],
			                 self.page.forgot_login_text)

		# Register
		with allure.step("Test 'Customer Login' > Register > href"):
			self.assertEqual(BasePageContext.REGISTER['href'],
			                 self.page.register_formated_href)
		with allure.step("Test 'Customer Login' > Register > text"):
			self.assertEqual(BasePageContext.REGISTER['text'],
			                 self.page.register_text)

	def footer_items_test(self):

		# Home
		with allure.step("Test 'Footer' items > 'Home' > href"):
			self.assertEqual(BasePageContext.FOOTER['footer menu']['home']['href'],
			                 self.page.footer_home_formated_href)
		with allure.step("Test 'Footer' items > 'Home' > text"):
			self.assertEqual(BasePageContext.FOOTER['footer menu']['home']['text'],
			                 self.page.footer_home_text)

		# About Us
		with allure.step("Test 'Footer' items > 'About Us' > href"):
			self.assertEqual(BasePageContext.FOOTER['footer menu']['about us']['href'],
			                 self.page.footer_about_us_formated_href)
		with allure.step("Test 'Footer' items > 'About Us' > text"):
			self.assertEqual(BasePageContext.FOOTER['footer menu']['about us']['text'],
			                 self.page.footer_about_us_text)

		# Services
		with allure.step("Test 'Footer' items > 'Services' > href"):
			self.assertEqual(BasePageContext.FOOTER['footer menu']['services']['href'],
			                 self.page.footer_services_formated_href)
		with allure.step("Test 'Footer' items > 'Services' > text"):
			self.assertEqual(BasePageContext.FOOTER['footer menu']['services']['text'],
			                 self.page.footer_services_text)

		# Products
		with allure.step("Test 'Footer' items > 'Products' > href"):
			self.assertEqual(BasePageContext.FOOTER['footer menu']['products']['href'],
			                 self.page.footer_products_formated_href)
		with allure.step("Test 'Footer' items > 'Products' > text"):
			self.assertEqual(BasePageContext.FOOTER['footer menu']['products']['text'],
			                 self.page.footer_products_text)

		# Locations
		with allure.step("Test 'Footer' items > 'Locations' > href"):
			self.assertEqual(BasePageContext.FOOTER['footer menu']['locations']['href'],
			                 self.page.footer_locations_formated_href)
		with allure.step("Test 'Footer' items > 'Locations' > text"):
			self.assertEqual(BasePageContext.FOOTER['footer menu']['locations']['text'],
			                 self.page.footer_locations_text)

		# Forum
		with allure.step("Test 'Footer' items > 'Forum' > href"):
			self.assertEqual(BasePageContext.FOOTER['footer menu']['forum']['href'],
			                 self.page.footer_forum_formated_href)
		with allure.step("Test 'Footer' items > 'Forum' > text"):
			self.assertEqual(BasePageContext.FOOTER['footer menu']['forum']['text'],
			                 self.page.footer_forum_text)

		# Site Map
		with allure.step("Test 'Footer' items > 'Site Map' > href"):
			self.assertEqual(BasePageContext.FOOTER['footer menu']['site map']['href'],
			                 self.page.footer_site_map_formated_href)
		with allure.step("Test 'Footer' items > 'Site Map' > text"):
			self.assertEqual(BasePageContext.FOOTER['footer menu']['site map']['text'],
			                 self.page.footer_site_map_text)

		# Contact Us
		with allure.step("Test 'Footer' items > 'Contact Us' > href"):
			self.assertEqual(BasePageContext.FOOTER['footer menu']['contact us']['href'],
			                 self.page.footer_contact_us_formated_href)
		with allure.step("Test 'Footer' items > 'Contact Us' > text"):
			self.assertEqual(BasePageContext.FOOTER['footer menu']['contact us']['text'],
			                 self.page.footer_contact_us_text)

		# Copyright
		with allure.step("Test 'Footer' items > 'Copyright' > class"):
			self.assertEqual(BasePageContext.FOOTER['copyright']['class'],
			                 self.page.footer_copyright_class)
		with allure.step("Test 'Footer' items > 'Copyright' > text"):
			self.assertEqual(BasePageContext.FOOTER['copyright']['text'],
			                 self.page.footer_copyright_text)

		# Visit
		with allure.step("Test 'Footer' items > 'Visit' > link > href"):
			self.assertEqual(BasePageContext.FOOTER['visit']['link']['href'],
			                 self.page.footer_visit_link_formated_href)
		with allure.step("Test 'Footer' items > 'Visit' > link > text"):
			self.assertEqual(BasePageContext.FOOTER['visit']['link']['text'],
			                 self.page.footer_visit_link_text)
		with allure.step("Test 'Footer' items > 'Visit' > link > target"):
			self.assertEqual(BasePageContext.FOOTER['visit']['link']['target'],
			                 self.page.footer_visit_link_target)
		with allure.step("Test 'Footer' items > 'Visit' > text"):
			self.assertEqual(BasePageContext.FOOTER['visit']['text'],
			                 self.page.footer_visit_us_text)
