#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
import unittest

from utils.screenshot import screenshot_on_fail
from utils.step_definition import step_definition
from utils.open_web_browser import open_web_browser

from expected_results.users.base_user import BaseUser
from expected_results.users.valid_users_templates.john_doe import JohnDoe

from page_object_models.contact_page_model import ContactPageModel
from expected_results.page_content.contact_page_content import ContactPageContent


@allure.epic('Page Functionality')
@allure.parent_suite('End To End')
@allure.suite("Customer Care")
@allure.sub_suite('Positive Tests')
@allure.feature("Customer Care Page")
@allure.story('Customer Care Functionality')
@screenshot_on_fail()
class TestCustomerCareCase(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.client = BaseUser(JohnDoe)
		cls.page = None
		cls.page_model = ContactPageModel
		cls.page_content = ContactPageContent
		cls.message = "Hello there. This is test message. Thanks"

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
			2. Fill out user personal data > Set all fields with valid data
			3. Verify that each data item (empty string) appears in relevant field
			4. Hit 'SEND TO CUSTOMER CARE' button
			5. Verify web page title
			6. Verify "Thank you" line
			7. Verify "Success" message
			8. Verify web page URL
			9. Close web browser
		""")
		allure.dynamic.title("Customer Care > Send Message > Positive Test")
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		step_definition(self,
		                expected='{} {}'.format(self.client.first_name,
		                                        self.client.last_name),
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

		# Verify Page Title
		step_definition(self,
		                expected=ContactPageContent.TITLE,
		                actual=self.page.title,
		                act=None,
		                step_description='Verify web page title',
		                click=False)

		# Verify Page URL
		step_definition(self,
		                expected=ContactPageContent.URL,
		                actual=self.page.url,
		                act=None,
		                step_description='Verify web page URL',
		                click=False)

		# Verify Thank you message
		step_definition(self,
		                expected='{}{} {}'.format(ContactPageContent.THANK_YOU,
		                                          self.client.first_name,
		                                          self.client.last_name),
		                actual=self.page.thank_you_message,
		                act=None,
		                step_description='Verify "Thank you" line',
		                click=False)

		# Verify Success message
		step_definition(self,
		                expected=ContactPageContent.SUCCESS_MESSAGE,
		                actual=self.page.success_message,
		                act=None,
		                step_description='Verify "Success" message',
		                click=False)

