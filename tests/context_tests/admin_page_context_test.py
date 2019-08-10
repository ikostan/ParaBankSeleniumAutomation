#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure

from utils.screenshot import screenshot_on_fail
from utils.open_web_browser import open_web_browser
from utils.browser_configuration import browser_configuration

from page_models.admin_page_model import AdminPageModel
from expected_results.page_context.admin_page_context import AdminPageContext
from tests.context_tests.context_cases.admin_page_context_case import AdminPageContextCase


@allure.epic('Page Context')
@allure.parent_suite('Page Unique Context')
@allure.suite('Admin Page Context')
@allure.sub_suite("Admin Page Unique Context")
@allure.feature("Admin Page")
@allure.story('Admin Context')
@screenshot_on_fail()
class TestAdminPageContext(AdminPageContextCase):

	@classmethod
	def setUpClass(cls):
		with allure.step("Open web browser"):
			cls.browser = browser_configuration()
			cls.page_model = AdminPageModel
			cls.page_context = AdminPageContext
			cls.page = open_web_browser(browser=cls.browser,
			                            page_model=cls.page_model,
			                            page_context=cls.page_context)

	@classmethod
	def tearDownClass(cls):
		with allure.step("Close web browser"):
			if cls.page:
				cls.page.quit()
				cls.page = None

	def test_page_url(self):
		allure.dynamic.description("""
		Context base elements validation > Admin page URL:
			1. Open Admin web page
			2. Do URL verification
		""")
		allure.dynamic.title("Web page URL test")

		# verify web page url
		self.verify_page_url()

	def test_page_title(self):
		allure.dynamic.description("""
		Context base elements validation > Admin page URL:
			1. Open Admin web page
			2. Do Title verification
		""")
		allure.dynamic.title("Web page Title test")

		# verify web page url
		self.verify_page_title()
