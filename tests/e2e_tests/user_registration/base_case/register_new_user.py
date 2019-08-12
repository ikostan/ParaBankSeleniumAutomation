#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_locators.register_page_locator import RegisterPageLocator
from expected_results.page_content.register_page_content import RegisterPageContent
from expected_results.page_content.home_page_content import HomePageContent


class UserRegistrationCase(unittest.TestCase):

	def register_new_user(self):

		with allure.step('Type first name'):
			expected = self.client.FIRST_NAME
			self.page.type_first_name(expected)
			actual = self.page.first_name
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('\'Type first name\'',
			                                                    expected,
			                                                    actual))
			with allure.step('Verify "First Name" field value'):
				self.assertEqual(expected,
				                 actual,
				                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
				                                                                                    actual))

		with allure.step('Type last name'):
			expected = self.client.LAST_NAME
			self.page.type_last_name(expected)
			actual = self.page.last_name
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('\'Type last name\'',
			                                                    expected,
			                                                    actual))
			with allure.step('Verify "Last Name" field value'):
				self.assertEqual(expected,
				                 actual,
				                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
				                                                                                    actual))

		with allure.step('Type address'):
			expected = self.client.ADDRESS
			self.page.type_address(expected)
			actual = self.page.address
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('\'Type address\'',
			                                                    expected,
			                                                    actual))
			with allure.step('Verify "Address" field value'):
				self.assertEqual(expected,
				                 actual,
				                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
				                                                                                    actual))

		with allure.step('Type city'):
			expected = self.client.CITY
			self.page.type_city(expected)
			actual = self.page.city
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('\'Type city\'',
			                                                    expected,
			                                                    actual))
			with allure.step('Verify "City" field value'):
				self.assertEqual(expected,
				                 actual,
				                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
				                                                                                    actual))

		with allure.step('Type state'):
			expected = self.client.STATE
			self.page.type_state(expected)
			actual = self.page.state
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('\'Type state\'',
			                                                    expected,
			                                                    actual))
			with allure.step('Verify "State" field value'):
				self.assertEqual(expected,
				                 actual,
				                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
				                                                                                    actual))

		with allure.step('Type zip code'):
			expected = self.client.ZIP_CODE
			self.page.type_zip_code(expected)
			actual = self.page.zip_code
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('\'Type zip code\'',
			                                                    expected,
			                                                    actual))
			with allure.step('Verify "Zip Code" field value'):
				self.assertEqual(expected,
				                 actual,
				                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
				                                                                                    actual))

		with allure.step('Type phone'):
			expected = self.client.PHONE
			self.page.type_phone(expected)
			actual = self.page.phone
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('\'Type phone\'',
			                                                    expected,
			                                                    actual))
			with allure.step('Verify "Phone" field value'):
				self.assertEqual(expected,
				                 actual,
				                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
				                                                                                    actual))
		with allure.step('Type SSN'):
			expected = self.client.SSN
			self.page.type_ssn(expected)
			actual = self.page.ssn
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('\'Type SSN\'',
			                                                    expected,
			                                                    actual))
			with allure.step('Verify "SSN" field value'):
				self.assertEqual(expected,
				                 actual,
				                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
				                                                                                    actual))

		with allure.step('Type username'):
			expected = self.client.USERNAME
			self.page.type_username(expected)
			actual = self.page.username
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('\'Type username\'',
			                                                    expected,
			                                                    actual))
			with allure.step('Verify "Username" field value'):
				self.assertEqual(expected,
				                 actual,
				                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
				                                                                                    actual))

		with allure.step('Type password'):
			expected = self.client.PASSWORD
			self.page.type_password(expected)
			actual = self.page.password
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('\'Type password\'',
			                                                    expected,
			                                                    actual))
			with allure.step('Verify "Password" field value'):
				self.assertEqual(expected,
				                 actual,
				                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
				                                                                                    actual))

		with allure.step('Type confirm'):
			expected = self.client.PASSWORD
			self.page.type_confirm(expected)
			actual = self.page.confirm
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('\'Type confirm\'',
			                                                    expected,
			                                                    actual))
			with allure.step('Verify "Confirm" field value'):
				self.assertEqual(expected,
				                 actual,
				                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
				                                                                                    actual))

		with allure.step('Hit "Register" button'):
			print('Hit "Register" button')
			self.page.click_register_btn()

		with allure.step('Wait for "Welcome" message'):
			WebDriverWait(self.page.driver,
			              self.page.explicit_wait_time).until(EC.presence_of_element_located(RegisterPageLocator.HEADER))

		with allure.step('Verify "Welcome" header'):
			expected = RegisterPageContent.WELCOME_MESSAGE['header'] + self.client.USERNAME
			actual = self.page.welcome_header
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('\'Verify "Welcome" header\'',
			                                                    expected,
			                                                    actual))
			self.assertEqual(expected,
			                 actual,
			                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
			                                                                                    actual))

		with allure.step('Verify "Welcome" message'):
			expected = RegisterPageContent.WELCOME_MESSAGE['message']
			actual = self.page.welcome_message
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('\'Verify "Welcome" header\'',
			                                                    expected,
			                                                    actual))
			self.assertEqual(expected,
			                 actual,
			                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
			                                                                                    actual))

		with allure.step('Verify that "Account Services" menu is present'):
			expected = True
			actual = self.page.account_services_menu_is_visible
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('"Account Services" menu is present',
			                                                    expected,
			                                                    actual))
			self.assertEqual(expected,
			                 actual,
			                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
			                                                                                    actual))
		# Logout
		with allure.step('Hit "Log Out" link'):
			print('Hit "Log Out" link')
			self.page.log_out()
			WebDriverWait(self.page.driver, self.page.explicit_wait_time).until(EC.url_contains('index.htm'))

		# Post Logout validation
		with allure.step('Verify URL'):
			expected = HomePageContent.URL
			actual = self.page.url
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('\'Verify URL\'',
			                                                    expected,
			                                                    actual))
			self.assertEqual(expected,
			                 actual,
			                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
			                                                                                    actual))

		with allure.step('Verify that "Account Services" menu is not present'):
			expected = False
			actual = self.page.account_services_menu_is_visible
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('"Account Services" menu is not present',
			                                                    expected,
			                                                    actual))
			self.assertEqual(expected,
			                 actual,
			                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
			                                                                                    actual))
