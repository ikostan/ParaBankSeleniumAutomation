#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
import unittest

from utils.screenshot import screenshot_on_fail
from utils.open_web_browser import open_web_browser
from utils.browser_configuration import browser_configuration

from page_object_models.home_page_model import HomePageModel
from expected_results.page_content.home_page_content import HomePageContent


@allure.epic('Page Content')
@allure.parent_suite('Page Unique Content')
@allure.suite('Home Page Content')
@allure.sub_suite("Home Page Unique Content")
@allure.feature("Home Page")
@allure.story('Home Content')
@screenshot_on_fail()
class TestHomePageContent(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		with allure.step("Open web browser"):
			cls.browser = browser_configuration()
			cls.page_model = HomePageModel
			cls.page_content = HomePageContent
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
		Content base elements validation > Home page URL:
			1. Open Home web page
			2. Do URL verification
		""")
		allure.dynamic.title("Web page URL test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# test url
		expected_url = HomePageContent.URL
		with allure.step("Verify web page URL. Expected result: {}".format(expected_url)):
			actual = self.page.url()
			self.assertEqual(expected_url, actual, msg='\nExpected: {}. Actual: {}\n'.format(expected_url, actual))

	def test_page_title(self):
		allure.dynamic.description("""
		Content base elements validation > Home page title:
			1. Open Home web page
			2. Do web page title verification
		""")
		allure.dynamic.title("Web page title test")

		# Verify Page Title
		allure.dynamic.severity(allure.severity_level.MINOR)

		with allure.step("Verify web page title. Expected result: {}".format(HomePageContent.TITLE)):
			self.assertEqual(HomePageContent.TITLE,
			                 self.page.title())

	def test_atm_services_context(self):
		allure.dynamic.description("""
		Home page Content elements validation > ATM services:
			1. Open Home web page
			2. Do ATM services context verification
		""")
		allure.dynamic.title("ATM services context test")

		# Verify ATM Services Content
		# allure.step
		allure.dynamic.severity(allure.severity_level.MINOR)

		with allure.step("Verify ATM services title. Expected result: {}".format(
				HomePageContent.ATM_SERVICES['title'])):
			self.assertEqual(HomePageContent.ATM_SERVICES['title'],
			                 self.page.atm_title)

		with allure.step("Verify ATM services > Withdraw Funds > text. Expected result: {}".format(
				HomePageContent.ATM_SERVICES['Withdraw Funds']['text'])):
			self.assertEqual(HomePageContent.ATM_SERVICES['Withdraw Funds']['text'],
			                 self.page.atm_withdraw_funds_text)

		with allure.step("Verify ATM services > Withdraw Funds > href. Expected result: {}".format(
				HomePageContent.ATM_SERVICES['Withdraw Funds']['href'])):
			self.assertEqual(HomePageContent.ATM_SERVICES['Withdraw Funds']['href'],
			                 self.page.atm_withdraw_funds_formated_href)

		with allure.step("Verify ATM services > Check Balances > text. Expected result: {}".format(
				HomePageContent.ATM_SERVICES['Check Balances']['text'])):
			self.assertEqual(HomePageContent.ATM_SERVICES['Check Balances']['text'],
			                 self.page.atm_check_balances_text)

		with allure.step("Verify ATM services > Check Balances > href. Expected result: {}".format(
				HomePageContent.ATM_SERVICES['Check Balances']['href'])):
			self.assertEqual(HomePageContent.ATM_SERVICES['Check Balances']['href'],
			                 self.page.atm_check_balances_formated_href)

		with allure.step("Verify ATM services > Make Deposits > text. Expected result: {}".format(
				HomePageContent.ATM_SERVICES['Make Deposits']['text'])):
			self.assertEqual(HomePageContent.ATM_SERVICES['Make Deposits']['text'],
			                 self.page.atm_make_deposits_text)

		with allure.step("Verify ATM services > Make Deposits > href. Expected result: {}".format(
				HomePageContent.ATM_SERVICES['Make Deposits']['href'])):
			self.assertEqual(HomePageContent.ATM_SERVICES['Make Deposits']['href'],
			                 self.page.atm_make_deposits_formated_href)

	def test_online_services_context(self):
		allure.dynamic.description("""
		Home page Content elements validation > ATM services:
			1. Open Home web page
			2. Do Online services context verification
		""")
		allure.dynamic.title("Online services context test")

		# Verify Online Services Content
		allure.dynamic.severity(allure.severity_level.MINOR)

		with allure.step("Verify Online Services title. Expected result: {}".format(
				HomePageContent.ONLINE_SERVICES['title'])):
			self.assertEqual(HomePageContent.ONLINE_SERVICES['title'],
			                 self.page.online_services_title)

		with allure.step("Verify Bill Pay text. Expected result: {}".format(
				HomePageContent.ONLINE_SERVICES['Bill Pay']['text'])):
			self.assertEqual(HomePageContent.ONLINE_SERVICES['Bill Pay']['text'],
			                 self.page.bill_pay_title)

		with allure.step("Verify Bill Pay href. Expected result: {}".format(
				HomePageContent.ONLINE_SERVICES['Bill Pay']['href'])):
			self.assertEqual(HomePageContent.ONLINE_SERVICES['Bill Pay']['href'],
			                 self.page.bill_pay_formated_href)

		with allure.step("Verify Account History text. Expected result: {}".format(
				HomePageContent.ONLINE_SERVICES['Account History']['text'])):
			self.assertEqual(HomePageContent.ONLINE_SERVICES['Account History']['text'],
			                 self.page.account_history_title)

		with allure.step("Verify Account History href. Expected result: {}".format(
				HomePageContent.ONLINE_SERVICES['Account History']['href'])):
			self.assertEqual(HomePageContent.ONLINE_SERVICES['Account History']['href'],
			                 self.page.account_history_formated_href)

		with allure.step("Verify Transfer Funds text. Expected result: {}".format(
				HomePageContent.ONLINE_SERVICES['Transfer Funds']['text'])):
			self.assertEqual(HomePageContent.ONLINE_SERVICES['Transfer Funds']['text'],
			                 self.page.online_transfer_funds_title)

		with allure.step("Verify Transfer Funds href. Expected result: {}".format(
				HomePageContent.ONLINE_SERVICES['Transfer Funds']['href'])):
			self.assertEqual(HomePageContent.ONLINE_SERVICES['Transfer Funds']['href'],
			                 self.page.online_transfer_funds_formated_href)

	def test_read_more_services_button(self):
		allure.dynamic.description("""
		Home page Content elements validation > 'Read More' (services) button:
			1. Open Home web page
			2. Do 'Read More' button verification
		""")
		allure.dynamic.title("'Read More' (services) button test")

		# Verify Read More Services button
		allure.dynamic.severity(allure.severity_level.MINOR)

		with allure.step("Verify Read More Services text. Expected result: {}".format(
				HomePageContent.READ_MORE_SERVICES['text'])):
			self.assertEqual(HomePageContent.READ_MORE_SERVICES['text'],
			                 self.page.read_more_services_title)

		with allure.step("Verify Read More Services href. Expected result: {}".format(
				HomePageContent.READ_MORE_SERVICES['href'])):
			self.assertEqual(HomePageContent.READ_MORE_SERVICES['href'],
			                 self.page.read_more_services_formated_href)

	def test_read_more_news_button(self):
		allure.dynamic.description("""
		Home page Content elements validation > 'Read More' (news) button:
			1. Open Home web page
			2. Do 'Read More' button verification
		""")
		allure.dynamic.title("'Read More' (news) button test")

		# Verify Read More News button
		with allure.step("Verify Read More News button attributes:"):

			allure.dynamic.severity(allure.severity_level.MINOR)
			with allure.step("Verify Read More News text. Expected result: {}".format(
					HomePageContent.READ_MORE_NEWS['text'])):
				self.assertEqual(HomePageContent.READ_MORE_NEWS['text'],
				                 self.page.read_more_news_title)

			allure.dynamic.severity(allure.severity_level.NORMAL)
			with allure.step("Verify Read More News href. Expected result: {}".format(
					HomePageContent.READ_MORE_NEWS['href'])):
				self.assertEqual(HomePageContent.READ_MORE_NEWS['href'],
				                 self.page.read_more_news_formated_href)

	def test_latest_news_title(self):
		allure.dynamic.description("""
		Home page Content elements validation > 'Latest News' title:
			1. Open Home web page
			2. Do 'Latest News' title verification
		""")
		allure.dynamic.title("'Latest News' title test")

		# Verify Last News title
		allure.dynamic.severity(allure.severity_level.MINOR)

		with allure.step("Verify Latest News title. Expected result: {}".format(
				HomePageContent.LATEST_NEWS)):
			self.assertEqual(HomePageContent.LATEST_NEWS,
			                 self.page.latest_news_title)
