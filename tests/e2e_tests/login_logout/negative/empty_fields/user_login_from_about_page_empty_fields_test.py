#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
import unittest

from tests.config import Config
from utils.clean_database import clean_database
from utils.screenshot import screenshot_on_fail
from utils.open_web_browser import open_web_browser
from utils.step_definition import step_definition

from expected_results.users.base_user import BaseUser
from page_object_models.about_page_model import AboutPageModel
from expected_results.page_content.about_page_content import AboutPageContent
from expected_results.page_content.login_page_content import LoginPageContent
from expected_results.users.invalid_users_templates.no_such_user import NoSuchUser


@allure.epic('Page Functionality')
@allure.parent_suite('End To End')
@allure.suite("User Login/Logout")
@allure.sub_suite('Negative Tests')
@allure.feature("About Page")
@allure.story('Login/Logout Functionality')
@pytest.mark.skipif(get_args()['env'] == 'production',
                   reason="This is demo test that will have negative effect on Travis CI status")
@screenshot_on_fail()
class TestUserLoginFromAboutPageEmptyFieldsError(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.user = BaseUser(NoSuchUser)
		cls.page_model = AboutPageModel
		cls.page_content = AboutPageContent
		cls.config = Config()

		with allure.step("Initial data setup > clean DB"):
			clean_database(cls.config)

		with allure.step("Open web browser"):
			cls.page = open_web_browser(config=cls.config,
			                            page_model=cls.page_model,
			                            page_content=cls.page_content)

	@classmethod
	def tearDownClass(cls):
		with allure.step("Close web browser"):
			if cls.page:
				cls.page.quit()
				cls.page = None

	def test_user_login_logout(self):
		allure.dynamic.description("""
				User Log In validation > Negative test (no such user):
					1. Open About web page
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
		allure.dynamic.title("About page > User Log In validation > Negative test > No such user")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		step_definition(self,
		                step_description='Type Username > Verify Username value',
		                expected=self.user.username,
		                actual=self.page.username,
		                act=self.page.enter_username,
		                click=False)

		step_definition(self,
		                step_description='Type Password > Verify Password value',
		                expected=self.user.password,
		                actual=self.page.password,
		                act=self.page.enter_password,
		                click=False)

		with allure.step('Hit Log In button'):
			self.page = self.page.hit_login_button()

		step_definition(self,
		                step_description='Verify that "Account Services" menu is not present',
		                expected=False,
		                actual=self.page.account_services_menu_is_visible,
		                act=None,
		                click=False)

		# Verify ERROR title
		step_definition(self,
		                step_description='Verify Error title',
		                expected=LoginPageContent.ERROR_TITLE,
		                actual=self.page.error_title,
		                act=None,
		                click=False)

		# Verify ERROR message
		step_definition(self,
		                step_description='Verify Error message',
		                expected=LoginPageContent.NO_SUCH_USER_ERROR_MESSAGE,
		                actual=self.page.error_message,
		                act=None,
		                click=False)

		# URL validation
		step_definition(self,
		                step_description='Do URL verification',
		                expected=self.config.base_url + LoginPageContent.URL,
		                actual=self.page.url,
		                act=None,
		                click=False)


