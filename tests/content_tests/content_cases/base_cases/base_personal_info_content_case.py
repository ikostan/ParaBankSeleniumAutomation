#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
from expected_results.page_content.base_personal_info_content import BasePersonalInfoContent
from tests.content_tests.content_cases.base_cases.base_content_case import BaseContentCase


class BasePersonalInfoContentCase(BaseContentCase):
	"""
	This class should be the parent class to each test case class.
	"""

	def verify_first_name_title(self):
		'''
		Validate First Name field title
		:return:
		'''

		with allure.step("Test First Name title"):
			self.assertEqual(BasePersonalInfoContent.FORM['first_name']['title'], self.page.first_name_title)

	def verify_last_name_title(self):
		'''
		Validate Last Name field title
		:return:
		'''

		with allure.step("Test Last Name title"):
			self.assertEqual(BasePersonalInfoContent.FORM['last_name']['title'], self.page.last_name_title)

	def verify_address_title(self):
		'''
		Validate Address field title
		:return:
		'''

		with allure.step("Test Address title"):
			self.assertEqual(BasePersonalInfoContent.FORM['address']['title'], self.page.address_title)

	def verify_city_title(self):
		'''
		Validate city field title
		:return:
		'''

		with allure.step("Test City title"):
			self.assertEqual(BasePersonalInfoContent.FORM['city']['title'], self.page.city_title)

	def verify_state_title(self):
		'''
		Validate state field title
		:return:
		'''

		with allure.step("Test State title"):
			self.assertEqual(BasePersonalInfoContent.FORM['state']['title'], self.page.state_title)

	def verify_zip_code_title(self):
		'''
		Validate Zip Code field title
		:return:
		'''

		with allure.step("Test Zip Code title"):
			self.assertEqual(BasePersonalInfoContent.FORM['zip_code']['title'], self.page.zip_code_title)

	def verify_phone_title(self):
		'''
		Validate phone field title
		:return:
		'''

		with allure.step("Test Phone title"):
			self.assertEqual(BasePersonalInfoContent.FORM['phone']['title'], self.page.phone_title)

	def verify_ssn_title(self):
		'''
		Validate ssn field title
		:return:
		'''

		with allure.step("Test SSN title"):
			self.assertEqual(BasePersonalInfoContent.FORM['ssn']['title'], self.page.ssn_title)

