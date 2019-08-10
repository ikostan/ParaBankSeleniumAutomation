#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
from utils.clean_database import clean_database
from utils.screenshot import screenshot_on_fail
from utils.open_web_browser import open_web_browser
from expected_results.users.no_such_user import NoOne
from page_models.home_page_model import HomePageModel
from utils.http_status_code import get_http_status_code
from tests.context_tests.context_cases import HomePageContextCase
from expected_results.page_context.home_page_context import HomePageContext


@allure.suite("End To End")
@allure.sub_suite('Home Page')
@allure.feature("User Login/Logout")
@screenshot_on_fail()
class TestUserLoginFromHomePage(HomePageContextCase):

	@classmethod
	def setUpClass(cls):
		cls.user = NoOne
		cls.browser = 'chrome'
		cls.page_model = HomePageModel
		cls.page_context = HomePageContext

		with allure.step("Initial data setup > clean DB"):
			clean_database()

		with allure.step("Open web browser"):
			get_http_status_code(HomePageContext.URL)
			cls.page = open_web_browser(browser=cls.browser,
			                            page_model=cls.page_model,
			                            page_context=cls.page_context)

	@classmethod
	def tearDownClass(cls):
		with allure.step("Close web browser"):
			if cls.page:
				cls.page.quit()
				cls.page = None

	def test_user_login_logout(self):
		allure.dynamic.description("""
				User Log In validation > Negative test (no such user):
					1. Open Home web page
					2. Do URL verification
					3. Do Title verification
					4. Type username/password
					5. Hit "Log In" button
					6. Verify error title
					7. Verify error message
					9. Do URL verification
					10. Verify that "Account Services" menu is not displayed
					11. Verify web page title
					12. Close web browser
				""")
		allure.dynamic.title("User Log In validation > Negative test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# test url
		self.verify_page_url()

		# Verify Page Title
		self.verify_page_title()

		with allure.step('Type Username'):
			expected = self.user.USERNAME
			self.page.enter_username(expected)

			with allure.step('Verify Username value'):
				actual = self.page.username
				print('\nStep: {}\nExpected: {}\nActual: {}'.format('Verify Username value',
				                                                    expected,
				                                                    actual))
				self.assertEqual(expected,
				                 actual,
				                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
				                                                                                    actual))

		with allure.step('Type Password'):
			expected = self.user.PASSWORD
			self.page.enter_password(expected)

			with allure.step('Verify Password value'):
				actual = self.page.password
				print('\nStep: {}\nExpected: {}\nActual: {}'.format('Verify Password value',
				                                                    expected,
				                                                    actual))
				self.assertEqual(expected,
				                 actual,
				                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
				                                                                                    actual))

		with allure.step('Hit Log In button'):
			self.page.hit_login_button()

		# Verify ERROR message
		with allure.step('Verify Error title'):
			expected = HomePageContext.ERROR_TITLE
			actual = self.page.error_title
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('Verify "Error" title',
			                                                    expected,
			                                                    actual))
			self.assertEqual(expected,
			                 actual,
			                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
			                                                                                    actual))

		with allure.step('Verify Error message'):
			expected = HomePageContext.ERROR_MESSAGE
			actual = self.page.error_message
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('Verify "Error" message',
			                                                    expected,
			                                                    actual))
			self.assertEqual(expected,
			                 actual,
			                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
			                                                                                    actual))

		# Post Logout validation
		with allure.step('Do URL verification'):
			expected = 'https://parabank.parasoft.com/parabank/login.htm'
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

		# Verify Page Title
		with allure.step("Verify web page title. Expected result: {}".format(HomePageContext.TITLE)):
			expected = 'ParaBank | Error'
			actual = self.page.driver.title
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('\'Verify URL\'',
			                                                    expected,
			                                                    actual))
			self.assertEqual(expected,
			                 actual,
			                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
			                                                                                    actual))
