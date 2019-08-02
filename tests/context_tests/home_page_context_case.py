import  allure
from utils.driver import Driver
from utils.screenshot import screenshot_on_fail
from page_models.home_page_model import HomePageModel
from page_context.home_page_context import HomePageContext
from tests.context_tests.base_context_case import BaseTestCase


@screenshot_on_fail()
class HomePageContextTestCase(BaseTestCase):

	@allure.step("Open web browser on {}.".format(HomePageContext.URL))
	def open_web_browser(self, browser):

		# Open web page
		driver = Driver(browser)
		self.page = HomePageModel(driver=driver, implicit_wait_time=5, explicit_wait_time=10)
		self.page.go()

	def verify_page_url_title(self):

		self.assertEqual(HomePageContext.URL,
		                 self.page.url)
		self.assertEqual(HomePageContext.TITLE,
		                 self.page.title)

	def verify_atm_services_context(self):

		self.assertEqual(HomePageContext.ATM_SERVICES['title'],
		                 self.page.atm_title)

		self.assertEqual(HomePageContext.ATM_SERVICES['Withdraw Funds']['text'],
		                 self.page.atm_withdraw_funds_text)
		self.assertEqual(HomePageContext.ATM_SERVICES['Withdraw Funds']['href'],
		                 self.page.atm_withdraw_funds_formated_href)

		self.assertEqual(HomePageContext.ATM_SERVICES['Check Balances']['text'],
		                 self.page.atm_check_balances_text)
		self.assertEqual(HomePageContext.ATM_SERVICES['Check Balances']['href'],
		                 self.page.atm_check_balances_formated_href)

		self.assertEqual(HomePageContext.ATM_SERVICES['Make Deposits']['text'],
		                 self.page.atm_make_deposits_text)
		self.assertEqual(HomePageContext.ATM_SERVICES['Make Deposits']['href'],
		                 self.page.atm_make_deposits_formated_href)

	def verify_online_services_context(self):

		self.assertEqual(HomePageContext.ONLINE_SERVICES['title'],
		                 self.page.online_services_title)

		self.assertEqual(HomePageContext.ONLINE_SERVICES['Bill Pay']['text'],
		                 self.page.bill_pay_title)
		self.assertEqual(HomePageContext.ONLINE_SERVICES['Bill Pay']['href'],
		                 self.page.bill_pay_formated_href)

		self.assertEqual(HomePageContext.ONLINE_SERVICES['Account History']['text'],
		                 self.page.account_history_title)
		self.assertEqual(HomePageContext.ONLINE_SERVICES['Account History']['href'],
		                 self.page.account_history_formated_href)

		self.assertEqual(HomePageContext.ONLINE_SERVICES['Transfer Funds']['text'],
		                 self.page.online_transfer_funds_title)
		self.assertEqual(HomePageContext.ONLINE_SERVICES['Transfer Funds']['href'],
		                 self.page.online_transfer_funds_formated_href)

	def verify_read_more_services_button(self):

		self.assertEqual(HomePageContext.READ_MORE_SERVICES['text'],
		                 self.page.read_more_services_title)
		self.assertEqual(HomePageContext.READ_MORE_SERVICES['href'],
		                 self.page.read_more_services_formated_href)

	def verify_read_more_news_button(self):

		self.assertEqual(HomePageContext.READ_MORE_NEWS['text'],
		                 self.page.read_more_news_title)
		self.assertEqual(HomePageContext.READ_MORE_NEWS['href'],
		                 self.page.read_more_news_formated_href)

	def verify_latest_news_title(self):

		self.assertEqual(HomePageContext.LATEST_NEWS,
		                 self.page.latest_news_title)

	def verify_parabank_admin_logo(self):

		# Context base elements validation:
		self.parabank_admin_logo_test()

	def verify_parabank_logo(self):

		# Context base elements validation:
		self.parabank_logo_test()

	@allure.description("Home web page > Home button verification: href + text")
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


