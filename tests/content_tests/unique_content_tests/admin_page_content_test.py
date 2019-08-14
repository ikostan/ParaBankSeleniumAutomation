#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
import unittest

from utils.screenshot import screenshot_on_fail
from utils.open_web_browser import open_web_browser
from utils.browser_configuration import browser_configuration

from page_object_models.admin_page_model import AdminPageModel
from expected_results.page_content.admin_page_content import AdminPageContent
from utils.step_definition import step_definition


@allure.epic('Page Content')
@allure.parent_suite('Page Unique Content')
@allure.suite('Admin Page Content')
@allure.sub_suite("Admin Page Unique Content")
@allure.feature("Admin Page")
@allure.story('Admin Content')
@screenshot_on_fail()
class TestAdminPageContent(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		with allure.step("Open web browser"):
			cls.browser = browser_configuration()
			cls.page_model = AdminPageModel
			cls.page_content = AdminPageContent
			cls.page = open_web_browser(browser=cls.browser,
			                            page_model=cls.page_model,
			                            page_content=cls.page_content)

	@classmethod
	def tearDownClass(cls):
		with allure.step("Close web browser"):
			if cls.page:
				cls.page.quit()
				cls.page = None

	def test_page_url(self):
		allure.dynamic.description("""
		Content base elements validation > Admin page URL:
			1. Open Admin web page
			2. Do URL verification
		""")
		allure.dynamic.title("Web page URL test")
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		# verify web page url
		step_definition(self,
		                expected=AdminPageContent.URL,
		                actual=self.page.url,
		                act=None,
		                step_description='Admin page URL test')
		'''
		with allure.step("Admin page URL test"):
			self.assertEqual(AdminPageContent.URL,
			                 self.page.url)
		'''

	def test_page_title(self):
		allure.dynamic.description("""
		Content base elements validation > Admin page URL:
			1. Open Admin web page
			2. Do Title verification
		""")
		allure.dynamic.title("Web page Title test")
		allure.dynamic.severity(allure.severity_level.MINOR)

		# verify web page url
		step_definition(self,
		                expected=AdminPageContent.TITLE,
		                actual=self.page.title,
		                act=None,
		                step_description="Admin page title test")
		'''
		with allure.step("Admin page title test"):
			self.assertEqual(AdminPageContent.TITLE,
			                 self.page.title)
		'''
