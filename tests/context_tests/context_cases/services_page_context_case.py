#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure

from utils.screenshot import screenshot_on_fail
from utils.step_definition import step_definition

from expected_results.page_context.services_page_context import ServicesPageContext
from tests.context_tests.context_cases.base_cases.base_context_case import BaseContextCase


@screenshot_on_fail()
class ServicesPageContextCase(BaseContextCase):

	def verify_page_url(self):

		expected = ServicesPageContext.URL
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
		with allure.step('Verify "Services" web page title. Expected result: {}'.format(ServicesPageContext.TITLE)):
			self.assertEqual(ServicesPageContext.TITLE, self.page.title)

