#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure

from utils.screenshot import screenshot_on_fail
from utils.step_definition import step_definition

from expected_results.page_content.services_page_content import ServicesPageContent
from tests.content_tests.content_cases.base_cases.base_content_case import BaseContentCase


@screenshot_on_fail()
class ServicesPageContentCase(BaseContentCase):

	def verify_page_url(self):

		expected = ServicesPageContent.URL
		actual = self.page.url
		step_description = 'Verify "Services" web page URL'
		severity = allure.severity_level.BLOCKER

		step_definition(self, expected, actual, step_description, severity)
	'''
	def verify_page_url(self):

		allure.dynamic.severity(allure.severity_level.BLOCKER)
		with allure.step('Verify "Services" web page URL. Expected result: {}'.format(ServicesPageContext.URL)):
			self.assertEqual(ServicesPageContext.URL, self.page.url)
	'''

	def verify_page_title(self):
		allure.dynamic.severity(allure.severity_level.MINOR)
		with allure.step('Verify "Services" web page title. Expected result: {}'.format(ServicesPageContent.TITLE)):
			self.assertEqual(ServicesPageContent.TITLE, self.page.title)

