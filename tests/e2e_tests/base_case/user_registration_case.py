#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure

from expected_results.page_content.register_page_content import RegisterPageContent
from tests.e2e_tests.base_case.user_personal_info_case import UserPersonalInfoCase
from utils.step_definition import step_definition


class UserRegistrationCase(UserPersonalInfoCase):

	def fill_out_user_data(self):

		super().fill_out_user_data()

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

	def verify_username_error(self, expected=RegisterPageContent.FORM['username']['error']):

		actual = self.page.state_error
		step_definition(self,
		                expected=expected,
		                actual=actual,
		                step_description='Verify Username Error',
		                severity=allure.severity_level.NORMAL)

	def verify_password_error(self, expected=RegisterPageContent.FORM['password']['error']):

		actual = self.page.state_error
		step_definition(self,
		                expected=expected,
		                actual=actual,
		                step_description='Verify Password Error',
		                severity=allure.severity_level.NORMAL)

	def verify_confirm_error(self, expected=RegisterPageContent.FORM['confirm']['error']):

		actual = self.page.state_error
		step_definition(self,
		                expected=expected,
		                actual=actual,
		                step_description='Verify Confirm Error',
		                severity=allure.severity_level.NORMAL)

