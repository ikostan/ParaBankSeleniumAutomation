#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
import unittest

from tests.config import Config
from utils.register_user import register_user
from utils.clean_database import clean_database
from utils.screenshot import screenshot_on_fail
from utils.open_web_browser import open_web_browser
from utils.step_definition import step_definition

from page_object_models.home_page_model import HomePageModel
from expected_results.users.base_user import BaseUser
from expected_results.users.valid_users_templates.jane_doe import JaneDoe
from expected_results.page_content.home_page_content import HomePageContent
from expected_results.page_content.bank_account_content import BankAccountContent


@allure.epic('Page Functionality')
@allure.parent_suite('End To End')
@allure.suite("User Login/Logout")
@allure.sub_suite("Positive Tests")
@allure.feature("Home Page")
@allure.story('Login/Logout Functionality')
@screenshot_on_fail()
class TestUserLoginFromHomePage(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.user = BaseUser(JaneDoe)
		cls.page_model = HomePageModel
		cls.page_context = HomePageContent
		cls.config = Config()

		with allure.step("Initial data setup > clean DB"):
			clean_database(config=cls.config)

		with allure.step("Initial data setup > register test user"):
			register_user(user=cls.user, config=cls.config)

		with allure.step("Open web browser"):
			cls.page = open_web_browser(config=cls.config,
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
		allure.dynamic.title("Home page > User Log In validation > Positive test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

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
		                step_description='Verify "Welcome" message',
		                expected='{}{} {}'.format(BankAccountContent.ACCOUNT_SERVICES_MENU['welcome_message'],
		                                          self.user.first_name,
		                                          self.user.last_name),
		                actual=self.page.welcome_message,
		                act=None,
		                click=False)
		'''
		with allure.step('Hit Log In button'):
			self.page.hit_login_button()

		# Verify "Welcome" message
		with allure.step('Verify "Welcome" message'):
			expected = '{}{} {}'.format(BankAccountContent.ACCOUNT_SERVICES_MENU['welcome_message'],
			                            self.user.first_name,
			                            self.user.last_name)
			actual = self.page.welcome_message()
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('Verify "Welcome" message',
			                                                    expected,
			                                                    actual))
			self.assertEqual(expected,
			                 actual,
			                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
			                                                                                    actual))
		'''

		step_definition(self,
		                step_description='Verify that "Account Services" menu is present',
		                expected=True,
		                actual=self.page.account_services_menu_is_visible,
		                act=None,
		                click=False)
		'''
		with allure.step('Verify that "Account Services" menu is present'):
			expected = True
			actual = self.page.account_services_menu_is_visible()
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('"Account Services" menu is present',
			                                                    expected,
			                                                    actual))
			self.assertEqual(expected,
			                 actual,
			                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
			                                                                                    actual))
		'''

		# Log Out
		with allure.step('Hit "Log Out" link'):
			self.page = self.page.hit_log_out_button()

		# Post Logout validation
		step_definition(self,
		                step_description='Do URL verification',
		                expected= self.config.base_url + HomePageContent.URL,
		                actual=self.page.url,
		                act=None,
		                click=False)
		'''
		with allure.step('Hit "Log Out" link'):
			self.page.hit_log_out_button()

		with allure.step('Do URL verification'):

			expected = 'https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC'
			actual = self.page.url()
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('\'Verify URL\'',
			                                                    expected,
			                                                    actual))
			self.assertEqual(expected,
			                 actual,
			                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
			                                                                                    actual))
		'''

		step_definition(self,
		                step_description='Verify that "Account Services" menu is not shown',
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

		# Verify Page Title
		step_definition(self,
		                step_description='Verify web page title',
		                expected=HomePageContent.TITLE,
		                actual=self.page.title,
		                act=None,
		                click=False)
		'''
		with allure.step("Verify web page title. Expected result: {}".format(HomePageContent.TITLE)):
			self.assertEqual(HomePageContent.TITLE,
			                 self.page.title())
		'''
