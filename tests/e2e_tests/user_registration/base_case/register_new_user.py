import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_locators.register_page_locator import RegisterPageLocator
from tests.context_cases.register_page_context_case import RegisterContextCase
from expected_results.page_context.register_page_context import RegisterPageContext


class UserRegistrationCase(RegisterContextCase):

	def register_new_user(self, client):  # TODO: remove browser after done

		with allure.step('Type first name'):
			expected = client.FIRST_NAME
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
			expected = client.LAST_NAME
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
			expected = client.ADDRESS
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
			expected = client.CITY
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
			expected = client.STATE
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
			expected = client.ZIP_CODE
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
			expected = client.PHONE
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
			expected = client.SSN
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
			expected = client.USERNAME
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
			expected = client.PASSWORD
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
			expected = client.PASSWORD
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
			self.page.click_register_btn()

		with allure.step('Wait for "Welcome" message'):
			WebDriverWait(self.page.driver,
			              self.page.explicit_wait_time).until(EC.presence_of_element_located(RegisterPageLocator.HEADER))

		with allure.step('Verify "Welcome" header'):
			expected = RegisterPageContext.WELCOME_MESSAGE['header'] + client.USERNAME
			actual = self.page.welcome_header
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('\'Verify "Welcome" header\'',
			                                                    expected,
			                                                    actual))
			self.assertEqual(expected,
			                 actual,
			                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
			                                                                                    actual))

		with allure.step('Verify "Welcome" message'):
			expected = RegisterPageContext.WELCOME_MESSAGE['message']
			actual = self.page.welcome_message
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('\'Verify "Welcome" header\'',
			                                                    expected,
			                                                    actual))
			self.assertEqual(expected,
			                 actual,
			                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
			                                                                                    actual))




