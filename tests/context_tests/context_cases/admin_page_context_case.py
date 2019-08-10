#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
from utils.screenshot import screenshot_on_fail
from expected_results.page_context.admin_page_context import AdminPageContext
from tests.context_tests.context_cases.base_cases.base_context_case import BaseContextCase


@screenshot_on_fail()
class AdminPageContextCase(BaseContextCase):

	def verify_page_url(self):

		allure.dynamic.severity(allure.severity_level.CRITICAL)
		with allure.step("Admin page URL test"):
			self.assertEqual(AdminPageContext.URL,
			                 self.page.url)

	def verify_page_title(self):

		allure.dynamic.severity(allure.severity_level.MINOR)
		with allure.step("Admin page title test"):
			self.assertEqual(AdminPageContext.TITLE,
			                 self.page.title)
