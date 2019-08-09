import allure
from utils.screenshot import screenshot_on_fail
from utils.open_web_browser import open_web_browser
from expected_results.users.jane_doe import JaneDoe
from utils.http_status_code import get_http_status_code
from page_models.register_page_model import RegisterPageModel
from expected_results.page_context.register_page_context import RegisterPageContext
from tests.e2e_tests.user_registration.base_case.register_new_user import UserRegistrationCase


@allure.suite("End To End")
@allure.feature("User Registration")
@screenshot_on_fail()
class TestChromeUserRegistration(UserRegistrationCase):

	@classmethod
	def setUpClass(cls):
		with allure.step("Initial data setup: {}, {}".format('chrome', RegisterPageContext.URL)):
			cls.browser = 'chrome'
			cls.page_model = RegisterPageModel
			cls.page_context = RegisterPageContext
			cls.page = None

	@classmethod
	def tearDownClass(cls):
		with allure.step("Close Web Browser"):
			if cls.page:
				cls.page.quit()
				cls.page = None

	def setUp(self):
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
			6. Verify success message
			7. Log Out
		""")
		allure.dynamic.title("User registration test")
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		client = JaneDoe
		self.register_new_user(client)

		# TODO: add logout
