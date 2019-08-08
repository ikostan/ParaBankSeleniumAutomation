import allure
from utils.screenshot import screenshot_on_fail
from tests.context_tests.base_cases.base_context_case import BaseContextCase
from expected_results.page_context.about_page_context import AboutPageContext


@allure.feature("About Page")
@allure.story('About Context')
@allure.suite('About Page Context Test Suite')
@screenshot_on_fail()
class AboutPageContextCase(BaseContextCase):

	def verify_page_url(self):

		allure.dynamic.severity(allure.severity_level.CRITICAL)

		with allure.step("About page URL test"):
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

