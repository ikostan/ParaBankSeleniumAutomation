import allure
from tests.context_tests.base_context_case import TestBaseContextCase
from expected_results.page_context.base_personal_info_context import BasePersonalInfoContext


# @allure.feature("Base Personal Info Context")
class BasePersonalInfoContextTestCase(TestBaseContextCase):
	"""
	This class should be the parent class to each test case class.
	"""

	@allure.feature("Base Personal Info Context")
	def first_name_title_test(self):
		'''
		Validate First Name field title
		:return:
		'''

		with allure.step("Test First Name title"):
			self.assertEqual(BasePersonalInfoContext.FORM['first_name']['title'], self.page.first_name_title)

	@allure.feature("Base Personal Info Context")
	def last_name_title_test(self):
		'''
		Validate Last Name field title
		:return:
		'''

		with allure.step("Test Last Name title"):
			self.assertEqual(BasePersonalInfoContext.FORM['last_name']['title'], self.page.last_name_title)

	@allure.feature("Base Personal Info Context")
	def address_title_test(self):
		'''
		Validate Address field title
		:return:
		'''

		with allure.step("Test Address title"):
			self.assertEqual(BasePersonalInfoContext.FORM['address']['title'], self.page.address_title)

	@allure.feature("Base Personal Info Context")
	def city_title_test(self):
		'''
		Validate city field title
		:return:
		'''

		with allure.step("Test City title"):
			self.assertEqual(BasePersonalInfoContext.FORM['city']['title'], self.page.city_title)

	@allure.feature("Base Personal Info Context")
	def state_title_test(self):
		'''
		Validate state field title
		:return:
		'''

		with allure.step("Test State title"):
			self.assertEqual(BasePersonalInfoContext.FORM['state']['title'], self.page.state_title)

	@allure.feature("Base Personal Info Context")
	def zip_code_title_test(self):
		'''
		Validate Zip Code field title
		:return:
		'''

		with allure.step("Test Zip Code title"):
			self.assertEqual(BasePersonalInfoContext.FORM['zip_code']['title'], self.page.zip_code_title)

	@allure.feature("Base Personal Info Context")
	def phone_title_test(self):
		'''
		Validate phone field title
		:return:
		'''

		with allure.step("Test Phone title"):
			self.assertEqual(BasePersonalInfoContext.FORM['phone']['title'], self.page.phone_title)

	@allure.feature("Base Personal Info Context")
	def ssn_title_test(self):
		'''
		Validate ssn field title
		:return:
		'''

		with allure.step("Test SSN title"):
			self.assertEqual(BasePersonalInfoContext.FORM['ssn']['title'], self.page.ssn_title)

