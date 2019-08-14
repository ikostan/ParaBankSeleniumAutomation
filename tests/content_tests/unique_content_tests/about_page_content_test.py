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
	'''
	Test unique "About" web page content
	'''

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
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		with allure.step("About Web Page URL test"):
			self.assertEqual(AboutPageContent.URL,
			                 self.page.url())

	def test_page_title(self):
		allure.dynamic.description("""
		Content base elements validation > About page title:
			1. Open About web page
			2. Do Title verification
		""")
		allure.dynamic.title("Web page title test")

		# Verify Web Page Title
		allure.dynamic.severity(allure.severity_level.MINOR)

		with allure.step("About Web Page Title test"):
			self.assertEqual(AboutPageContent.TITLE,
			                 self.page.title())

	def test_description_title_text(self):
		allure.dynamic.description("""
		Content base elements validation > About page > description title:
			1. Open About web page
			2. Do URL verification
		""")
		allure.dynamic.title("Web page description title test")

		# verify description title text
		allure.dynamic.severity(allure.severity_level.MINOR)

		# Context About page elements validation:
		with allure.step("Description header test"):
			self.assertEqual(AboutPageContent.DESCRIPTION['title'], self.page.description_title)

	def test_description_text(self):
		allure.dynamic.description("""
		Content base elements validation > About page > description:
			1. Open About web page
			2. Do URL verification
		""")
		allure.dynamic.title("Web page description test")

		# verify description text
		allure.dynamic.severity(allure.severity_level.MINOR)

		# Context About page elements validation:
		with allure.step("Description text (first paragraph) test"):
			self.assertEqual(AboutPageContent.DESCRIPTION['text'][0], self.page.description_first_line)

		with allure.step("Description text (second paragraph) test"):
			self.assertEqual(AboutPageContent.DESCRIPTION['text'][1], self.page.description_second_line)

		with allure.step("Description text (third paragraph) test"):
			self.assertEqual(AboutPageContent.DESCRIPTION['text'][2], self.page.description_third_line)

		with allure.step("Description text (fourth paragraph) test"):
			self.assertEqual(AboutPageContent.LINK, self.page.description_link)
