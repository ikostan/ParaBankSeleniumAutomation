#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure

from utils.screenshot import screenshot_on_fail
from utils.open_web_browser import open_web_browser
from utils.browser_configuration import browser_configuration

from page_object_models.services_page_model import ServicesPageModel
from expected_results.page_content.services_page_content import ServicesPageContent
from tests.content_tests.content_cases.services_page_content_case import ServicesPageContentCase


@allure.epic('Page Context')
@allure.parent_suite('Page Unique Context')
@allure.suite('Services Page Context')
@allure.sub_suite("Services Page Unique Context")
@allure.feature("Services Page")
@allure.story('Services Context')
@screenshot_on_fail()
class TestServicesPageContext(ServicesPageContentCase):

	@classmethod
	def setUpClass(cls):
		with allure.step("Open web browser"):
			cls.browser = browser_configuration()
			cls.page_model = ServicesPageModel
			cls.page_context = ServicesPageContent
			cls.page = open_web_browser(browser=cls.browser,
			                            page_model=cls.page_model,
			                            page_context=cls.page_context)

	@classmethod
	def tearDownClass(cls):
		with allure.step("Close web browser"):
			if cls.page:
				cls.page.quit()
				cls.page = None

	@allure.feature("Services Page")
	def test_page_url(self):
		allure.dynamic.description("""
		Context base elements validation > Services page URL:
			1. Open Services web page
			2. Do URL verification
		""")
		allure.dynamic.title("Web page URL test")
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		# Verify web page url
		self.verify_page_url()

	@allure.feature("Services Page")
	def test_page_title(self):
		allure.dynamic.description("""
		Context base elements validation > Services page title:
			1. Open Services web page
			2. Do Services page title verification
		""")
		allure.dynamic.title("Services page title test")
		allure.dynamic.severity(allure.severity_level.MINOR)

		# Verify web page title
		self.verify_page_title()

	# Services Context Testing

