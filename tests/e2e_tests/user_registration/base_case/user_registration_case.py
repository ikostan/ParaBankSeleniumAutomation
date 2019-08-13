#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
import unittest


class UserRegistrationCase(unittest.TestCase):

	def fill_out_user_data(self):

		with allure.step('Type first name'):
			expected = self.client.first_name
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
			expected = self.client.last_name
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
			expected = self.client.address
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
			expected = self.client.city
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
			expected = self.client.state
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
			expected = self.client.zip_code
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
			expected = self.client.phone
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
			expected = self.client.ssn
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
			expected = self.client.username
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
			expected = self.client.password
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
			expected = self.client.password
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

