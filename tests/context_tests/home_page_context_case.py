import allure
from utils.driver import Driver
from utils.screenshot import screenshot_on_fail
from page_models.home_page_model import HomePageModel
from tests.context_tests.base_context_case import TestBaseContextCase
from expected_results.page_context.home_page_context import HomePageContext


@allure.feature("Home Page")
@allure.story('Home Context')
@allure.suite('Home Page Context Test Suite')
@screenshot_on_fail()
class TestHomePageContextCase(TestBaseContextCase):

	def open_web_browser(self, browser):

		# Open web page
		with allure.step("Open web browser on {}.".format(HomePageContext.URL)):
			driver = Driver(browser)
			self.page = HomePageModel(driver=driver, implicit_wait_time=5, explicit_wait_time=10)
			self.page.go()

	@allure.feature("Base Page")
	def verify_page_url(self):

		with allure.step("Verify web page URL. Expected result: {}".format(HomePageContext.URL)):
			self.assertEqual(HomePageContext.URL,
			                 self.page.url)

	@allure.feature("Base Page")
	def verify_page_title(self):

		with allure.step("Verify web page title. Expected result: {}".format(HomePageContext.TITLE)):
			self.assertEqual(HomePageContext.TITLE,
			                 self.page.title)

	@allure.feature("Home Page")
	def verify_atm_services_context(self):

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

	@allure.feature("Home Page")
	def verify_online_services_context(self):

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

	@allure.feature("Home Page")
	def verify_read_more_services_button(self):

		with allure.step("Verify Read More Services text. Expected result: {}".format(
				HomePageContext.READ_MORE_SERVICES['text'])):
			self.assertEqual(HomePageContext.READ_MORE_SERVICES['text'],
			                 self.page.read_more_services_title)

		with allure.step("Verify Read More Services href. Expected result: {}".format(
				HomePageContext.READ_MORE_SERVICES['href'])):
			self.assertEqual(HomePageContext.READ_MORE_SERVICES['href'],
			                 self.page.read_more_services_formated_href)

	@allure.feature("Home Page")
	def verify_read_more_news_button(self):

		with allure.step("Verify Read More News text. Expected result: {}".format(
				HomePageContext.READ_MORE_NEWS['text'])):
			self.assertEqual(HomePageContext.READ_MORE_NEWS['text'],
			                 self.page.read_more_news_title)

		with allure.step("Verify Read More News ref. Expected result: {}".format(
				HomePageContext.READ_MORE_NEWS['href'])):
			self.assertEqual(HomePageContext.READ_MORE_NEWS['href'],
			                 self.page.read_more_news_formated_href)

	@allure.feature("Home Page")
	def verify_latest_news_title(self):

		with allure.step("Verify Latest News title. Expected result: {}".format(
				HomePageContext.LATEST_NEWS)):
			self.assertEqual(HomePageContext.LATEST_NEWS,
			                 self.page.latest_news_title)

	def verify_parabank_admin_logo(self):

		# Context base elements validation:
		self.parabank_admin_logo_test()

	def verify_parabank_logo(self):

		# Context base elements validation:
		self.parabank_logo_test()

	def verify_home_right_menu_button(self):

		# Context base elements validation:
		self.right_menu_home_button_test()

	def verify_about_right_menu_button(self):

		# Context base elements validation:
		self.right_menu_about_button_test()

	def verify_contact_right_menu_button(self):

		# Context base elements validation:
		self.right_menu_contact_button_test()

	def verify_solutions_menu_items(self):

		# Context base elements validation:
		self.solutions_menu_items_test()

	def verify_customer_login(self):

		# Context base elements validation:
		self.customer_login_test()

	def verify_footer_items(self):

		# Context base elements validation:
		self.footer_items_test()


