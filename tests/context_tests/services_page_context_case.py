import allure
from utils.screenshot import screenshot_on_fail
from tests.context_tests.base_cases.base_context_case import BaseContextCase
from expected_results.page_context.services_page_context import ServicesPageContext


@allure.story('Services Context')
@allure.suite('Services Page Context Test Suite')
@screenshot_on_fail()
class ServicesPageContextCase(BaseContextCase):

	def verify_page_url(self):

		allure.dynamic.severity(allure.severity_level.BLOCKER)
		with allure.step('Verify "Services" web page URL. Expected result: {}'.format(ServicesPageContext.URL)):
			self.assertEqual(ServicesPageContext.URL,
			                 self.page.url)

	def verify_page_title(self):
		allure.dynamic.severity(allure.severity_level.MINOR)
		with allure.step('Verify "Services" web page title. Expected result: {}'.format(ServicesPageContext.TITLE)):
			self.assertEqual(ServicesPageContext.TITLE,
			                 self.page.title)

