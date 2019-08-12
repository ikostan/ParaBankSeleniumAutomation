#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
from utils.screenshot import screenshot_on_fail
from expected_results.page_context.about_page_context import AboutPageContext
from tests.content_tests.content_cases.base_cases.base_content_case import BaseContextCase


@screenshot_on_fail()
class AboutPageContentCase(BaseContextCase):

	def verify_page_url(self):

		allure.dynamic.severity(allure.severity_level.CRITICAL)

		with allure.step("About Web Page URL test"):
			self.assertEqual(AboutPageContext.URL,
			                 self.page.url)

	def verify_page_title(self):

		allure.dynamic.severity(allure.severity_level.MINOR)

		with allure.step("About Web Page Title test"):
			self.assertEqual(AboutPageContext.TITLE,
			                 self.page.title)

	def verify_description_title(self):
		allure.dynamic.severity(allure.severity_level.MINOR)

		# Context About page elements validation:
		with allure.step("Description header test"):
			self.assertEqual(AboutPageContext.DESCRIPTION['title'], self.page.description_title)

	def verify_description_text(self):
		allure.dynamic.severity(allure.severity_level.MINOR)

		# Context About page elements validation:
		with allure.step("Description text (first paragraph) test"):
			self.assertEqual(AboutPageContext.DESCRIPTION['text'][0], self.page.description_first_line)

		with allure.step("Description text (second paragraph) test"):
			self.assertEqual(AboutPageContext.DESCRIPTION['text'][1], self.page.description_second_line)

		with allure.step("Description text (third paragraph) test"):
			self.assertEqual(AboutPageContext.DESCRIPTION['text'][2], self.page.description_third_line)

		with allure.step("Description text (fourth paragraph) test"):
			self.assertEqual(AboutPageContext.LINK, self.page.description_link)

