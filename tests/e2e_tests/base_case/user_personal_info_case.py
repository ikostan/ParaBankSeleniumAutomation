#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
import unittest

from expected_results.page_content.register_page_content import RegisterPageContent
from utils.step_definition import step_definition


class UserPersonalInfoCase(unittest.TestCase):

	def verify_first_name_error(self, expected=RegisterPageContent.FORM['first name']['error']):

		actual = self.page.first_name_error
		step_definition(self,
		                expected=expected,
		                actual=actual,
		                step_description='Verify First Name Error')

	def verify_last_name_error(self, expected=RegisterPageContent.FORM['last name']['error']):

		actual = self.page.last_name_error
		step_definition(self,
		                expected=expected,
		                actual=actual,
		                step_description='Verify Last Name Error')

	def verify_address_error(self, expected=RegisterPageContent.FORM['address']['error']):

		actual = self.page.address_error
		step_definition(self,
		                expected=expected,
		                actual=actual,
		                step_description='Verify Address Error')

	def verify_city_error(self, expected=RegisterPageContent.FORM['city']['error']):

		actual = self.page.city_error
		step_definition(self,
		                expected=expected,
		                actual=actual,
		                step_description='Verify City Error')

	def verify_state_error(self, expected=RegisterPageContent.FORM['state']['error']):

		actual = self.page.state_error
		step_definition(self,
		                expected=expected,
		                actual=actual,
		                step_description='Verify State Error')

	def verify_zip_code_error(self, expected=RegisterPageContent.FORM['zip code']['error']):

		actual = self.page.zip_code_error
		step_definition(self,
		                expected=expected,
		                actual=actual,
		                step_description='Verify Zip Code Error')

	def verify_ssn_error(self, expected=RegisterPageContent.FORM['ssn']['error']):

		actual = self.page.ssn_error
		step_definition(self,
		                expected=expected,
		                actual=actual,
		                step_description='Verify SSN Error')

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

