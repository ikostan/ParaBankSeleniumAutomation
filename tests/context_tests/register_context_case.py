import allure
from utils.driver import Driver
from utils.screenshot import screenshot_on_fail
from page_models.register_page_model import RegisterPageModel
from tests.context_tests.base_context_case import TestBaseContextCase
from expected_results.page_context.register_page_context import RegisterPageContext
from tests.context_tests.base_personal_context_case import BasePersonalInfoContextTestCase


@allure.feature("Register Page")
@allure.story('Register Context')
@allure.suite('Register Page Context Test Suite')
@screenshot_on_fail()
class RegisterContextTestCase(BasePersonalInfoContextTestCase, TestBaseContextCase):

	def open_web_browser(self, browser):
		with allure.step('Open web browser on: {}'.format(RegisterPageContext.URL)):
			# Open web page
			driver = Driver(browser)
			self.page = RegisterPageModel(driver=driver, implicit_wait_time=5, explicit_wait_time=10)
			self.page.go()

	@allure.feature("Register Page")
	def verify_page_url(self):

		allure.dynamic.severity(allure.severity_level.BLOCKER)
		with allure.step('Verify "Register" web page URL. Expected result: {}'.format(RegisterPageContext.URL)):
			self.assertEqual(RegisterPageContext.URL,
			                 self.page.url)

	@allure.feature("Register Page")
	def verify_page_title(self):
		allure.dynamic.severity(allure.severity_level.MINOR)
		with allure.step('Verify "Register" web page title. Expected result: {}'.format(RegisterPageContext.TITLE)):
			self.assertEqual(RegisterPageContext.TITLE,
			                 self.page.title)

