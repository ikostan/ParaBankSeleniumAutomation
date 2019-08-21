#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
import pytest

from tests.config import Config
from utils.screenshot import screenshot_on_fail
from utils.step_definition import step_definition
from utils.open_web_browser import open_web_browser

from expected_results.users.base_user import BaseUser
from expected_results.users.valid_users_templates.john_doe import JohnDoe

from page_object_models.register_page_model import RegisterPageModel
from tests.e2e_tests.base_case.user_registration_case import UserRegistrationCase
from expected_results.page_content.register_page_content import RegisterPageContent


@allure.epic('Page Functionality')
@allure.parent_suite('End To End')
@allure.suite("User Registration")
@allure.sub_suite('Negative Tests')
@allure.feature("Register Page")
@allure.story('Register Functionality')
#@pytest.mark.skipif(get_args()['env'] == 'production',
#                    reason="This is demo test that will have negative effect on Travis CI status")
@screenshot_on_fail()
class TestUserRegistrationPasswordDidNotMatch(UserRegistrationCase):

	@classmethod
	def setUpClass(cls):
		cls.client = BaseUser(JohnDoe)
		cls.page = None
		cls.config = Config()

	@classmethod
	def tearDownClass(cls):
		with allure.step("Close Web Browser"):
			if cls.page:
				cls.page.quit()
				cls.page = None

	def setUp(self):
		with allure.step("Initial data setup: {}".format(RegisterPageContent.URL)):
			self.page_model = RegisterPageModel
			self.page_context = RegisterPageContent
			with allure.step("Open web browser"):
				self.page = open_web_browser(config=self.config,
				                             page_model=self.page_model,
				                             page_content=self.page_context)

	def tearDown(self):
		with allure.step("Close current tab"):
			if self.page:
				self.page.close()

	def test_user_registration_duplicate_username(self):
		allure.dynamic.description("""
		User registration test case:
			1. Open 'Register' web page
			2. Fill out user personal data > Set different values for Password and Confirm fields
			3. Verify that each data item appears in relevant field
			4. Hit 'Register' button
			5. Verify that each personal data item appears in relevant field
			6. Verify 'Error' message
			7. Verify that "Account Services" menu is not present
			8. Close web browser
		""")
		allure.dynamic.title("User registration > Negative test > Password did not match")
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		# Register a new user:
		self.fill_out_user_data()

		step_definition(self,
		                expected='something',
		                actual=self.page.confirm,
		                act=self.page.type_confirm,
		                step_description='Type a new Confirm value > Verify "Confirm" field value',
		                click=False)

		with allure.step('Hit "Register" button'):
			print('Hit "Register" button')
			self.page = self.page.hit_register_btn()

		step_definition(self,
		                step_description='Verify that "Account Services" menu is not present',
		                expected=False,
		                actual=self.page.account_services_menu_is_visible,
		                act=None,
		                click=False)

		step_definition(self,
		                step_description='Verify Confirm error',
		                expected=RegisterPageContent.FORM['confirm']['no_match'],
		                actual=self.page.confirm_error,
		                act=None,
		                click=False)

		step_definition(self,
		                expected=self.client.first_name,
		                actual=self.page.first_name,
		                act=None,
		                step_description='Verify "First Name" field value')

		step_definition(self,
		                expected=self.client.last_name,
		                actual=self.page.last_name,
		                act=None,
		                step_description='Verify "Last Name" field value')

		step_definition(self,
		                expected=self.client.address,
		                actual=self.page.address,
		                act=None,
		                step_description='Verify "Address" field value')

		step_definition(self,
		                expected=self.client.city,
		                actual=self.page.city,
		                act=None,
		                step_description='Verify "City" field value')

		step_definition(self,
		                expected=self.client.state,
		                actual=self.page.state,
		                act=None,
		                step_description='Verify "State" field value')

		step_definition(self,
		                expected=self.client.zip_code,
		                actual=self.page.zip_code,
		                act=None,
		                step_description='Verify "Zip Code" field value')

		step_definition(self,
		                expected=self.client.ssn,
		                actual=self.page.ssn,
		                act=None,
		                step_description='Verify "SSN" field value')

		step_definition(self,
		                expected=self.client.phone,
		                actual=self.page.phone,
		                act=None,
		                step_description='TVerify "Phone" field value',
		                click=False)

		step_definition(self,
		                expected=self.client.username,
		                actual=self.page.username,
		                act=None,
		                step_description='TVerify "Username" field value',
		                click=False)

		step_definition(self,
		                expected='',
		                actual=self.page.password,
		                act=None,
		                step_description='Verify that "Password" field vis empty',
		                click=False)

		step_definition(self,
		                expected='',
		                actual=self.page.confirm,
		                act=None,
		                step_description='Verify that "Confirm" field is empty',
		                click=False)
