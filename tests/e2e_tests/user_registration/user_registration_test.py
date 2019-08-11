#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
from utils.screenshot import screenshot_on_fail
from utils.clean_database import clean_database
from utils.open_web_browser import open_web_browser
from expected_results.users.jane_doe import JaneDoe
from utils.http_status_code import get_http_status_code
from page_object_models.register_page_model import RegisterPageModel
from expected_results.page_context.register_page_context import RegisterPageContext
from tests.e2e_tests.user_registration.base_case.register_new_user import UserRegistrationCase


@allure.epic('Page Functionality')
@allure.parent_suite('End To End')
@allure.suite("User Registration")
@allure.sub_suite('Positive Tests')
@allure.feature("Register Page")
@allure.story('Register Functionality')
@screenshot_on_fail()
class TestUserRegistration(UserRegistrationCase):

	@classmethod
	def setUpClass(cls):
		cls.client = JaneDoe
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
		with allure.step("Initial data setup: {}, {}".format(self.browser, RegisterPageContext.URL)):
			self.page_model = RegisterPageModel
			self.page_context = RegisterPageContext
			with allure.step("Open web browser"):
				get_http_status_code(RegisterPageContext.URL)
				self.page = open_web_browser(browser=self.browser,
				                             page_model=self.page_model,
				                             page_context=self.page_context)

	def tearDown(self):
		with allure.step("Close current tab"):
			if self.page:
				self.page.close()

	def test_user_registration(self):
		allure.dynamic.description("""
		User registration test case:
			1. Open 'Register' web page
			2. Fill out user personal data
			4. Verify that each data item appears in relevant field
			5. Hit 'Register' button
			6. Verify 'Welcome' message
			7. Verify that "Account Services" menu is present
			8. Log Out
			9. Verify that "Account Services" menu is not present
			10. Close web browser
		""")
		allure.dynamic.title("User registration > Positive test")
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		# Register a new user:
		self.register_new_user()

