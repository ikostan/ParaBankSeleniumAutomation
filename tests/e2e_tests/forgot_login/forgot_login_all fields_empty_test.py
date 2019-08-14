#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure

from utils.screenshot import screenshot_on_fail
from utils.open_web_browser import open_web_browser

from expected_results.users.base_user import BaseUser
from expected_results.users.invalid_users_templates.empty_fields import EmptyFields

from tests.e2e_tests.base_case.user_personal_info_case import UserPersonalInfoCase
from page_object_models.forgot_login_info_page_model import ForgotLoginInfoPageModel
from expected_results.page_content.forgot_login_info_page_content import ForgotLoginInfoPageContent


@allure.epic('Page Functionality')
@allure.parent_suite('End To End')
@allure.suite("Forgot Login")
@allure.sub_suite('Negative Tests')
@allure.feature("Forgot Login Page")
@allure.story('Forgot Login Functionality')
@screenshot_on_fail()
class TestForgotLoginAllFieldsEmpty(UserPersonalInfoCase):

	@classmethod
	def setUpClass(cls):
		cls.client = BaseUser(EmptyFields)
		cls.browser = 'chrome'
		cls.page = None

	@classmethod
	def tearDownClass(cls):
		with allure.step("Close Web Browser"):
			if cls.page:
				cls.page.quit()
				cls.page = None

	def setUp(self):
		with allure.step("Initial data setup: {}, {}".format(self.browser, ForgotLoginInfoPageContent.URL)):
			self.page_model = ForgotLoginInfoPageModel
			self.page_context = ForgotLoginInfoPageContent
			with allure.step("Open web browser"):
				self.page = open_web_browser(browser=self.browser,
				                             page_model=self.page_model,
				                             page_content=self.page_context)

	def tearDown(self):
		with allure.step("Close current tab"):
			if self.page:
				self.page.close()

	def test_user_registration(self):
		allure.dynamic.description("""
		Forgot Login Info test case:
			1. Open 'Forgot Login Info' web page
			2. Fill out user personal data > Set all fields empty
			3. Verify that each data item (empty string) appears in relevant field
			4. Hit 'FIND MY LOGIN' button
			5. Verify 'Error' messages
			6. Close web browser
		""")
		allure.dynamic.title("User registration > Negative test > Empty fields")
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		# Register a new user:
		self.fill_out_user_data()

		with allure.step('Hit "FIND MY LOGIN INFO" button'):
			print('Hit "Register" button')
			self.page.click_find_info_btn()

		self.verify_first_name_error()

		self.verify_last_name_error()

		self.verify_address_error()

		self.verify_city_error()

		self.verify_state_error()

		self.verify_zip_code_error()

		self.verify_ssn_error()

