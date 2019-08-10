#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
from utils.screenshot import screenshot_on_fail
from expected_results.page_context.home_page_context import HomePageContext
from tests.content_tests.content_cases.base_cases.base_content_case import BaseContextCase


@screenshot_on_fail()
class HomePageContextCase(BaseContextCase):

	# @pytest.mark.parametrize('expected_url', [HomePageContext.URL], ids=['Expected web page url'])
	def verify_page_url(self):

		expected_url = HomePageContext.URL
		with allure.step("Verify web page URL. Expected result: {}".format(expected_url)):
			actual = self.page.url
			self.assertEqual(expected_url, actual, msg='\nExpected: {}. Actual: {}\n'.format(expected_url, actual))

	def verify_page_title(self):
		allure.dynamic.severity(allure.severity_level.MINOR)

		with allure.step("Verify web page title. Expected result: {}".format(HomePageContext.TITLE)):
			self.assertEqual(HomePageContext.TITLE,
			                 self.page.title)

	def verify_atm_services_context(self):
		allure.dynamic.severity(allure.severity_level.MINOR)

		with allure.step("Verify ATM services title. Expected result: {}".format(
				HomePageContext.ATM_SERVICES['title'])):
			self.assertEqual(HomePageContext.ATM_SERVICES['title'],
			                 self.page.atm_title)

		with allure.step("Verify ATM services > Withdraw Funds > text. Expected result: {}".format(
				HomePageContext.ATM_SERVICES['Withdraw Funds']['text'])):
			self.assertEqual(HomePageContext.ATM_SERVICES['Withdraw Funds']['text'],
			                 self.page.atm_withdraw_funds_text)

		with allure.step("Verify ATM services > Withdraw Funds > href. Expected result: {}".format(
				HomePageContext.ATM_SERVICES['Withdraw Funds']['href'])):
			self.assertEqual(HomePageContext.ATM_SERVICES['Withdraw Funds']['href'],
			                 self.page.atm_withdraw_funds_formated_href)

		with allure.step("Verify ATM services > Check Balances > text. Expected result: {}".format(
				HomePageContext.ATM_SERVICES['Check Balances']['text'])):
			self.assertEqual(HomePageContext.ATM_SERVICES['Check Balances']['text'],
			                 self.page.atm_check_balances_text)

		with allure.step("Verify ATM services > Check Balances > href. Expected result: {}".format(
				HomePageContext.ATM_SERVICES['Check Balances']['href'])):
			self.assertEqual(HomePageContext.ATM_SERVICES['Check Balances']['href'],
			                 self.page.atm_check_balances_formated_href)

		with allure.step("Verify ATM services > Make Deposits > text. Expected result: {}".format(
				HomePageContext.ATM_SERVICES['Make Deposits']['text'])):
			self.assertEqual(HomePageContext.ATM_SERVICES['Make Deposits']['text'],
			                 self.page.atm_make_deposits_text)

		with allure.step("Verify ATM services > Make Deposits > href. Expected result: {}".format(
				HomePageContext.ATM_SERVICES['Make Deposits']['href'])):
			self.assertEqual(HomePageContext.ATM_SERVICES['Make Deposits']['href'],
			                 self.page.atm_make_deposits_formated_href)

	def verify_online_services_context(self):
		allure.dynamic.severity(allure.severity_level.MINOR)

		with allure.step("Verify Online Services title. Expected result: {}".format(
				HomePageContext.ONLINE_SERVICES['title'])):
			self.assertEqual(HomePageContext.ONLINE_SERVICES['title'],
			                 self.page.online_services_title)

		with allure.step("Verify Bill Pay text. Expected result: {}".format(
				HomePageContext.ONLINE_SERVICES['Bill Pay']['text'])):
			self.assertEqual(HomePageContext.ONLINE_SERVICES['Bill Pay']['text'],
			                 self.page.bill_pay_title)

		with allure.step("Verify Bill Pay href. Expected result: {}".format(
				HomePageContext.ONLINE_SERVICES['Bill Pay']['href'])):
			self.assertEqual(HomePageContext.ONLINE_SERVICES['Bill Pay']['href'],
			                 self.page.bill_pay_formated_href)

		with allure.step("Verify Account History text. Expected result: {}".format(
				HomePageContext.ONLINE_SERVICES['Account History']['text'])):
			self.assertEqual(HomePageContext.ONLINE_SERVICES['Account History']['text'],
			                 self.page.account_history_title)

		with allure.step("Verify Account History href. Expected result: {}".format(
				HomePageContext.ONLINE_SERVICES['Account History']['href'])):
			self.assertEqual(HomePageContext.ONLINE_SERVICES['Account History']['href'],
			                 self.page.account_history_formated_href)

		with allure.step("Verify Transfer Funds text. Expected result: {}".format(
				HomePageContext.ONLINE_SERVICES['Transfer Funds']['text'])):
			self.assertEqual(HomePageContext.ONLINE_SERVICES['Transfer Funds']['text'],
			                 self.page.online_transfer_funds_title)

		with allure.step("Verify Transfer Funds href. Expected result: {}".format(
				HomePageContext.ONLINE_SERVICES['Transfer Funds']['href'])):
			self.assertEqual(HomePageContext.ONLINE_SERVICES['Transfer Funds']['href'],
			                 self.page.online_transfer_funds_formated_href)

	def verify_read_more_services_button(self):

		allure.dynamic.severity(allure.severity_level.MINOR)

		with allure.step("Verify Read More Services text. Expected result: {}".format(
				HomePageContext.READ_MORE_SERVICES['text'])):
			self.assertEqual(HomePageContext.READ_MORE_SERVICES['text'],
			                 self.page.read_more_services_title)

		with allure.step("Verify Read More Services href. Expected result: {}".format(
				HomePageContext.READ_MORE_SERVICES['href'])):
			self.assertEqual(HomePageContext.READ_MORE_SERVICES['href'],
			                 self.page.read_more_services_formated_href)

	def verify_read_more_news_button_text(self):

		allure.dynamic.severity(allure.severity_level.MINOR)
		with allure.step("Verify Read More News text. Expected result: {}".format(
				HomePageContext.READ_MORE_NEWS['text'])):
			self.assertEqual(HomePageContext.READ_MORE_NEWS['text'],
			                 self.page.read_more_news_title)

	def verify_read_more_news_button_href(self):

		allure.dynamic.severity(allure.severity_level.NORMAL)
		with allure.step("Verify Read More News href. Expected result: {}".format(
				HomePageContext.READ_MORE_NEWS['href'])):
			self.assertEqual(HomePageContext.READ_MORE_NEWS['href'],
				                self.page.read_more_news_formated_href)

	def verify_latest_news_title(self):

		allure.dynamic.severity(allure.severity_level.MINOR)

		with allure.step("Verify Latest News title. Expected result: {}".format(
				HomePageContext.LATEST_NEWS)):
			self.assertEqual(HomePageContext.LATEST_NEWS,
			                 self.page.latest_news_title)

