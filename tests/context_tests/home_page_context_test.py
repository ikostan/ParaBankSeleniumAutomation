#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure

from utils.screenshot import screenshot_on_fail
from utils.open_web_browser import open_web_browser
from utils.browser_configuration import browser_configuration

from page_models.home_page_model import HomePageModel
from expected_results.page_context.home_page_context import HomePageContext
from tests.context_tests.context_cases.home_page_context_case import HomePageContextCase


@allure.suite("Chrome Browser")
@allure.sub_suite('Context Test')
@allure.feature("Home Page")
@screenshot_on_fail()
class TestChromeHomePageContext(HomePageContextCase):

	@classmethod
	def setUpClass(cls):
		with allure.step("Open web browser"):
			cls.browser = browser_configuration()
			cls.page_model = HomePageModel
			cls.page_context = HomePageContext
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
		Context base elements validation > Home page URL:
			1. Open Home web page
			2. Do URL verification
		""")
		allure.dynamic.title("Web page URL test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# test url
		self.verify_page_url()

	def test_page_title(self):
		allure.dynamic.description("""
		Context base elements validation > Home page title:
			1. Open Home web page
			2. Do web page title verification
		""")
		allure.dynamic.title("Web page title test")

		# Verify Page Title
		self.verify_page_title()

	def test_atm_services_context(self):
		allure.dynamic.description("""
		Home page Context elements validation > ATM services:
			1. Open Home web page
			2. Do ATM services context verification
		""")
		allure.dynamic.title("ATM services context test")

		# Verify ATM Services Context
		# allure.step
		self.verify_atm_services_context()

	def test_online_services_context(self):
		allure.dynamic.description("""
		Home page Context elements validation > ATM services:
			1. Open Home web page
			2. Do Online services context verification
		""")
		allure.dynamic.title("Online services context test")

		# Verify Online Services Context
		self.verify_online_services_context()

	def test_read_more_services_button(self):
		allure.dynamic.description("""
		Home page Context elements validation > 'Read More' (services) button:
			1. Open Home web page
			2. Do 'Read More' button verification
		""")
		allure.dynamic.title("'Read More' (services) button test")

		# Verify Read More Services button
		self.verify_read_more_services_button()

	def test_read_more_news_button(self):
		allure.dynamic.description("""
		Home page Context elements validation > 'Read More' (news) button:
			1. Open Home web page
			2. Do 'Read More' button verification
		""")
		allure.dynamic.title("'Read More' (news) button test")

		# Verify Read More News button
		with allure.step("Verify Read More News button attributes:"):
			self.verify_read_more_news_button_text()
			self.verify_read_more_news_button_href()

	def test_latest_news_title(self):
		allure.dynamic.description("""
		Home page Context elements validation > 'Latest News' title:
			1. Open Home web page
			2. Do 'Latest News' title verification
		""")
		allure.dynamic.title("'Latest News' title test")

		# Verify Last News title
		self.verify_latest_news_title()
