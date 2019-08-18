#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure

from utils.screenshot import screenshot_on_fail
from utils.open_web_browser import open_web_browser
from utils.step_definition import step_definition

from page_object_models.register_page_model import RegisterPageModel
from expected_results.page_content.register_page_content import RegisterPageContent
from tests.content_tests.base_cases.base_personal_info_content_case import BasePersonalInfoContentCase


@allure.epic('Page Content')
@allure.parent_suite('Page Unique Content')
@allure.suite('Register Page Content')
@allure.sub_suite("Register Page Unique Content")
@allure.feature("Register Page")
@allure.story('Register Content')
@screenshot_on_fail()
class TestRegisterPageContent(BasePersonalInfoContentCase):

	@classmethod
	def setUpClass(cls):
		with allure.step("Open web browser"):
			cls.page_model = RegisterPageModel
			cls.page_content = RegisterPageContent
			cls.page = open_web_browser(page_model=cls.page_model,
			                            page_content=cls.page_content)

	@classmethod
	def tearDownClass(cls):
		with allure.step("Close web browser"):
			if cls.page:
				cls.page.quit()
				cls.page = None

	# Generic/Base context
	def test_page_url(self):
		allure.dynamic.description("""
		ontext base elements validation > Register page URL:
			1. Open Register page web page
			2. Do URL verification
		""")
		allure.dynamic.title("Web page URL test")
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		# Verify web page url
		step_definition(self,
		                step_description='Verify "Register" web page URL',
		                expected=RegisterPageContent.URL,
		                actual=self.page.url,
		                act=None,
		                click=False)
		'''
		with allure.step('Verify "Register" web page URL. Expected result: {}'.format(RegisterPageContent.URL)):
			self.assertEqual(RegisterPageContent.URL,
			                 self.page.url())
		'''

	def test_page_title(self):
		allure.dynamic.description("""
		Content base elements validation > Register page title:
			1. Open Register page web page
			2. Do Register page title verification
		""")
		allure.dynamic.title("Register page title test")
		allure.dynamic.severity(allure.severity_level.MINOR)

		# Verify web page title
		step_definition(self,
		                step_description='Verify "Register" web page title',
		                expected=RegisterPageContent.TITLE,
		                actual=self.page.title,
		                act=None,
		                click=False)
		'''
		with allure.step('Verify "Register" web page title. Expected result: {}'.format(RegisterPageContent.TITLE)):
			self.assertEqual(RegisterPageContent.TITLE,
			                 self.page.title())
		'''

	# Registration page context - Personal Info Content base elements validation
	def test_first_name_title(self):
		allure.dynamic.description("""
		Content base elements validation > Register Form:
			1. Open Register web page
			2. Do First Name title verification
		""")
		allure.dynamic.title("First Name title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# Personal Info Content base elements validation:
		self.verify_first_name_title()

	def test_last_name_title(self):
		allure.dynamic.description("""
		Content base elements validation > Register Form:
			1. Open Register web page
			2. Do Last Name title verification
		""")
		allure.dynamic.title("Last Name title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# Personal Info Content base elements validation:
		self.verify_last_name_title()

	def test_address_title(self):
		allure.dynamic.description("""
		Content base elements validation > Register Form:
			1. Open Register web page
			2. Do Address title verification
		""")
		allure.dynamic.title("Address title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# Personal Info Content base elements validation:
		self.verify_address_title()

	def test_city_title(self):
		allure.dynamic.description("""
		Content base elements validation > Register Form:
			1. Open Register web page
			2. Do City title verification
		""")
		allure.dynamic.title("City title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# Personal Info Content base elements validation:
		self.verify_city_title()

	def test_state_title(self):
		allure.dynamic.description("""
		Content base elements validation > Register Form:
			1. Open Register web page
			2. Do State title verification
		""")
		allure.dynamic.title("State title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# Personal Info Content base elements validation:
		self.verify_state_title()

	def test_zip_code_title(self):
		allure.dynamic.description("""
		Content base elements validation > Register Form:
			1. Open Register web page
			2. Do Zip Code title verification
		""")
		allure.dynamic.title("Zip Code title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# Personal Info Content base elements validation:
		self.verify_zip_code_title()

	def test_phone_title(self):
		allure.dynamic.description("""
		Content base elements validation > Register Form:
			1. Open Register web page
			2. Do Phone title verification
		""")
		allure.dynamic.title("Phone title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# Personal Info Content base elements validation:
		self.verify_phone_title()

	def test_ssn_title(self):
		allure.dynamic.description("""
		Content base elements validation > Register Form:
			1. Open Register web page
			2. Do SSN title verification
		""")
		allure.dynamic.title("SSN title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# Personal Info Content base elements validation:
		self.verify_ssn_title()

	# Registration page context - Register web page context base elements validation
	def test_username_title(self):
		allure.dynamic.description("""
		Content base elements validation > Register Form:
			1. Open Register web page
			2. Do Username title verification
		""")
		allure.dynamic.title("Username title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# Register web page elements validation:
		step_definition(self,
		                step_description='Verify "Username" title',
		                expected=RegisterPageContent.FORM['username']['title'],
		                actual=self.page.username_title,
		                act=None,
		                click=False)
		'''
		expected = RegisterPageContent.FORM['username']['title']
		with allure.step('Verify "Username" title. Expected result: {}'.format(expected)):
			self.assertEqual(expected, self.page.username_title())
		'''

	def test_password_title(self):
		allure.dynamic.description("""
		Content base elements validation > Register Form:
			1. Open Register web page
			2. Do Password title verification
		""")
		allure.dynamic.title("Password title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# Register web page elements validation:
		step_definition(self,
		                step_description='Verify "Password" title',
		                expected=RegisterPageContent.FORM['password']['title'],
		                actual=self.page.password_title,
		                act=None,
		                click=False)
		'''
		expected = RegisterPageContent.FORM['password']['title']
		with allure.step('Verify "Password" title. Expected result: {}'.format(expected)):
			self.assertEqual(expected, self.page.password_title())
		'''

	def test_confirm_title(self):
		allure.dynamic.description("""
		Content base elements validation > Register Form:
			1. Open Register web page
			2. Do Confirm title verification
		""")
		allure.dynamic.title("Confirm title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# Register web page elements validation:
		step_definition(self,
		                step_description='Verify "Confirm" title',
		                expected=RegisterPageContent.FORM['confirm']['title'],
		                actual=self.page.confirm_title,
		                act=None,
		                click=False)
		'''
		expected = RegisterPageContent.FORM['confirm']['title']
		with allure.step('Verify "Confirm" title. Expected result: {}'.format(expected)):
			self.assertEqual(expected, self.page.confirm_title())
		'''

	def test_register_button(self):
		allure.dynamic.description("""
		Content base elements validation > Register Form:
			1. Open Register web page
			2. Do "Register" button verification
		""")
		allure.dynamic.title("\"Register\" button test")
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		# Register web page elements validation:
		step_definition(self,
		                step_description='Verify "Register" button label',
		                expected=RegisterPageContent.REGISTER_BUTTON['value'],
		                actual=self.page.register_btn_label,
		                act=None,
		                click=False)
		'''
		with allure.step('Verify "Register" button label. Expected result: {}'.format(
				RegisterPageContent.REGISTER_BUTTON['value'])):
			self.assertEqual(RegisterPageContent.REGISTER_BUTTON['value'], self.page.register_btn_label())
		'''

		step_definition(self,
		                step_description='Verify "Register" button class',
		                expected=RegisterPageContent.REGISTER_BUTTON['class'],
		                actual=self.page.register_btn_class,
		                act=None,
		                click=False)
		'''
		with allure.step('Verify "Register" button class. Expected result: {}'.format(
				RegisterPageContent.REGISTER_BUTTON['class'])):
			self.assertEqual(RegisterPageContent.REGISTER_BUTTON['class'], self.page.register_btn_class())
		'''

		step_definition(self,
		                step_description='Verify "Register" button type',
		                expected=RegisterPageContent.REGISTER_BUTTON['type'],
		                actual=self.page.register_btn_type,
		                act=None,
		                click=False)
		'''
		with allure.step('Verify "Register" button type. Expected result: {}'.format(
				RegisterPageContent.REGISTER_BUTTON['type'])):
			self.assertEqual(RegisterPageContent.REGISTER_BUTTON['type'], self.page.register_btn_type())
		'''

