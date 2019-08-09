import allure
from utils.screenshot import screenshot_on_fail
from utils.open_web_browser import open_web_browser
from utils.clean_database import clean_database
from expected_results.users.jane_doe import JaneDoe
from utils.http_status_code import get_http_status_code
from page_models.register_page_model import RegisterPageModel
from expected_results.page_context.home_page_context import HomePageContext
from expected_results.page_context.register_page_context import RegisterPageContext
from tests.e2e_tests.user_registration.base_case.register_new_user import UserRegistrationCase


@allure.suite("End To End")
@allure.sub_suite('User Registration Page')
@allure.feature("User Registration")
@screenshot_on_fail()
class TestChromeUserRegistration(UserRegistrationCase):

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
		allure.dynamic.title("User registration test")
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		# Register a new user:
		self.register_new_user(self.client)

		with allure.step('Verify that "Account Services" menu is present'):
			expected = True
			actual = self.page.account_services_menu_is_visible
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('"Account Services" menu is present',
			                                                    expected,
			                                                    actual))
			self.assertEqual(expected,
			                 actual,
			                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
			                                                                                    actual))
		# Logout
		with allure.step('Hit "Log Out" link'):
			self.page.log_out()

		# Post Logout validation
		with allure.step('Verify URL'):
			expected = HomePageContext.URL
			actual = self.page.url
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('\'Verify URL\'',
			                                                    expected,
			                                                    actual))
			self.assertEqual(expected,
			                 actual,
			                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
			                                                                                    actual))

		with allure.step('Verify that "Account Services" menu is not present'):
			expected = False
			actual = self.page.account_services_menu_is_visible
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('"Account Services" menu is not present',
			                                                    expected,
			                                                    actual))
			self.assertEqual(expected,
			                 actual,
			                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
			                                                                                    actual))
