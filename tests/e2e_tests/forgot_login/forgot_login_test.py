#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure

from utils.screenshot import screenshot_on_fail
from utils.open_web_browser import open_web_browser
from utils.clean_database import clean_database
from utils.register_user import register_user
from utils.step_definition import step_definition

from expected_results.users.base_user import BaseUser
from expected_results.users.valid_users_templates.john_doe import JohnDoe
from expected_results.page_content.bank_account_content import BankAccountContent
from expected_results.page_content.home_page_content import HomePageContent

from tests.e2e_tests.base_case.user_personal_info_case import UserPersonalInfoCase
from page_object_models.forgot_login_info_page_model import ForgotLoginInfoPageModel
from expected_results.page_content.forgot_login_info_page_content import ForgotLoginInfoPageContent


@allure.epic('Page Functionality')
@allure.parent_suite('End To End')
@allure.suite("Forgot Login")
@allure.sub_suite('Positive Tests')
@allure.feature("Forgot Login Page")
@allure.story('Forgot Login Functionality')
@screenshot_on_fail()
class TestForgotLoginCase(UserPersonalInfoCase):

	@classmethod
	def setUpClass(cls):
		cls.client = BaseUser(JohnDoe)
		cls.page = None
		cls.page_model = ForgotLoginInfoPageModel
		cls.page_context = ForgotLoginInfoPageContent

	@classmethod
	def tearDownClass(cls):
		with allure.step("Close Web Browser"):
			if cls.page:
				cls.page.quit()
				cls.page = None

	def setUp(self):

		with allure.step("Initial data setup > clean DB"):
			clean_database()

		with allure.step("Initial data setup > register test user"):
			register_user(self.client)

		with allure.step("Initial data setup: {}".format(ForgotLoginInfoPageContent.URL)):
			with allure.step("Open web browser"):
				self.page = open_web_browser(page_model=self.page_model,
				                             page_content=self.page_context)

	def tearDown(self):
		with allure.step("Close current tab"):
			if self.page:
				self.page.close()

	def test_user_registration(self):
		allure.dynamic.description("""
		Forgot Login Info test case:
			1. Open 'Forgot Login Info' web page
			2. Fill out user personal data > Set all fields with valid data
			3. Verify that each data item (empty string) appears in relevant field
			4. Hit 'FIND MY LOGIN' button
			5. Verify that Username/Password appears
			6. Verify "Welcome" message
			7. Verify that "Account Services" menu is present
			8. Log Out
			9. Close web browser
		""")
		allure.dynamic.title("User registration > Positive Test")
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		# Register a new user:
		self.fill_out_user_data()

		with allure.step('Hit "FIND MY LOGIN INFO" button'):
			print('Hit "FIND MY LOGIN INFO" button')
			self.page = self.page.click_find_info_btn()

		# Verify "Username/Password" data
		step_definition(self,
		                expected='{}{}\n{}{}'.format(ForgotLoginInfoPageContent.USERNAME,
		                                             self.client.username,
		                                             ForgotLoginInfoPageContent.PASSWORD,
		                                             self.client.password),
		                actual=self.page.username_password,
		                act=None,
		                step_description='Verify "Username/Password" data',
		                click=False)

		# Verify "Welcome" message
		step_definition(self,
		                expected='{}{} {}'.format(BankAccountContent.ACCOUNT_SERVICES_MENU['welcome_message'],
		                                          self.client.first_name,
		                                          self.client.last_name),
		                actual=self.page.welcome_message,
		                act=None,
		                step_description='Verify "Welcome" message')
		'''
		with allure.step('Verify "Welcome" message'):
			expected = '{}{} {}'.format(BankAccountContent.ACCOUNT_SERVICES_MENU['welcome_message'],
			                            self.client.first_name,
			                            self.client.last_name)
			actual = self.page.welcome_message
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('Verify "Welcome" message',
			                                                    expected,
			                                                    actual))
			self.assertEqual(expected,
			                 actual,
			                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
			                                                                                    actual))
		'''

		step_definition(self,
		                expected=True,
		                actual=self.page.account_services_menu_is_visible,
		                act=None,
		                step_description='Verify that "Account Services" menu is present')
		'''
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
		'''

		# Log Out
		with allure.step('Hit "Log Out" link'):
			print("Log Out..")
			self.page = self.page.hit_log_out_button()

		# Log Out > Post Logout validation
		step_definition(self,
		                expected=HomePageContent.URL,
		                actual=self.page.url,
		                act=None,
		                step_description='Do URL verification',
		                click=False)
		'''
		with allure.step('Hit "Log Out" link > Do URL verification'):
			expected = HomePageContent.URL
			actual = self.page.url
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('\'Verify URL\'',
			                                                    expected,
			                                                    actual))
			self.assertEqual(expected,
			                 actual,
			                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
			                                                                                    actual))
		'''

		# Verify that "Account Services" menu is not present
		step_definition(self,
		                expected=False,
		                actual=self.page.account_services_menu_is_visible,
		                act=None,
		                step_description='Verify that "Account Services" menu is not present')
		'''
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
		'''

		# Verify Page Title
		step_definition(self,
		                expected=HomePageContent.TITLE,
		                actual=self.page.title,
		                act=None,
		                step_description='Verify web page title')
		'''
		with allure.step("Verify web page title. Expected result: {}".format(HomePageContent.TITLE)):
			self.assertEqual(HomePageContent.TITLE,
			                 self.page.title)
		'''

