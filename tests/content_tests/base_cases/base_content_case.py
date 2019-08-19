#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
import unittest
from utils.step_definition import step_definition
from expected_results.page_content.base_page_content import BasePageContent


class BaseContentCase(unittest.TestCase):
	"""
	BaseTest
	This class should be the parent class to each test case class.
	"""

	def verify_solutions_menu_items(self):
		allure.dynamic.description("""
		Context base elements validation > 'Solutions' menu items:
			1. Open Home web page
			2. Do 'Solutions' menu items verification
		""")
		allure.dynamic.title("'Solutions' menu items test")

		allure.dynamic.severity(allure.severity_level.MINOR)

		step_definition(self,
		                expected=BasePageContent.LEFT_MENU_ITEMS['Solutions']['text'],
		                actual=self.page.solutions_menu_text,
		                step_description="Test 'Solutions' menu title: text")

		step_definition(self,
		                expected=BasePageContent.LEFT_MENU_ITEMS['Solutions']['class'],
		                actual=self.page.solutions_menu_class,
		                step_description="Test 'Solutions' menu title: class")

		'''
		with allure.step("Test 'Solutions' menu title: text + css"):
			self.assertEqual(BasePageContent.LEFT_MENU_ITEMS['Solutions']['text'],
			                 self.page.solutions_menu_text)
			self.assertEqual(BasePageContent.LEFT_MENU_ITEMS['Solutions']['class'],
			                 self.page.solutions_menu_class)
		'''

		step_definition(self,
		                expected=self.config.base_url + BasePageContent.LEFT_MENU_ITEMS['About Us']['href'],
		                actual=self.page.about_us_menu_item_formated_href,
		                step_description="Test 'Solutions' menu > 'About Us': href")

		step_definition(self,
		                expected=BasePageContent.LEFT_MENU_ITEMS['About Us']['text'],
		                actual=self.page.about_us_menu_item_text,
		                step_description="Test 'Solutions' menu > 'About Us': text")

		'''
		with allure.step("Test 'Solutions' menu > 'About Us': text + href"):
			self.assertEqual(BasePageContent.LEFT_MENU_ITEMS['About Us']['href'],
			                 self.page.about_us_menu_item_formated_href)
			self.assertEqual(BasePageContent.LEFT_MENU_ITEMS['About Us']['text'],
			                 self.page.about_us_menu_item_text)
		'''

		step_definition(self,
		                expected=self.config.base_url + BasePageContent.LEFT_MENU_ITEMS['Services']['href'],
		                actual=self.page.services_us_menu_item_formated_href,
		                step_description="Test 'Solutions' menu > 'Services': href")

		step_definition(self,
		                expected=BasePageContent.LEFT_MENU_ITEMS['Services']['text'],
		                actual=self.page.services_us_menu_item_text,
		                step_description="Test 'Solutions' menu > 'Services': text")

		'''
		with allure.step("Test 'Solutions' menu > 'Services': text + href"):
			self.assertEqual(BasePageContent.LEFT_MENU_ITEMS['Services']['href'],
			                 self.page.services_us_menu_item_formated_href)
			self.assertEqual(BasePageContent.LEFT_MENU_ITEMS['Services']['text'],
			                 self.page.services_us_menu_item_text)
		'''

		step_definition(self,
		                expected=BasePageContent.LEFT_MENU_ITEMS['Products']['href'],
		                actual=self.page.products_menu_item_formated_href,
		                step_description="Test 'Solutions' menu > 'Products': href")

		step_definition(self,
		                expected=BasePageContent.LEFT_MENU_ITEMS['Products']['text'],
		                actual=self.page.products_menu_item_text,
		                step_description="Test 'Solutions' menu > 'Products': text")

		'''
		with allure.step("Test 'Solutions' menu > 'Products': text + href"):
			self.assertEqual(BasePageContent.LEFT_MENU_ITEMS['Products']['href'],
			                 self.page.products_menu_item_formated_href)
			self.assertEqual(BasePageContent.LEFT_MENU_ITEMS['Products']['text'],
			                 self.page.products_menu_item_text)
		'''

		step_definition(self,
		                expected=BasePageContent.LEFT_MENU_ITEMS['Locations']['href'],
		                actual=self.page.locations_menu_item_formated_href,
		                step_description="Test 'Solutions' menu > 'Locations': href")

		step_definition(self,
		                expected=BasePageContent.LEFT_MENU_ITEMS['Locations']['text'],
		                actual=self.page.locations_menu_item_text,
		                step_description="Test 'Solutions' menu > 'Locations': text")

		'''
		with allure.step("Test 'Solutions' menu > 'Locations': text + href"):
			self.assertEqual(BasePageContent.LEFT_MENU_ITEMS['Locations']['href'],
			                 self.page.locations_menu_item_formated_href)
			self.assertEqual(BasePageContent.LEFT_MENU_ITEMS['Locations']['text'],
			                 self.page.locations_menu_item_text)
		'''

		step_definition(self,
		                expected=self.config.base_url + BasePageContent.LEFT_MENU_ITEMS['Admin Page']['href'],
		                actual=self.page.admin_page_menu_item_formated_href,
		                step_description="Test 'Solutions' menu > 'Admin Page': href")

		step_definition(self,
		                expected=BasePageContent.LEFT_MENU_ITEMS['Admin Page']['text'],
		                actual=self.page.admin_page_menu_item_text,
		                step_description="Test 'Solutions' menu > 'Admin Page': text")

		'''
		with allure.step("Test 'Solutions' menu > 'Admin Page': text + href"):
			self.assertEqual(BasePageContent.LEFT_MENU_ITEMS['Admin Page']['href'],
			                 self.page.admin_page_menu_item_formated_href)
			self.assertEqual(BasePageContent.LEFT_MENU_ITEMS['Admin Page']['text'],
			                 self.page.admin_page_menu_item_text)
		'''

	def verify_right_menu_home_button(self):
		allure.dynamic.severity(allure.severity_level.MINOR)

		step_definition(self,
		                expected=self.config.base_url + BasePageContent.MENU_BUTTONS['home']['href'],
		                actual=self.page.home_button_formated_href,
		                act=None,
		                step_description='Do "Home" button verification > verify button href')
		'''
		with allure.step('Do "Home" button verification > verify button href. Expected: {}.'.format(
				BasePageContent.MENU_BUTTONS['home']['href'])):
			self.assertEqual(BasePageContent.MENU_BUTTONS['home']['href'],
			                 self.page.home_button_formated_href)
		'''

		step_definition(self,
		                expected=BasePageContent.MENU_BUTTONS['home']['text'],
		                actual=self.page.home_button_text,
		                act=None,
		                step_description='Do "Home" button verification > verify button label')
		'''
		with allure.step('Do "Home" button verification > verify button label. Expected: {}.'.format(
				BasePageContent.MENU_BUTTONS['home']['text'])):
			self.assertEqual(BasePageContent.MENU_BUTTONS['home']['text'],
			                 self.page.home_button_text)
		'''

	def verify_right_menu_about_button(self):
		allure.dynamic.severity(allure.severity_level.MINOR)

		step_definition(self,
		                expected=self.config.base_url + BasePageContent.MENU_BUTTONS['about']['href'],
		                actual=self.page.about_button_formated_href,
		                act=None,
		                step_description='Do "About" button verification > verify button href')
		'''
		with allure.step('Do "About" button verification > verify button href. Expected: {}.'.format(
				BasePageContent.MENU_BUTTONS['about']['href'])):
			self.assertEqual(BasePageContent.MENU_BUTTONS['about']['href'],
			                 self.page.about_button_formated_href)
		'''

		step_definition(self,
		                expected=BasePageContent.MENU_BUTTONS['about']['text'],
		                actual=self.page.about_button_text,
		                act=None,
		                step_description='Do "About" button verification > verify button label')
		'''
		with allure.step('Do "About" button verification > verify button label. Expected: {}.'.format(
				BasePageContent.MENU_BUTTONS['about']['text'])):
			self.assertEqual(BasePageContent.MENU_BUTTONS['about']['text'],
			                 self.page.about_button_text)
		'''

	def verify_right_menu_contact_button(self):
		allure.dynamic.severity(allure.severity_level.MINOR)

		step_definition(self,
		                expected=self.config.base_url + BasePageContent.MENU_BUTTONS['contact']['href'],
		                actual=self.page.contact_button_formated_href,
		                act=None,
		                step_description='Do "Contact" button verification > verify button href')
		'''
		with allure.step('Do "Contact" button verification > verify button href. Expected: {}.'.format(
				BasePageContent.MENU_BUTTONS['contact']['href'])):
			self.assertEqual(BasePageContent.MENU_BUTTONS['contact']['href'],
			                 self.page.contact_button_formated_href)
		'''

		step_definition(self,
		                expected=BasePageContent.MENU_BUTTONS['contact']['text'],
		                actual=self.page.contact_button_text,
		                act=None,
		                step_description='Do "Contact" button verification > verify button label')
		'''
		with allure.step('Do "Contact" button verification > verify button label. Expected: {}.'.format(
				BasePageContent.MENU_BUTTONS['contact']['text'])):
			self.assertEqual(BasePageContent.MENU_BUTTONS['contact']['text'],
			                 self.page.contact_button_text)
		'''

	def verify_parabank_logo(self):
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		step_definition(self,
		                expected=BasePageContent.SLOGAN,
		                actual=self.page.slogan,
		                act=None,
		                step_description="Test 'ParaBank' logo > slogan")
		'''
		with allure.step("Test 'ParaBank' logo > slogan"):
			self.assertEqual(BasePageContent.SLOGAN,
			                 self.page.slogan)
		'''

		step_definition(self,
		                expected=self.config.base_url + BasePageContent.PARA_BANK_LOGO['href'],
		                actual=self.page.para_bank_logo_formated_href,
		                act=None,
		                step_description="Test 'ParaBank' logo > href")
		'''
		with allure.step("Test 'ParaBank' logo > href"):
			self.assertEqual(BasePageContent.PARA_BANK_LOGO['href'],
			                 self.page.para_bank_logo_formated_href)
		'''

		step_definition(self,
		                expected=BasePageContent.PARA_BANK_LOGO['class'],
		                actual=self.page.para_bank_logo_img_class,
		                act=None,
		                step_description="Test 'ParaBank' logo > class")
		'''
		with allure.step("Test 'ParaBank' logo > class"):
			self.assertEqual(BasePageContent.PARA_BANK_LOGO['class'],
			                 self.page.para_bank_logo_img_class)
		'''

		step_definition(self,
		                expected=self.config.base_url + BasePageContent.PARA_BANK_LOGO['src'],
		                actual=self.page.para_bank_logo_formated_img_src,
		                act=None,
		                step_description="Test 'ParaBank' logo > src")
		'''
		with allure.step("Test 'ParaBank' logo > src"):
			self.assertEqual(BasePageContent.PARA_BANK_LOGO['src'],
			                 self.page.para_bank_logo_formated_img_src)
		'''

		step_definition(self,
		                expected=BasePageContent.PARA_BANK_LOGO['alt'],
		                actual=self.page.para_bank_logo_img_alt,
		                act=None,
		                step_description="Test 'ParaBank' logo > alt")
		'''
		with allure.step("Test 'ParaBank' logo > alt"):
			self.assertEqual(BasePageContent.PARA_BANK_LOGO['alt'],
			                 self.page.para_bank_logo_img_alt)
		'''

		step_definition(self,
		                expected=BasePageContent.PARA_BANK_LOGO['title'],
		                actual=self.page.para_bank_logo_img_title,
		                act=None,
		                step_description="Test 'ParaBank' logo > title")
		'''
		with allure.step("Test 'ParaBank' logo > title"):
			self.assertEqual(BasePageContent.PARA_BANK_LOGO['title'],
			                 self.page.para_bank_logo_img_title)
		'''

	def verify_parabank_admin_logo(self):
		allure.dynamic.severity(allure.severity_level.MINOR)

		step_definition(self,
		                expected=self.config.base_url + BasePageContent.ADMIN_LOGO['href'],
		                actual=self.page.admin_logo_formated_href,
		                act=None,
		                step_description="Test 'Admin' logo > href")
		'''
		with allure.step("Test 'Admin' logo > href"):
			self.assertEqual(BasePageContent.ADMIN_LOGO['href'],
			                 self.page.admin_logo_formated_href)
		'''

		step_definition(self,
		                expected=BasePageContent.ADMIN_LOGO['class'],
		                actual=self.page.admin_logo_img_class,
		                act=None,
		                step_description="Test 'Admin' logo > class")
		'''
		with allure.step("Test 'Admin' logo > class"):
			self.assertEqual(BasePageContent.ADMIN_LOGO['class'],
			                 self.page.admin_logo_img_class)
		'''

		step_definition(self,
		                expected=self.config.base_url + BasePageContent.ADMIN_LOGO['src'],
		                actual=self.page.admin_logo_formated_img_src,
		                act=None,
		                step_description="Test 'Admin' logo > src")
		'''
		with allure.step("Test 'Admin' logo > src"):
			self.assertEqual(BasePageContent.ADMIN_LOGO['src'],
			                 self.page.admin_logo_formated_img_src)
		'''

	def verify_customer_login(self):
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# Title:
		step_definition(self,
		                expected=BasePageContent.CUSTOMER_LOGIN['login title'],
		                actual=self.page.customer_login_title,
		                act=None,
		                step_description="Test 'Customer Login' logo > title")
		'''
		with allure.step("Test 'Customer Login' logo > title"):
			self.assertEqual(BasePageContent.CUSTOMER_LOGIN['login title'],
			                 self.page.customer_login_title)
		'''

		# Username:
		step_definition(self,
		                expected=BasePageContent.CUSTOMER_LOGIN['username title'],
		                actual=self.page.username_login_title,
		                act=None,
		                step_description="Test 'Customer Login' > Username title > title")
		'''
		with allure.step("Test 'Customer Login' > Username title > title"):
			self.assertEqual(BasePageContent.CUSTOMER_LOGIN['username title'],
			                 self.page.username_login_title)
		'''

		step_definition(self,
		                expected=BasePageContent.CUSTOMER_LOGIN['username input']['class'],
		                actual=self.page.username_input_class,
		                act=None,
		                step_description="Test 'Customer Login' logo > Username field > class")
		'''
		with allure.step("Test 'Customer Login' logo > Username field > class"):
			self.assertEqual(BasePageContent.CUSTOMER_LOGIN['username input']['class'],
			                 self.page.username_input_class)
		'''

		step_definition(self,
		                expected=BasePageContent.CUSTOMER_LOGIN['username input']['type'],
		                actual=self.page.username_input_type,
		                act=None,
		                step_description="Test 'Customer Login' logo > Username field > type")
		'''
		with allure.step("Test 'Customer Login' logo > Username field > type"):
			self.assertEqual(BasePageContent.CUSTOMER_LOGIN['username input']['type'],
			                 self.page.username_input_type)
		'''

		step_definition(self,
		                expected=BasePageContent.CUSTOMER_LOGIN['username input']['name'],
		                actual=self.page.username_input_name,
		                act=None,
		                step_description="Test 'Customer Login' logo > Username field > name")
		'''
		with allure.step("Test 'Customer Login' logo > Username field > name"):
			self.assertEqual(BasePageContent.CUSTOMER_LOGIN['username input']['name'],
			                 self.page.username_input_name)
		'''

		# Password:
		step_definition(self,
		                expected=BasePageContent.CUSTOMER_LOGIN['password title'],
		                actual=self.page.password_login_title,
		                act=None,
		                step_description="Test 'Customer Login' > Password title > title")
		'''
		with allure.step("Test 'Customer Login' > Password title > title"):
			self.assertEqual(BasePageContent.CUSTOMER_LOGIN['password title'],
			                 self.page.password_login_title)
		'''

		step_definition(self,
		                expected=BasePageContent.CUSTOMER_LOGIN['password input']['class'],
		                actual=self.page.password_input_class,
		                act=None,
		                step_description="Test 'Customer Login' > Password field > class")
		'''
		with allure.step("Test 'Customer Login' > Password field > class"):
			self.assertEqual(BasePageContent.CUSTOMER_LOGIN['password input']['class'],
			                 self.page.password_input_class)
		'''

		step_definition(self,
		                expected=BasePageContent.CUSTOMER_LOGIN['password input']['type'],
		                actual=self.page.password_input_type,
		                act=None,
		                step_description="Test 'Customer Login' > Password field > type")
		'''
		with allure.step("Test 'Customer Login' > Password field > type"):
			self.assertEqual(BasePageContent.CUSTOMER_LOGIN['password input']['type'],
			                 self.page.password_input_type)
		'''

		step_definition(self,
		                expected=BasePageContent.CUSTOMER_LOGIN['password input']['name'],
		                actual=self.page.password_input_name,
		                act=None,
		                step_description="Test 'Customer Login' > Password field > name")
		'''
		with allure.step("Test 'Customer Login' > Password field > name"):
			self.assertEqual(BasePageContent.CUSTOMER_LOGIN['password input']['name'],
			                 self.page.password_input_name)
		'''

		# Login Button
		step_definition(self,
		                expected=BasePageContent.CUSTOMER_LOGIN['login button']['class'],
		                actual=self.page.login_button_class,
		                act=None,
		                step_description="Test 'Customer Login' > Login button > class")
		'''
		with allure.step("Test 'Customer Login' > Login button > class"):
			self.assertEqual(BasePageContent.CUSTOMER_LOGIN['login button']['class'],
			                 self.page.login_button_class)
		'''

		step_definition(self,
		                expected=BasePageContent.CUSTOMER_LOGIN['login button']['type'],
		                actual=self.page.login_button_type,
		                act=None,
		                step_description="Test 'Customer Login' > Login button > class")
		'''
		with allure.step("Test 'Customer Login' > Login button > class"):
			self.assertEqual(BasePageContent.CUSTOMER_LOGIN['login button']['type'],
			                 self.page.login_button_type)
		'''

		step_definition(self,
		                expected=BasePageContent.CUSTOMER_LOGIN['login button']['value'],
		                actual=self.page.login_button_value,
		                act=None,
		                step_description="Test 'Customer Login' > Login button > class")
		'''
		with allure.step("Test 'Customer Login' > Login button > class"):
			self.assertEqual(BasePageContent.CUSTOMER_LOGIN['login button']['value'],
			                 self.page.login_button_value)
		'''

		# Forgot Login
		step_definition(self,
		                expected=self.config.base_url + BasePageContent.FORGOT_LOGIN['href'],
		                actual=self.page.forgot_login_formated_href,
		                act=None,
		                step_description="Test 'Customer Login' > Forgot Login > href")
		'''
		with allure.step("Test 'Customer Login' > Forgot Login > href"):
			self.assertEqual(BasePageContent.FORGOT_LOGIN['href'],
			                 self.page.forgot_login_formated_href)
		'''

		step_definition(self,
		                expected=BasePageContent.FORGOT_LOGIN['text'],
		                actual=self.page.forgot_login_text,
		                act=None,
		                step_description="Test 'Customer Login' > Forgot Login > text")
		'''
		with allure.step("Test 'Customer Login' > Forgot Login > text"):
			self.assertEqual(BasePageContent.FORGOT_LOGIN['text'],
			                 self.page.forgot_login_text)
		'''

		# Register
		step_definition(self,
		                expected=self.config.base_url + BasePageContent.REGISTER['href'],
		                actual=self.page.register_formated_href,
		                act=None,
		                step_description="Test 'Customer Login' > Register > href")
		'''
		with allure.step("Test 'Customer Login' > Register > href"):
			self.assertEqual(BasePageContent.REGISTER['href'],
			                 self.page.register_formated_href)
		'''

		step_definition(self,
		                expected=BasePageContent.REGISTER['text'],
		                actual=self.page.register_text,
		                act=None,
		                step_description="Test 'Customer Login' > Register > text")
		'''
		with allure.step("Test 'Customer Login' > Register > text"):
			self.assertEqual(BasePageContent.REGISTER['text'],
			                 self.page.register_text)
		'''

	def verify_footer_home_item(self):

		allure.dynamic.severity(allure.severity_level.MINOR)

		# 'Home' > href
		step_definition(self,
		                expected=self.config.base_url + BasePageContent.FOOTER['footer menu']['home']['href'],
		                actual=self.page.footer_home_formated_href,
		                act=None,
		                step_description="Test 'Footer' items > 'Home' > href")
		'''
		with allure.step("Test 'Footer' items > 'Home' > href"):
			expected = BasePageContent.FOOTER['footer menu']['home']['href']
			actual = self.page.footer_home_formated_href
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('\'Home\' > href', expected, actual))
			self.assertEqual(expected, actual)
		'''

		# 'Home' > text
		step_definition(self,
		                expected=BasePageContent.FOOTER['footer menu']['home']['text'],
		                actual=self.page.footer_home_text,
		                act=None,
		                step_description="Test 'Footer' items > 'Home' > text")
		'''
		with allure.step("Test 'Footer' items > 'Home' > text"):
			expected = BasePageContent.FOOTER['footer menu']['home']['text']
			actual = self.page.footer_home_text
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('\'Home\' > text', expected, actual))
			self.assertEqual(expected, actual)
		'''

	def verify_footer_about_item(self):
		allure.dynamic.severity(allure.severity_level.MINOR)

		# About Us
		step_definition(self,
		                expected=self.config.base_url + BasePageContent.FOOTER['footer menu']['about us']['href'],
		                actual=self.page.footer_about_us_formated_href,
		                act=None,
		                step_description="Test 'Footer' items > 'About Us' > href")
		'''
		with allure.step("Test 'Footer' items > 'About Us' > href"):
			self.assertEqual(BasePageContent.FOOTER['footer menu']['about us']['href'],
			                 self.page.footer_about_us_formated_href)
		'''

		step_definition(self,
		                expected=BasePageContent.FOOTER['footer menu']['about us']['text'],
		                actual=self.page.footer_about_us_text,
		                act=None,
		                step_description="Test 'Footer' items > 'About Us' > text")
		'''
		with allure.step("Test 'Footer' items > 'About Us' > text"):
			self.assertEqual(BasePageContent.FOOTER['footer menu']['about us']['text'],
			                 self.page.footer_about_us_text)
		'''

	def verify_footer_services_item(self):
		allure.dynamic.severity(allure.severity_level.MINOR)

		# Services
		step_definition(self,
		                expected=self.config.base_url + BasePageContent.FOOTER['footer menu']['services']['href'],
		                actual=self.page.footer_services_formated_href,
		                act=None,
		                step_description="Test 'Footer' items > 'Services' > href")
		'''
		with allure.step("Test 'Footer' items > 'Services' > href"):
			self.assertEqual(BasePageContent.FOOTER['footer menu']['services']['href'],
			                 self.page.footer_services_formated_href)
		'''

		step_definition(self,
		                expected=BasePageContent.FOOTER['footer menu']['services']['text'],
		                actual=self.page.footer_services_text,
		                act=None,
		                step_description="Test 'Footer' items > 'Services' > text")
		'''
		with allure.step("Test 'Footer' items > 'Services' > text"):
			self.assertEqual(BasePageContent.FOOTER['footer menu']['services']['text'],
			                 self.page.footer_services_text)
		'''

	def verify_footer_products_item(self):
		allure.dynamic.severity(allure.severity_level.MINOR)

		# Products
		step_definition(self,
		                expected=BasePageContent.FOOTER['footer menu']['products']['href'],
		                actual=self.page.footer_products_formated_href,
		                act=None,
		                step_description="Test 'Footer' items > 'Products' > href")
		'''
		with allure.step("Test 'Footer' items > 'Products' > href"):
			self.assertEqual(BasePageContent.FOOTER['footer menu']['products']['href'],
			                 self.page.footer_products_formated_href)
		'''

		step_definition(self,
		                expected=BasePageContent.FOOTER['footer menu']['products']['text'],
		                actual=self.page.footer_products_text,
		                act=None,
		                step_description="Test 'Footer' items > 'Products' > text")
		'''
		with allure.step("Test 'Footer' items > 'Products' > text"):
			self.assertEqual(BasePageContent.FOOTER['footer menu']['products']['text'],
			                 self.page.footer_products_text)
		'''

	def verify_footer_locations_item(self):
		allure.dynamic.severity(allure.severity_level.MINOR)

		# Locations
		step_definition(self,
		                expected=BasePageContent.FOOTER['footer menu']['locations']['href'],
		                actual=self.page.footer_locations_formated_href,
		                act=None,
		                step_description="Test 'Footer' items > 'Locations' > href")
		'''
		with allure.step("Test 'Footer' items > 'Locations' > href"):
			self.assertEqual(BasePageContent.FOOTER['footer menu']['locations']['href'],
			                 self.page.footer_locations_formated_href)
		'''

		step_definition(self,
		                expected=BasePageContent.FOOTER['footer menu']['locations']['text'],
		                actual=self.page.footer_locations_text,
		                act=None,
		                step_description="Test 'Footer' items > 'Locations' > text")
		'''
		with allure.step("Test 'Footer' items > 'Locations' > text"):
			self.assertEqual(BasePageContent.FOOTER['footer menu']['locations']['text'],
			                 self.page.footer_locations_text)
		'''

	def verify_footer_forum_item(self):
		allure.dynamic.severity(allure.severity_level.MINOR)

		# Forum
		step_definition(self,
		                expected=BasePageContent.FOOTER['footer menu']['forum']['href'],
		                actual=self.page.footer_forum_formated_href,
		                act=None,
		                step_description="Test 'Footer' items > 'Forum' > href")
		'''
		with allure.step("Test 'Footer' items > 'Forum' > href"):
			self.assertEqual(BasePageContent.FOOTER['footer menu']['forum']['href'],
			                 self.page.footer_forum_formated_href)
		'''

		step_definition(self,
		                expected=BasePageContent.FOOTER['footer menu']['forum']['text'],
		                actual=self.page.footer_forum_text,
		                act=None,
		                step_description="Test 'Footer' items > 'Forum' > text")
		'''
		with allure.step("Test 'Footer' items > 'Forum' > text"):
			self.assertEqual(BasePageContent.FOOTER['footer menu']['forum']['text'],
			                 self.page.footer_forum_text)
		'''

	def verify_footer_site_map_item(self):
		allure.dynamic.severity(allure.severity_level.MINOR)

		# Site Map
		step_definition(self,
		                expected=self.config.base_url + BasePageContent.FOOTER['footer menu']['site map']['href'],
		                actual=self.page.footer_site_map_formated_href,
		                act=None,
		                step_description="Test 'Footer' items > 'Site Map' > href")
		'''
		with allure.step("Test 'Footer' items > 'Site Map' > href"):
			self.assertEqual(BasePageContent.FOOTER['footer menu']['site map']['href'],
			                 self.page.footer_site_map_formated_href)
		'''

		step_definition(self,
		                expected=BasePageContent.FOOTER['footer menu']['site map']['text'],
		                actual=self.page.footer_site_map_text,
		                act=None,
		                step_description="Test 'Footer' items > 'Site Map' > text")
		'''
		with allure.step("Test 'Footer' items > 'Site Map' > text"):
			self.assertEqual(BasePageContent.FOOTER['footer menu']['site map']['text'],
			                 self.page.footer_site_map_text)
		'''

	def verify_footer_contact_us_item(self):
		allure.dynamic.severity(allure.severity_level.MINOR)

		# Contact Us
		step_definition(self,
		                expected=self.config.base_url + BasePageContent.FOOTER['footer menu']['contact us']['href'],
		                actual=self.page.footer_contact_us_formated_href,
		                act=None,
		                step_description="Test 'Footer' items > 'Contact Us' > href")
		'''
		with allure.step("Test 'Footer' items > 'Contact Us' > href"):
			self.assertEqual(BasePageContent.FOOTER['footer menu']['contact us']['href'],
			                 self.page.footer_contact_us_formated_href)
		'''

		step_definition(self,
		                expected=BasePageContent.FOOTER['footer menu']['contact us']['text'],
		                actual=self.page.footer_contact_us_text,
		                act=None,
		                step_description="Test 'Footer' items > 'Contact Us' > text")
		'''
		with allure.step("Test 'Footer' items > 'Contact Us' > text"):
			self.assertEqual(BasePageContent.FOOTER['footer menu']['contact us']['text'],
			                 self.page.footer_contact_us_text)
		'''

	def verify_footer_copyright_item(self):
		allure.dynamic.severity(allure.severity_level.MINOR)

		# Copyright
		step_definition(self,
		                expected=BasePageContent.FOOTER['copyright']['class'],
		                actual=self.page.footer_copyright_class,
		                act=None,
		                step_description="Test 'Footer' items > 'Copyright' > class")
		'''
		with allure.step("Test 'Footer' items > 'Copyright' > class"):
			self.assertEqual(BasePageContent.FOOTER['copyright']['class'],
			                 self.page.footer_copyright_class)
		'''

		step_definition(self,
		                expected=BasePageContent.FOOTER['copyright']['text'],
		                actual=self.page.footer_copyright_text,
		                act=None,
		                step_description="Test 'Footer' items > 'Copyright' > text")
		'''
		with allure.step("Test 'Footer' items > 'Copyright' > text"):
			self.assertEqual(BasePageContent.FOOTER['copyright']['text'],
			                 self.page.footer_copyright_text)
		'''

	def verify_footer_visit_item(self):
		allure.dynamic.severity(allure.severity_level.MINOR)

		# Visit
		step_definition(self,
		                expected=BasePageContent.FOOTER['visit']['link']['href'],
		                actual=self.page.footer_visit_link_formated_href,
		                act=None,
		                step_description="Test 'Footer' items > 'Visit' > link > href")
		'''
		with allure.step("Test 'Footer' items > 'Visit' > link > href"):
			self.assertEqual(BasePageContent.FOOTER['visit']['link']['href'],
			                 self.page.footer_visit_link_formated_href)
		'''

		step_definition(self,
		                expected=BasePageContent.FOOTER['visit']['link']['text'],
		                actual=self.page.footer_visit_link_text,
		                act=None,
		                step_description="Test 'Footer' items > 'Visit' > link > text")
		'''
		with allure.step("Test 'Footer' items > 'Visit' > link > text"):
			self.assertEqual(BasePageContent.FOOTER['visit']['link']['text'],
			                 self.page.footer_visit_link_text)
		'''

		step_definition(self,
		                expected=BasePageContent.FOOTER['visit']['link']['target'],
		                actual=self.page.footer_visit_link_target,
		                act=None,
		                step_description="Test 'Footer' items > 'Visit' > link > target")
		'''
		with allure.step("Test 'Footer' items > 'Visit' > link > target"):
			self.assertEqual(BasePageContent.FOOTER['visit']['link']['target'],
			                 self.page.footer_visit_link_target)
		'''

		step_definition(self,
		                expected=BasePageContent.FOOTER['visit']['text'],
		                actual=self.page.footer_visit_us_text,
		                act=None,
		                step_description="Test 'Footer' items > 'Visit' > text")
		'''
		with allure.step("Test 'Footer' items > 'Visit' > text"):
			self.assertEqual(BasePageContent.FOOTER['visit']['text'],
			                 self.page.footer_visit_us_text)
		'''
