#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
from utils.screenshot import screenshot_on_fail
from expected_results.page_content.register_page_content import RegisterPageContent
from tests.content_tests.content_cases.base_cases.base_personal_info_content_case import BasePersonalInfoContentCase


@screenshot_on_fail()
class RegisterPageContentCase(BasePersonalInfoContentCase):

	def verify_page_url(self):

		with allure.step('Verify "Register" web page URL. Expected result: {}'.format(RegisterPageContent.URL)):
			self.assertEqual(RegisterPageContent.URL,
			                 self.page.url)

	def verify_page_title(self):

		with allure.step('Verify "Register" web page title. Expected result: {}'.format(RegisterPageContent.TITLE)):
			self.assertEqual(RegisterPageContent.TITLE,
			                 self.page.title)

	def verify_username_title(self):

		expected = RegisterPageContent.FORM['username']['title']
		with allure.step('Verify "Username" title. Expected result: {}'.format(expected)):
			self.assertEqual(expected, self.page.username_title)

	def verify_password_title(self):
		expected = RegisterPageContent.FORM['password']['title']
		with allure.step('Verify "Password" title. Expected result: {}'.format(expected)):
			self.assertEqual(expected, self.page.password_title)

	def verify_confirm_title(self):

		expected = RegisterPageContent.FORM['confirm']['title']
		with allure.step('Verify "Confirm" title. Expected result: {}'.format(expected)):
			self.assertEqual(expected, self.page.confirm_title)

	def verify_register_button(self):

		with allure.step('Verify "Register" button label. Expected result: {}'.format(
				RegisterPageContent.REGISTER_BUTTON['value'])):
			self.assertEqual(RegisterPageContent.REGISTER_BUTTON['value'], self.page.register_btn_label)

		with allure.step('Verify "Register" button class. Expected result: {}'.format(
				RegisterPageContent.REGISTER_BUTTON['class'])):
			self.assertEqual(RegisterPageContent.REGISTER_BUTTON['class'], self.page.register_btn_class)

		with allure.step('Verify "Register" button type. Expected result: {}'.format(
				RegisterPageContent.REGISTER_BUTTON['type'])):
			self.assertEqual(RegisterPageContent.REGISTER_BUTTON['type'], self.page.register_btn_type)

	# "Base Personal Info Context"
