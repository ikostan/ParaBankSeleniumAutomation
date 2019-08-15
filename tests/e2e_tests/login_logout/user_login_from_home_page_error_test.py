#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
import unittest

from utils.clean_database import clean_database
from utils.screenshot import screenshot_on_fail
from utils.open_web_browser import open_web_browser
from utils.step_definition import step_definition
from utils.browser_configuration import browser_configuration

from expected_results.users.base_user import BaseUser
from page_object_models.home_page_model import HomePageModel
from expected_results.page_content.home_page_content import HomePageContent
from expected_results.page_content.login_page_content import LoginPageContent
from expected_results.users.invalid_users_templates.no_such_user import NoSuchUser


@allure.epic('Page Functionality')
@allure.parent_suite('End To End')
@allure.suite("User Login/Logout")
@allure.sub_suite('Negative Tests')
@allure.feature("Home Page")
@allure.story('Login/Logout Functionality')
@screenshot_on_fail()
class TestUserLoginFromHomePageError(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.user = BaseUser(NoSuchUser)
		cls.browser = browser_configuration()
		cls.page_model = HomePageModel
		cls.page_context = HomePageContent

		with allure.step("Initial data setup > clean DB"):
			clean_database()

		with allure.step("Open web browser"):
			cls.page = open_web_browser(browser=cls.browser,
			                            page_model=cls.page_model,
			                            page_content=cls.page_context)

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
		#self.verify_page_url()

		# Verify Page Title
		#self.verify_page_title()

		step_definition(self,
		                step_description='Type Username > Verify Username value',
		                expected=self.user.username,
		                actual=self.page.username,
		                act=self.page.enter_username,
		                click=False)
		'''
		with allure.step('Type Username'):
			expected = self.user.username
			self.page.enter_username(expected)

			with allure.step('Verify Username value'):
				actual = self.page.username()
				print('\nStep: {}\nExpected: {}\nActual: {}'.format('Verify Username value',
				                                                    expected,
				                                                    actual))
				self.assertEqual(expected,
				                 actual,
				                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
				                                                                                    actual))
		'''

		step_definition(self,
		                step_description='Type Password > Verify Password value',
		                expected=self.user.password,
		                actual=self.page.password,
		                act=self.page.enter_password,
		                click=False)
		'''
		with allure.step('Type Password'):
			expected = self.user.password
			self.page.enter_password(expected)

			with allure.step('Verify Password value'):
				actual = self.page.password()
				print('\nStep: {}\nExpected: {}\nActual: {}'.format('Verify Password value',
				                                                    expected,
				                                                    actual))
				self.assertEqual(expected,
				                 actual,
				                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
				                                                                                    actual))
		'''

		with allure.step('Hit Log In button'):
			self.page = self.page.hit_login_button()

		step_definition(self,
		                step_description='Verify that "Account Services" menu is not present',
		                expected=False,
		                actual=self.page.account_services_menu_is_visible,
		                act=None,
		                click=False)
		'''
		with allure.step('Verify that "Account Services" menu is not present'):
			expected = False
			actual = self.page.account_services_menu_is_visible()
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('"Account Services" menu is not present',
			                                                    expected,
			                                                    actual))
			self.assertEqual(expected,
			                 actual,
			                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
			                                                                                    actual))
		'''

		# Verify ERROR title
		step_definition(self,
		                step_description='Verify Error title',
		                expected=LoginPageContent.ERROR_TITLE,
		                actual=self.page.error_title,
		                act=None,
		                click=False)
		'''
		with allure.step('Verify Error title'):
			expected = LoginPageContent.ERROR_TITLE
			actual = self.page.error_title()
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('Verify "Error" title',
			                                                    expected,
			                                                    actual))
			self.assertEqual(expected,
			                 actual,
			                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
			                                                                                    actual))
		'''

		# Verify ERROR message
		step_definition(self,
		                step_description='Verify Error message',
		                expected=LoginPageContent.ERROR_MESSAGE,
		                actual=self.page.error_message,
		                act=None,
		                click=False)
		'''
		with allure.step('Verify Error message'):
			expected = LoginPageContent.ERROR_MESSAGE
			actual = self.page.error_message()
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('Verify "Error" message',
			                                                    expected,
			                                                    actual))
			self.assertEqual(expected,
			                 actual,
			                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
			                                                                                    actual))
		'''

		# URL validation
		step_definition(self,
		                step_description='Do URL verification',
		                expected=LoginPageContent.URL,
		                actual=self.page.url,
		                act=None,
		                click=False)
		'''
		with allure.step('Do URL verification'):
			expected = 'https://parabank.parasoft.com/parabank/login.htm'
			actual = self.page.url()
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('\'Verify URL\'',
			                                                    expected,
			                                                    actual))
			self.assertEqual(expected,
			                 actual,
			                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
			                                                                                    actual))
		'''

