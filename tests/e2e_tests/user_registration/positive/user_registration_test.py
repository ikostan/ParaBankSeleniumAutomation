#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.config import Config
from utils.step_definition import step_definition
from utils.screenshot import screenshot_on_fail
from utils.clean_database import clean_database
from utils.open_web_browser import open_web_browser

from expected_results.users.base_user import BaseUser
from expected_results.page_content.home_page_content import HomePageContent
from expected_results.users.valid_users_templates.jane_doe import JaneDoe

from page_locators.register_page_locator import RegisterPageLocator
from page_object_models.register_page_model import RegisterPageModel
from tests.e2e_tests.base_case.user_registration_case import UserRegistrationCase
from expected_results.page_content.register_page_content import RegisterPageContent


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

		cls.config = Config()
		cls.client = BaseUser(JaneDoe)
		cls.page = None

		with allure.step("Initial data setup > clean DB"):
			clean_database(cls.config)

	@classmethod
	def tearDownClass(cls):
		with allure.step("Close Web Browser"):
			if cls.page:
				cls.page.quit()
				cls.page = None

	def setUp(self):
		with allure.step("Initial data setup: {}".format(RegisterPageContent.URL)):
			self.page_model = RegisterPageModel
			self.page_content = RegisterPageContent
			with allure.step("Open web browser"):
				self.page = open_web_browser(config=self.config,
				                             page_model=self.page_model,
				                             page_content=self.page_content)

	def tearDown(self):
		with allure.step("Close current tab"):
			if self.page:
				self.page.quit()
				self.page = None

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
		self.fill_out_user_data()

		with allure.step('Hit "Register" button'):
			print('Hit "Register" button')
			self.page = self.page.hit_register_btn()

		with allure.step('Wait for "Welcome" message'):
			WebDriverWait(self.page.driver,
			              self.page.explicit_wait_time).until(
				EC.presence_of_element_located(RegisterPageLocator.HEADER))

		step_definition(self,
		                expected=RegisterPageContent.WELCOME_MESSAGE['header'] + self.client.username,
		                actual=self.page.welcome_header,
		                act=None,
		                step_description='Verify "Welcome" header',
		                click=False)

		step_definition(self,
		                expected=RegisterPageContent.WELCOME_MESSAGE['message'],
		                actual=self.page.welcome_message,
		                act=None,
		                step_description='Verify "Welcome" message',
		                click=False)

		step_definition(self,
		                expected=True,
		                actual=self.page.account_services_menu_is_visible,
		                act=None,
		                step_description='Verify that "Account Services" menu is present',
		                click=False)

		# Logout
		with allure.step('Hit "Log Out" link'):
			self.page = self.page.hit_log_out_button()

		# Post Logout validation
		step_definition(self,
		                expected=self.config.base_url + HomePageContent.URL,
		                actual=self.page.url,
		                act=None,
		                step_description='Verify URL',
		                click=False)

		step_definition(self,
		                expected=False,
		                actual=self.page.account_services_menu_is_visible,
		                act=None,
		                step_description='Verify that "Account Services" menu is not present',
		                click=False)
