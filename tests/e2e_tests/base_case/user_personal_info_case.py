#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import unittest

import pytest

from expected_results.page_content.register_page_content import RegisterPageContent
from tests.config import Config
from utils.step_definition import step_definition


class UserPersonalInfoCase(unittest.TestCase):

	@pytest.mark.skipif(Config().base_url == 'https://parabank.parasoft.com',
	                    reason="This is demo test that will have negative effect on Travis CI status")
	def verify_first_name_error(self, expected=RegisterPageContent.FORM['first name']['error']):

		# actual = self.page.first_name_error
		step_definition(self,
		                expected=expected,
		                actual=self.page.first_name_error,
		                step_description='Verify First Name Error')

	@pytest.mark.skipif(Config().base_url == 'https://parabank.parasoft.com',
	                    reason="This is demo test that will have negative effect on Travis CI status")
	def verify_last_name_error(self, expected=RegisterPageContent.FORM['last name']['error']):

		# actual = self.page.last_name_error
		step_definition(self,
		                expected=expected,
		                actual=self.page.last_name_error,
		                step_description='Verify Last Name Error')

	@pytest.mark.skipif(Config().base_url == 'https://parabank.parasoft.com',
	                    reason="This is demo test that will have negative effect on Travis CI status")
	def verify_address_error(self, expected=RegisterPageContent.FORM['address']['error']):

		# actual = self.page.address_error
		step_definition(self,
		                expected=expected,
		                actual=self.page.address_error,
		                step_description='Verify Address Error')

	@pytest.mark.skipif(Config().base_url == 'https://parabank.parasoft.com',
	                    reason="This is demo test that will have negative effect on Travis CI status")
	def verify_city_error(self, expected=RegisterPageContent.FORM['city']['error']):

		# actual = self.page.city_error
		step_definition(self,
		                expected=expected,
		                actual=self.page.city_error,
		                step_description='Verify City Error')

	@pytest.mark.skipif(Config().base_url == 'https://parabank.parasoft.com',
	                    reason="This is demo test that will have negative effect on Travis CI status")
	def verify_state_error(self, expected=RegisterPageContent.FORM['state']['error']):

		# actual = self.page.state_error
		step_definition(self,
		                expected=expected,
		                actual=self.page.state_error,
		                step_description='Verify State Error')

	@pytest.mark.skipif(Config().base_url == 'https://parabank.parasoft.com',
	                    reason="This is demo test that will have negative effect on Travis CI status")
	def verify_zip_code_error(self, expected=RegisterPageContent.FORM['zip code']['error']):

		# actual = self.page.zip_code_error
		step_definition(self,
		                expected=expected,
		                actual=self.page.zip_code_error,
		                step_description='Verify Zip Code Error')

	@pytest.mark.skipif(Config().base_url == 'https://parabank.parasoft.com',
	                    reason="This is demo test that will have negative effect on Travis CI status")
	def verify_ssn_error(self, expected=RegisterPageContent.FORM['ssn']['error']):

		step_definition(self,
		                expected=expected,
		                actual=self.page.ssn_error,
		                step_description='Verify SSN Error')

	def fill_out_user_data(self):

		step_definition(self,
		                expected=self.client.first_name,
		                actual=self.page.first_name,
		                act=self.page.type_first_name,
		                step_description='Type first name > Verify "First Name" field value')

		'''
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
		'''

		step_definition(self,
		                expected=self.client.last_name,
		                actual=self.page.last_name,
		                act=self.page.type_last_name,
		                step_description='Type last name > Verify "Last Name" field value')
		'''
		with allure.step('Type last name'):
			expected = self.client.last_name
			self.page.type_last_name(expected)
			actual = self.page.last_name()
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('\'Type last name\'',
			                                                    expected,
			                                                    actual))
			with allure.step('Verify "Last Name" field value'):
				self.assertEqual(expected,
				                 actual,
				                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
				                                                                                    actual))
		'''

		step_definition(self,
		                expected=self.client.address,
		                actual=self.page.address,
		                act=self.page.type_address,
		                step_description='Type address > Verify "Address" field value')
		'''
		with allure.step('Type address'):
			expected = self.client.address
			self.page.type_address(expected)
			actual = self.page.address()
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('\'Type address\'',
			                                                    expected,
			                                                    actual))
			with allure.step('Verify "Address" field value'):
				self.assertEqual(expected,
				                 actual,
				                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
				                                                                                    actual))
		'''

		step_definition(self,
		                expected=self.client.city,
		                actual=self.page.city,
		                act=self.page.type_city,
		                step_description='Type city > Verify "City" field value')
		'''
		with allure.step('Type city'):
			expected = self.client.city
			self.page.type_city(expected)
			actual = self.page.city()
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('\'Type city\'',
			                                                    expected,
			                                                    actual))
			with allure.step('Verify "City" field value'):
				self.assertEqual(expected,
				                 actual,
				                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
				                                                                                    actual))
		'''

		step_definition(self,
		                expected=self.client.state,
		                actual=self.page.state,
		                act=self.page.type_state,
		                step_description='Type state > Verify "State" field value')
		'''
		with allure.step('Type state'):
			expected = self.client.state
			self.page.type_state(expected)
			actual = self.page.state()
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('\'Type state\'',
			                                                    expected,
			                                                    actual))
			with allure.step('Verify "State" field value'):
				self.assertEqual(expected,
				                 actual,
				                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
				                                                                                    actual))
		'''

		step_definition(self,
		                expected=self.client.zip_code,
		                actual=self.page.zip_code,
		                act=self.page.type_zip_code,
		                step_description='Type zip code > Verify "Zip Code" field value')
		'''
		with allure.step('Type zip code'):
			expected = self.client.zip_code
			self.page.type_zip_code(expected)
			actual = self.page.zip_code()
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('\'Type zip code\'',
			                                                    expected,
			                                                    actual))
			with allure.step('Verify "Zip Code" field value'):
				self.assertEqual(expected,
				                 actual,
				                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
				                                                                                    actual))
		'''

		step_definition(self,
		                expected=self.client.ssn,
		                actual=self.page.ssn,
		                act=self.page.type_ssn,
		                step_description='Type SSN > Verify "SSN" field value')
		'''
		with allure.step('Type SSN'):
			expected = self.client.ssn
			self.page.type_ssn(expected)
			actual = self.page.ssn()
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('\'Type SSN\'',
			                                                    expected,
			                                                    actual))
			with allure.step('Verify "SSN" field value'):
				self.assertEqual(expected,
				                 actual,
				                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
				                                                                                    actual))
		'''

