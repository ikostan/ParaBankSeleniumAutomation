import allure
from utils.screenshot import screenshot_on_fail
from expected_results.page_context.register_page_context import RegisterPageContext
from tests.context_tests.base_tests.base_personal_context_case import BasePersonalInfoContextCase


@allure.feature("Register Page")
@allure.story('Register Context')
@allure.suite('Register Page Context Test Suite')
@screenshot_on_fail()
class RegisterContextCase(BasePersonalInfoContextCase):

	'''
	@staticmethod
	def open_web_browser(browser):

		# with allure.step('Open web browser on: {}'.format(RegisterPageContext.URL)):
		# Open web page
		driver = Driver(browser)
		page = RegisterPageModel(driver=driver, implicit_wait_time=5, explicit_wait_time=10)
		page.go()
		refresh_page(RegisterPageContext.TITLE, page)
		return page
	'''

	# Register Page Context
	# @allure.feature("Register Page")
	def verify_page_url(self):

		with allure.step('Verify "Register" web page URL. Expected result: {}'.format(RegisterPageContext.URL)):
			self.assertEqual(RegisterPageContext.URL,
			                 self.page.url)

	# @allure.feature("Register Page")
	def verify_page_title(self):

		with allure.step('Verify "Register" web page title. Expected result: {}'.format(RegisterPageContext.TITLE)):
			self.assertEqual(RegisterPageContext.TITLE,
			                 self.page.title)

	# @allure.feature("Register Page")
	def verify_username_title(self):

		expected = RegisterPageContext.FORM['username']['title']
		with allure.step('Verify "Username" title. Expected result: {}'.format(expected)):
			self.assertEqual(expected, self.page.username_title)

	# @allure.feature("Register Page")
	def verify_password_title(self):
		expected = RegisterPageContext.FORM['password']['title']
		with allure.step('Verify "Password" title. Expected result: {}'.format(expected)):
			self.assertEqual(expected, self.page.password_title)

	# @allure.feature("Register Page")
	def verify_confirm_title(self):

		expected = RegisterPageContext.FORM['confirm']['title']
		with allure.step('Verify "Confirm" title. Expected result: {}'.format(expected)):
			self.assertEqual(expected, self.page.confirm_title)

	# @allure.feature("Register Page")
	def verify_register_button(self):

		with allure.step('Verify "Register" button label. Expected result: {}'.format(
				RegisterPageContext.REGISTER_BUTTON['value'])):
			self.assertEqual(RegisterPageContext.REGISTER_BUTTON['value'], self.page.register_btn_label)

		with allure.step('Verify "Register" button class. Expected result: {}'.format(
				RegisterPageContext.REGISTER_BUTTON['class'])):
			self.assertEqual(RegisterPageContext.REGISTER_BUTTON['class'], self.page.register_btn_class)

		with allure.step('Verify "Register" button type. Expected result: {}'.format(
				RegisterPageContext.REGISTER_BUTTON['type'])):
			self.assertEqual(RegisterPageContext.REGISTER_BUTTON['type'], self.page.register_btn_type)

	# "Base Personal Info Context"
