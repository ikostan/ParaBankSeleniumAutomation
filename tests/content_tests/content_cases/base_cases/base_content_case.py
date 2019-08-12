#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
import unittest
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

		with allure.step("Test 'Solutions' menu title: text + css"):
			self.assertEqual(BasePageContent.LEFT_MENU_ITEMS['Solutions']['text'],
			                 self.page.solutions_menu_text)

			self.assertEqual(BasePageContent.LEFT_MENU_ITEMS['Solutions']['class'],
			                 self.page.solutions_menu_class)

		with allure.step("Test 'Solutions' menu > 'About Us': text + href"):
			self.assertEqual(BasePageContent.LEFT_MENU_ITEMS['About Us']['href'],
			                 self.page.about_us_menu_item_formated_href)
			self.assertEqual(BasePageContent.LEFT_MENU_ITEMS['About Us']['text'],
			                 self.page.about_us_menu_item_text)

		with allure.step("Test 'Solutions' menu > 'Services': text + href"):
			self.assertEqual(BasePageContent.LEFT_MENU_ITEMS['Services']['href'],
			                 self.page.services_us_menu_item_formated_href)
			self.assertEqual(BasePageContent.LEFT_MENU_ITEMS['Services']['text'],
			                 self.page.services_us_menu_item_text)

		with allure.step("Test 'Solutions' menu > 'Products': text + href"):
			self.assertEqual(BasePageContent.LEFT_MENU_ITEMS['Products']['href'],
			                 self.page.products_menu_item_formated_href)
			self.assertEqual(BasePageContent.LEFT_MENU_ITEMS['Products']['text'],
			                 self.page.products_menu_item_text)

		with allure.step("Test 'Solutions' menu > 'Locations': text + href"):
			self.assertEqual(BasePageContent.LEFT_MENU_ITEMS['Locations']['href'],
			                 self.page.locations_menu_item_formated_href)
			self.assertEqual(BasePageContent.LEFT_MENU_ITEMS['Locations']['text'],
			                 self.page.locations_menu_item_text)

		with allure.step("Test 'Solutions' menu > 'Admin Page': text + href"):
			self.assertEqual(BasePageContent.LEFT_MENU_ITEMS['Admin Page']['href'],
			                 self.page.admin_page_menu_item_formated_href)
			self.assertEqual(BasePageContent.LEFT_MENU_ITEMS['Admin Page']['text'],
			                 self.page.admin_page_menu_item_text)

	def verify_right_menu_home_button(self):
		allure.dynamic.severity(allure.severity_level.MINOR)

		with allure.step('Do "Home" button verification > verify button href. Expected: {}.'.format(
				BasePageContent.MENU_BUTTONS['home']['href'])):
			self.assertEqual(BasePageContent.MENU_BUTTONS['home']['href'],
			                 self.page.home_button_formated_href)

		with allure.step('Do "Home" button verification > verify button label. Expected: {}.'.format(
				BasePageContent.MENU_BUTTONS['home']['text'])):
			self.assertEqual(BasePageContent.MENU_BUTTONS['home']['text'],
			                 self.page.home_button_text)

	def verify_right_menu_about_button(self):
		allure.dynamic.severity(allure.severity_level.MINOR)

		with allure.step('Do "About" button verification > verify button href. Expected: {}.'.format(
				BasePageContent.MENU_BUTTONS['about']['href'])):
			self.assertEqual(BasePageContent.MENU_BUTTONS['about']['href'],
			                 self.page.about_button_formated_href)

		with allure.step('Do "About" button verification > verify button label. Expected: {}.'.format(
				BasePageContent.MENU_BUTTONS['about']['text'])):
			self.assertEqual(BasePageContent.MENU_BUTTONS['about']['text'],
			                 self.page.about_button_text)

	def verify_right_menu_contact_button(self):
		allure.dynamic.severity(allure.severity_level.MINOR)

		with allure.step('Do "Contact" button verification > verify button href. Expected: {}.'.format(
				BasePageContent.MENU_BUTTONS['contact']['href'])):
			self.assertEqual(BasePageContent.MENU_BUTTONS['contact']['href'],
			                 self.page.contact_button_formated_href)

		with allure.step('Do "Contact" button verification > verify button href. Expected: {}.'.format(
				BasePageContent.MENU_BUTTONS['contact']['text'])):
			self.assertEqual(BasePageContent.MENU_BUTTONS['contact']['text'],
			                 self.page.contact_button_text)

	def verify_parabank_logo(self):
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		with allure.step("Test 'ParaBank' logo > slogan"):
			self.assertEqual(BasePageContent.SLOGAN,
			                 self.page.slogan)

		with allure.step("Test 'ParaBank' logo > href"):
			self.assertEqual(BasePageContent.PARA_BANK_LOGO['href'],
			                 self.page.para_bank_logo_formated_href)

		with allure.step("Test 'ParaBank' logo > class"):
			self.assertEqual(BasePageContent.PARA_BANK_LOGO['class'],
			                 self.page.para_bank_logo_img_class)

		with allure.step("Test 'ParaBank' logo > src"):
			self.assertEqual(BasePageContent.PARA_BANK_LOGO['src'],
			                 self.page.para_bank_logo_formated_img_src)

		with allure.step("Test 'ParaBank' logo > alt"):
			self.assertEqual(BasePageContent.PARA_BANK_LOGO['alt'],
			                 self.page.para_bank_logo_img_alt)

		with allure.step("Test 'ParaBank' logo > title"):
			self.assertEqual(BasePageContent.PARA_BANK_LOGO['title'],
			                 self.page.para_bank_logo_img_title)

	def verify_parabank_admin_logo(self):
		allure.dynamic.severity(allure.severity_level.MINOR)

		with allure.step("Test 'Admin' logo > href"):
			self.assertEqual(BasePageContent.ADMIN_LOGO['href'],
			                 self.page.admin_logo_formated_href)

		with allure.step("Test 'Admin' logo > class"):
			self.assertEqual(BasePageContent.ADMIN_LOGO['class'],
			                 self.page.admin_logo_img_class)

		with allure.step("Test 'Admin' logo > src"):
			self.assertEqual(BasePageContent.ADMIN_LOGO['src'],
			                 self.page.admin_logo_formated_img_src)

	def verify_customer_login(self):
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# Title:
		with allure.step("Test 'Customer Login' logo > title"):
			self.assertEqual(BasePageContent.CUSTOMER_LOGIN['login title'],
			                 self.page.customer_login_title)

		# Username:
		with allure.step("Test 'Customer Login' > Username title > title"):
			self.assertEqual(BasePageContent.CUSTOMER_LOGIN['username title'],
			                 self.page.username_login_title)
		with allure.step("Test 'Customer Login' logo > Username field > class"):
			self.assertEqual(BasePageContent.CUSTOMER_LOGIN['username input']['class'],
			                 self.page.username_input_class)
		with allure.step("Test 'Customer Login' logo > Username field > type"):
			self.assertEqual(BasePageContent.CUSTOMER_LOGIN['username input']['type'],
			                 self.page.username_input_type)
		with allure.step("Test 'Customer Login' logo > Username field > name"):
			self.assertEqual(BasePageContent.CUSTOMER_LOGIN['username input']['name'],
			                 self.page.username_input_name)

		# Password:
		with allure.step("Test 'Customer Login' > Password title > title"):
			self.assertEqual(BasePageContent.CUSTOMER_LOGIN['password title'],
			                 self.page.password_login_title)
		with allure.step("Test 'Customer Login' > Password field > class"):
			self.assertEqual(BasePageContent.CUSTOMER_LOGIN['password input']['class'],
			                 self.page.password_input_class)
		with allure.step("Test 'Customer Login' > Password field > type"):
			self.assertEqual(BasePageContent.CUSTOMER_LOGIN['password input']['type'],
			                 self.page.password_input_type)
		with allure.step("Test 'Customer Login' > Password field > name"):
			self.assertEqual(BasePageContent.CUSTOMER_LOGIN['password input']['name'],
			                 self.page.password_input_name)

		# Login Button
		with allure.step("Test 'Customer Login' > Login button > class"):
			self.assertEqual(BasePageContent.CUSTOMER_LOGIN['login button']['class'],
			                 self.page.login_button_class)
		with allure.step("Test 'Customer Login' > Login button > class"):
			self.assertEqual(BasePageContent.CUSTOMER_LOGIN['login button']['type'],
			                 self.page.login_button_type)
		with allure.step("Test 'Customer Login' > Login button > class"):
			self.assertEqual(BasePageContent.CUSTOMER_LOGIN['login button']['value'],
			                 self.page.login_button_value)

		# Forgot Login
		with allure.step("Test 'Customer Login' > Forgot Login > href"):
			self.assertEqual(BasePageContent.FORGOT_LOGIN['href'],
			                 self.page.forgot_login_formated_href)
		with allure.step("Test 'Customer Login' > Forgot Login > text"):
			self.assertEqual(BasePageContent.FORGOT_LOGIN['text'],
			                 self.page.forgot_login_text)

		# Register
		with allure.step("Test 'Customer Login' > Register > href"):
			self.assertEqual(BasePageContent.REGISTER['href'],
			                 self.page.register_formated_href)
		with allure.step("Test 'Customer Login' > Register > text"):
			self.assertEqual(BasePageContent.REGISTER['text'],
			                 self.page.register_text)

	def verify_footer_home_item(self):

		allure.dynamic.severity(allure.severity_level.MINOR)

		# 'Home' > href
		with allure.step("Test 'Footer' items > 'Home' > href"):
			expected = BasePageContent.FOOTER['footer menu']['home']['href']
			actual = self.page.footer_home_formated_href
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('\'Home\' > href', expected, actual))
			self.assertEqual(expected, actual)

		# 'Home' > text
		with allure.step("Test 'Footer' items > 'Home' > text"):
			expected = BasePageContent.FOOTER['footer menu']['home']['text']
			actual = self.page.footer_home_text
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('\'Home\' > text', expected, actual))
			self.assertEqual(expected, actual)

		'''
		expected = BasePageContext.FOOTER['footer menu']['home']['href']
		actual = self.page.footer_home_formated_href
		step = "'Home' > href"
		description = "Test 'Footer' items > " + step
		severity = allure.severity_level.MINOR

		assert_equal_step(expected, actual, description, step, severity)
		'''

	def verify_footer_about_item(self):
		allure.dynamic.severity(allure.severity_level.MINOR)

		# About Us
		with allure.step("Test 'Footer' items > 'About Us' > href"):
			self.assertEqual(BasePageContent.FOOTER['footer menu']['about us']['href'],
			                 self.page.footer_about_us_formated_href)

		with allure.step("Test 'Footer' items > 'About Us' > text"):
			self.assertEqual(BasePageContent.FOOTER['footer menu']['about us']['text'],
			                 self.page.footer_about_us_text)

	def verify_footer_services_item(self):
		allure.dynamic.severity(allure.severity_level.MINOR)

		# Services
		with allure.step("Test 'Footer' items > 'Services' > href"):
			self.assertEqual(BasePageContent.FOOTER['footer menu']['services']['href'],
			                 self.page.footer_services_formated_href)

		with allure.step("Test 'Footer' items > 'Services' > text"):
			self.assertEqual(BasePageContent.FOOTER['footer menu']['services']['text'],
			                 self.page.footer_services_text)

	def verify_footer_products_item(self):
		allure.dynamic.severity(allure.severity_level.MINOR)

		# Products
		with allure.step("Test 'Footer' items > 'Products' > href"):
			self.assertEqual(BasePageContent.FOOTER['footer menu']['products']['href'],
			                 self.page.footer_products_formated_href)

		with allure.step("Test 'Footer' items > 'Products' > text"):
			self.assertEqual(BasePageContent.FOOTER['footer menu']['products']['text'],
			                 self.page.footer_products_text)

	def verify_footer_locations_item(self):
		allure.dynamic.severity(allure.severity_level.MINOR)

		# Locations
		with allure.step("Test 'Footer' items > 'Locations' > href"):
			self.assertEqual(BasePageContent.FOOTER['footer menu']['locations']['href'],
			                 self.page.footer_locations_formated_href)

		with allure.step("Test 'Footer' items > 'Locations' > text"):
			self.assertEqual(BasePageContent.FOOTER['footer menu']['locations']['text'],
			                 self.page.footer_locations_text)

	def verify_footer_forum_item(self):
		allure.dynamic.severity(allure.severity_level.MINOR)

		# Forum
		with allure.step("Test 'Footer' items > 'Forum' > href"):
			self.assertEqual(BasePageContent.FOOTER['footer menu']['forum']['href'],
			                 self.page.footer_forum_formated_href)

		with allure.step("Test 'Footer' items > 'Forum' > text"):
			self.assertEqual(BasePageContent.FOOTER['footer menu']['forum']['text'],
			                 self.page.footer_forum_text)

	def verify_footer_site_map_item(self):
		allure.dynamic.severity(allure.severity_level.MINOR)

		# Site Map
		with allure.step("Test 'Footer' items > 'Site Map' > href"):
			self.assertEqual(BasePageContent.FOOTER['footer menu']['site map']['href'],
			                 self.page.footer_site_map_formated_href)

		with allure.step("Test 'Footer' items > 'Site Map' > text"):
			self.assertEqual(BasePageContent.FOOTER['footer menu']['site map']['text'],
			                 self.page.footer_site_map_text)

	def verify_footer_contact_us_item(self):
		allure.dynamic.severity(allure.severity_level.MINOR)

		# Contact Us
		with allure.step("Test 'Footer' items > 'Contact Us' > href"):
			self.assertEqual(BasePageContent.FOOTER['footer menu']['contact us']['href'],
			                 self.page.footer_contact_us_formated_href)

		with allure.step("Test 'Footer' items > 'Contact Us' > text"):
			self.assertEqual(BasePageContent.FOOTER['footer menu']['contact us']['text'],
			                 self.page.footer_contact_us_text)

	def verify_footer_copyright_item(self):
		allure.dynamic.severity(allure.severity_level.MINOR)

		# Copyright
		with allure.step("Test 'Footer' items > 'Copyright' > class"):
			self.assertEqual(BasePageContent.FOOTER['copyright']['class'],
			                 self.page.footer_copyright_class)

		with allure.step("Test 'Footer' items > 'Copyright' > text"):
			self.assertEqual(BasePageContent.FOOTER['copyright']['text'],
			                 self.page.footer_copyright_text)

	def verify_footer_visit_item(self):
		allure.dynamic.severity(allure.severity_level.MINOR)

		# Visit
		with allure.step("Test 'Footer' items > 'Visit' > link > href"):
			self.assertEqual(BasePageContent.FOOTER['visit']['link']['href'],
			                 self.page.footer_visit_link_formated_href)

		with allure.step("Test 'Footer' items > 'Visit' > link > text"):
			self.assertEqual(BasePageContent.FOOTER['visit']['link']['text'],
			                 self.page.footer_visit_link_text)

		with allure.step("Test 'Footer' items > 'Visit' > link > target"):
			self.assertEqual(BasePageContent.FOOTER['visit']['link']['target'],
			                 self.page.footer_visit_link_target)

		with allure.step("Test 'Footer' items > 'Visit' > text"):
			self.assertEqual(BasePageContent.FOOTER['visit']['text'],
			                 self.page.footer_visit_us_text)
