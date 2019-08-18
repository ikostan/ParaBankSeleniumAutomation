#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
import unittest

from utils.screenshot import screenshot_on_fail
from utils.step_definition import step_definition
from utils.open_web_browser import open_web_browser

from expected_results.users.base_user import BaseUser
from expected_results.users.invalid_users_templates.empty_fields import EmptyFields

from page_object_models.contact_page_model import ContactPageModel
from expected_results.page_content.contact_page_content import ContactPageContent


@allure.epic('Page Functionality')
@allure.parent_suite('End To End')
@allure.suite("Customer Care")
@allure.sub_suite('Negative Tests')
@allure.feature("Customer Care Page")
@allure.story('Customer Care Functionality')
@screenshot_on_fail()
class TestCustomerCareEmptyFieldsCase(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.client = BaseUser(EmptyFields)
		cls.page = None
		cls.page_model = ContactPageModel
		cls.page_content = ContactPageContent
		cls.message = ""

		with allure.step("Initial data setup: {}".format(ContactPageContent.URL)):
			with allure.step("Open web browser"):
				cls.page = open_web_browser(page_model=cls.page_model,
				                            page_content=cls.page_content)

	@classmethod
	def tearDownClass(cls):
		with allure.step("Close Web Browser"):
			if cls.page:
				cls.page.quit()
				cls.page = None

	def test_user_registration(self):
		allure.dynamic.description("""
		Forgot Login Info test case:
			1. Open 'Forgot Customer Care' web page
			2. Fill out user personal data > Empty Fields
			3. Verify that each data item (empty string) appears in relevant field
			4. Hit 'SEND TO CUSTOMER CARE' button
			5. Verify Errors
			6. Verify that "Thank you" line does not appear
			7. Verify that "Success" message does not appear
			8. Verify web page URL
			9. Verify web page title
			10. Close web browser
		""")
		allure.dynamic.title("Customer Care > Send Message > Negative Test > Empty Fields")
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		step_definition(self,
		                expected='{}'.format(self.client.first_name),
		                actual=self.page.name_field,
		                act=self.page.type_name,
		                step_description='Type Name > Verify "Name" field value',
		                click=False)

		step_definition(self,
		                expected='{}'.format(self.client.email),
		                actual=self.page.email_field,
		                act=self.page.type_email,
		                step_description='Type Email > Verify "Email" field value',
		                click=False)

		step_definition(self,
		                expected='{}'.format(self.client.phone),
		                actual=self.page.phone_field,
		                act=self.page.type_phone,
		                step_description='Type Phone > Verify "Phone" field value',
		                click=False)

		step_definition(self,
		                expected='{}'.format(self.message),
		                actual=self.page.message_field,
		                act=self.page.type_message,
		                step_description='Type Message',
		                click=False)

		step_definition(self,
		                expected=True,
		                actual=True,
		                act=self.page.click_send_btn,
		                step_description='Hit "SEND TO CUSTOMER CARE" button',
		                click=True)

		# Verify Name error message
		step_definition(self,
		                expected=ContactPageContent.CONTACT_FORM['name']['error'],
		                actual=self.page.name_error,
		                act=None,
		                step_description='Verify Name error',
		                click=False)

		# Verify Email error message
		step_definition(self,
		                expected=ContactPageContent.CONTACT_FORM['email']['error'],
		                actual=self.page.email_error,
		                act=None,
		                step_description='Verify Email error',
		                click=False)

		# Verify Email error message
		step_definition(self,
		                expected=ContactPageContent.CONTACT_FORM['phone']['error'],
		                actual=self.page.phone_error,
		                act=None,
		                step_description='Verify Phone error',
		                click=False)

		# Verify Message error
		step_definition(self,
		                expected=ContactPageContent.CONTACT_FORM['message']['error'],
		                actual=self.page.message_error,
		                act=None,
		                step_description='Verify Message error',
		                click=False)

		# Verify Thank you message
		step_definition(self,
		                expected=None,
		                actual=self.page.thank_you_message,
		                act=None,
		                step_description='Verify "Thank you" line',
		                click=False)

		# Verify Success message
		step_definition(self,
		                expected=None,
		                actual=self.page.success_message,
		                act=None,
		                step_description='Verify "Success" message',
		                click=False)

		# Verify Page URL
		step_definition(self,
		                expected=ContactPageContent.URL,
		                actual=self.page.url,
		                act=None,
		                step_description='Verify web page URL',
		                click=False)

		# Verify Page Title
		step_definition(self,
		                expected=ContactPageContent.TITLE,
		                actual=self.page.title,
		                act=None,
		                step_description='Verify web page title',
		                click=False)

