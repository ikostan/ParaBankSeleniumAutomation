#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure

from utils.screenshot import screenshot_on_fail

from expected_results.page_content.admin_page_content import AdminPageContent
from tests.content_tests.content_cases.base_cases.base_content_case import BaseContentCase


@screenshot_on_fail()
class AdminPageContentCase(BaseContentCase):

	def verify_page_url(self):

		allure.dynamic.severity(allure.severity_level.CRITICAL)
		with allure.step("Admin page URL test"):
			self.assertEqual(AdminPageContent.URL,
			                 self.page.url)

	def verify_page_title(self):

		allure.dynamic.severity(allure.severity_level.MINOR)
		with allure.step("Admin page title test"):
			self.assertEqual(AdminPageContent.TITLE,
			                 self.page.title)
