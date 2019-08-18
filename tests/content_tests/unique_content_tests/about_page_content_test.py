#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
import unittest

from tests.config import Config
from utils.screenshot import screenshot_on_fail
from utils.open_web_browser import open_web_browser
from utils.step_definition import step_definition

from page_object_models.about_page_model import AboutPageModel
from expected_results.page_content.about_page_content import AboutPageContent


@allure.epic('Page Content')
@allure.parent_suite('Page Unique Content')
@allure.suite('About Page Content')
@allure.sub_suite("About Page Unique Content")
@allure.feature("About Page")
@allure.story('About Content')
@screenshot_on_fail()
class TestAboutPageContent(unittest.TestCase):
	"""
	Test unique "About" web page content
	"""

	@classmethod
	def setUpClass(cls):
		with allure.step("Open web browser"):
			cls.app_config = Config()
			cls.page_model = AboutPageModel
			cls.page_content = AboutPageContent
			cls.page = open_web_browser(browser=cls.app_config.browser,
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
		Content base elements validation > About page URL:
			1. Open About web page
			2. Do URL verification
		""")
		allure.dynamic.title("Web page URL test")
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		# Verify Web Page URL
		step_definition(self,
		                step_description="About Web Page URL test",
		                expected=AboutPageContent.URL,
		                actual=self.page.url,
		                act=None,
		                click=False)

	def test_page_title(self):
		allure.dynamic.description("""
		Content base elements validation > About page title:
			1. Open About web page
			2. Do Title verification
		""")
		allure.dynamic.title("Web page title test")
		allure.dynamic.severity(allure.severity_level.MINOR)

		# Verify Web Page Title
		step_definition(self,
		                step_description="About Web Page Title test",
		                expected=AboutPageContent.TITLE,
		                actual=self.page.title,
		                act=None,
		                click=False)

	def test_description_title_text(self):
		allure.dynamic.description("""
		Content base elements validation > About page > description title:
			1. Open About web page
			2. Do Description Title verification
		""")
		allure.dynamic.title("Web page description title test")
		allure.dynamic.severity(allure.severity_level.MINOR)

		# verify description title text
		step_definition(self,
		                step_description="Description header test",
		                expected=AboutPageContent.DESCRIPTION['title'],
		                actual=self.page.description_title,
		                act=None,
		                click=False)

	def test_description_text(self):
		allure.dynamic.description("""
		Content base elements validation > About page > description:
			1. Open About web page
			2. Do URL verification
		""")
		allure.dynamic.title("Web page description test")
		allure.dynamic.severity(allure.severity_level.MINOR)

		# Verify description text
		# Context About page elements validation:
		step_definition(self,
		                step_description="Description text (first paragraph) test",
		                expected=AboutPageContent.DESCRIPTION['text'][0],
		                actual=self.page.description_first_line,
		                act=None,
		                click=False)

		step_definition(self,
		                step_description="Description text (second paragraph) test",
		                expected=AboutPageContent.DESCRIPTION['text'][1],
		                actual=self.page.description_second_line,
		                act=None,
		                click=False)

		step_definition(self,
		                step_description="Description text (third paragraph) test",
		                expected=AboutPageContent.DESCRIPTION['text'][2],
		                actual=self.page.description_third_line,
		                act=None,
		                click=False)

		step_definition(self,
		                step_description="Description text (fourth paragraph) test",
		                expected=AboutPageContent.LINK,
		                actual=self.page.description_link,
		                act=None,
		                click=False)

