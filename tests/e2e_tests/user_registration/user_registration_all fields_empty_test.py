#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


import allure

from utils.screenshot import screenshot_on_fail
from utils.clean_database import clean_database
from utils.open_web_browser import open_web_browser

from expected_results.users.base_user import BaseUser
from expected_results.users.invalid_users_templates.empty_fields import EmptyFields

from page_object_models.register_page_model import RegisterPageModel
from expected_results.page_content.register_page_content import RegisterPageContent
from tests.e2e_tests.user_registration.base_case.user_registration_case import UserRegistrationCase


@allure.epic('Page Functionality')
@allure.parent_suite('End To End')
@allure.suite("User Registration")
@allure.sub_suite('Negative Tests')
@allure.feature("Register Page")
@allure.story('Register Functionality')
@screenshot_on_fail()
class TestUserRegistrationAllFieldsEmpty(UserRegistrationCase):

	@classmethod
	def setUpClass(cls):
		cls.client = BaseUser(EmptyFields)
		cls.browser = 'chrome'
		cls.page = None

		with allure.step("Initial data setup > clean DB"):
			clean_database()

	@classmethod
	def tearDownClass(cls):
		with allure.step("Close Web Browser"):
			if cls.page:
				cls.page.quit()
				cls.page = None

	def setUp(self):
		with allure.step("Initial data setup: {}, {}".format(self.browser, RegisterPageContent.URL)):
			self.page_model = RegisterPageModel
			self.page_context = RegisterPageContent
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
		User registration test case:
			1. Open 'Register' web page
			2. Fill out user personal data > Set all fields empty
			4. Verify that each data item (empty string) appears in relevant field
			5. Hit 'Register' button
			6. Verify 'Error' messages
			9. Verify that "Account Services" menu is not present
			10. Close web browser
		""")
		allure.dynamic.title("User registration > Negative test > Empty fields")
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		# Register a new user:
		self.fill_out_user_data()

