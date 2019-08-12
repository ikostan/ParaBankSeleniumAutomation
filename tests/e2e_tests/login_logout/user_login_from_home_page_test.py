#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure

from utils.register_user import register_user
from utils.clean_database import clean_database
from utils.screenshot import screenshot_on_fail
from utils.open_web_browser import open_web_browser
from utils.browser_configuration import browser_configuration

from expected_results.users.jane_doe import JaneDoe
from page_object_models.home_page_model import HomePageModel
from expected_results.page_context.home_page_context import HomePageContext
from expected_results.page_context.bank_account_context import BankAccountContext
from tests.content_tests.content_cases.home_page_content_case import HomePageContentCase


@allure.epic('Page Functionality')
@allure.parent_suite('End To End')
@allure.suite("User Login/Logout")
@allure.sub_suite("Negative Tests")
@allure.feature("Home Page")
@allure.story('Login/Logout Functionality')
@screenshot_on_fail()
class TestUserLoginFromHomePage(HomePageContentCase):

	@classmethod
	def setUpClass(cls):
		cls.user = JaneDoe
		cls.browser = browser_configuration()
		cls.page_model = HomePageModel
		cls.page_context = HomePageContext

		with allure.step("Initial data setup > clean DB"):
			clean_database()

		with allure.step("Initial data setup > register test user: {} {}".format(cls.user.FIRST_NAME,
		                                                                         cls.user.LAST_NAME)):
			register_user(cls.user)

		with allure.step("Open web browser"):
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
				User Log In validation > Login from Home page:
					1. Open Home web page
					2. Do URL verification
					3. Do Title verification
					4. Type username/password
					5. Hit "Log In" button
					6. Verify "Welcome" message
					7. Verify that "Account Services" menu is present
					8. Do URL verification
					9. Log Out
					10. Do URL verification
					11. Verify that "Account Services" menu is not present
					12. Verify web page title
					13. Close web browser
				""")
		allure.dynamic.title("User Log In validation > Positive test")
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

		# Verify "Welcome" message
		with allure.step('Verify "Welcome" message'):
			expected = '{}{} {}'.format(BankAccountContext.ACCOUNT_SERVICES_MENU['welcome_message'],
			                            self.user.FIRST_NAME,
			                            self.user.LAST_NAME)
			actual = self.page.welcome_message
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('Verify "Welcome" message',
			                                                    expected,
			                                                    actual))
			self.assertEqual(expected,
			                 actual,
			                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
			                                                                                    actual))

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

		# Log Out
		with allure.step('Hit "Log Out" link'):
			self.page.log_out()

		# Post Logout validation
		with allure.step('Do URL verification'):
			expected = 'https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC'
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
		self.verify_page_title()
