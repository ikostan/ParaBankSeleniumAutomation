import allure
from utils.screenshot import screenshot_on_fail
from expected_results.page_context.register_page_context import RegisterPageContext
from tests.context_tests.base_cases.base_personal_context_case import BasePersonalInfoContextCase


@allure.story('Register Context')
@allure.suite('Register Page Context Test Suite')
@screenshot_on_fail()
class RegisterContextCase(BasePersonalInfoContextCase):

	def verify_page_url(self):

		with allure.step('Verify "Register" web page URL. Expected result: {}'.format(RegisterPageContext.URL)):
			self.assertEqual(RegisterPageContext.URL,
			                 self.page.url)

	def verify_page_title(self):

		with allure.step('Verify "Register" web page title. Expected result: {}'.format(RegisterPageContext.TITLE)):
			self.assertEqual(RegisterPageContext.TITLE,
			                 self.page.title)

	def verify_username_title(self):

		expected = RegisterPageContext.FORM['username']['title']
		with allure.step('Verify "Username" title. Expected result: {}'.format(expected)):
			self.assertEqual(expected, self.page.username_title)

	def verify_password_title(self):
		expected = RegisterPageContext.FORM['password']['title']
		with allure.step('Verify "Password" title. Expected result: {}'.format(expected)):
			self.assertEqual(expected, self.page.password_title)

	def verify_confirm_title(self):

		expected = RegisterPageContext.FORM['confirm']['title']
		with allure.step('Verify "Confirm" title. Expected result: {}'.format(expected)):
			self.assertEqual(expected, self.page.confirm_title)

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
