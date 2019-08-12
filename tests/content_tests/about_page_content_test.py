#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure

from utils.screenshot import screenshot_on_fail
from utils.open_web_browser import open_web_browser
from utils.browser_configuration import browser_configuration

from page_object_models.about_page_model import AboutPageModel
from expected_results.page_content.about_page_content import AboutPageContent
from tests.content_tests.content_cases.about_page_content_case import AboutPageContentCase


@allure.epic('Page Content')
@allure.parent_suite('Page Unique Content')
@allure.suite('About Page Content')
@allure.sub_suite("About Page Unique Content")
@allure.feature("About Page")
@allure.story('About Content')
@screenshot_on_fail()
class TestAboutPageContent(AboutPageContentCase):

	@classmethod
	def setUpClass(cls):
		with allure.step("Open web browser"):
			cls.browser = browser_configuration()
			cls.page_model = AboutPageModel
			cls.page_content = AboutPageContent
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
		Content base elements validation > About page URL:
			1. Open About web page
			2. Do URL verification
		""")
		allure.dynamic.title("Web page URL test")

		# Verify Web Page URL
		self.verify_page_url()

	def test_page_title(self):
		allure.dynamic.description("""
		Content base elements validation > About page title:
			1. Open About web page
			2. Do Title verification
		""")
		allure.dynamic.title("Web page title test")

		# Verify Web Page Title
		self.verify_page_title()

	def test_description_title_text(self):
		allure.dynamic.description("""
		Content base elements validation > About page > description title:
			1. Open About web page
			2. Do URL verification
		""")
		allure.dynamic.title("Web page description title test")

		# verify description title text
		self.verify_description_title()

	def test_description_text(self):
		allure.dynamic.description("""
		Content base elements validation > About page > description:
			1. Open About web page
			2. Do URL verification
		""")
		allure.dynamic.title("Web page description test")

		# verify description text
		self.verify_description_text()
