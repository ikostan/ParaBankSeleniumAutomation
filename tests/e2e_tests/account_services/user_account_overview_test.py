#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
import unittest

from expected_results.page_content.bill_pay_content import BillPayContent
from expected_results.users.valid_users_templates.john_doe import JohnDoe
from tests.config import Config
from utils.register_user import register_user
from utils.clean_database import clean_database
from utils.screenshot import screenshot_on_fail
from utils.step_definition import step_definition
from utils.open_web_browser import open_web_browser

from expected_results.users.base_user import BaseUser
from page_object_models.home_page_model import HomePageModel
from expected_results.users.valid_users_templates.jane_doe import JaneDoe
from expected_results.page_content.home_page_content import HomePageContent


@allure.epic('Page Functionality')
@allure.parent_suite('End To End')
@allure.suite("Account Services")
@allure.sub_suite("Positive Tests")
@allure.feature("Accounts Overview")
@allure.story('Login/Logout Functionality')
@screenshot_on_fail()
class TestAccountsOverviewPage(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.user = BaseUser(JaneDoe)
		cls.payee = JohnDoe
		cls.page_model = HomePageModel
		cls.page_context = HomePageContent
		cls.transfer_amount = '153.45'
		cls.account = '11223344'
		cls.total_left = cls.user.balance - float(cls.transfer_amount)
		cls.config = Config()

		with allure.step("Initial data setup > clean DB"):
			clean_database(config=cls.config)

		with allure.step("Initial data setup > register test user"):
			register_user(user=cls.user, config=cls.config)

		with allure.step("Open web browser"):
			cls.page = open_web_browser(config=cls.config,
			                            page_model=cls.page_model,
			                            page_content=cls.page_context)

	@classmethod
	def tearDownClass(cls):
		with allure.step("Close web browser"):
			if cls.page:
				cls.page.quit()
				cls.page = None

	def test_user_login_logout(self):
		allure.dynamic.description("""
                Accounts Overview validation > Check Total Balance:
                    1. Open Home web page
                    2. Type username/password
                    3. Hit "Log In" button
                    4. Check Total Balance
                    5. Go to "Bill Pay"
                    6. Fill out the Bill Payment form + amount $153.45
                    7. Send payment
                    8. Go back to Accounts Overview
                    9. Verify Total > should be: 515.50 - 153.45 = 362.05
                    10. Log Out
                    11. Close web browser
                """)
		allure.dynamic.title("Home page > Accounts Overview > Check Balance")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		step_definition(self,
		                step_description='Type Username > Verify Username value',
		                expected=self.user.username,
		                actual=self.page.username,
		                act=self.page.enter_username,
		                click=False)

		step_definition(self,
		                step_description='Type Password > Verify Password value',
		                expected=self.user.password,
		                actual=self.page.password,
		                act=self.page.enter_password,
		                click=False)

		with allure.step('Hit Log In button'):
			print("Logging in...")
			self.page = self.page.hit_login_button()

		step_definition(self,
		                step_description='Check Total Balance',
		                expected='${0:.2f}'.format(self.user.balance),
		                actual=self.page.total_balance,
		                act=None,
		                click=False)

		with allure.step("Go to \"Bill Pay\""):
			print("Opening Bill Payment Service web page...")
			self.page = self.page.hit_bill_pay()

		with allure.step("Fill out Bill Payment form"):
			self.page.fill_out_bill_payment_form(payee=self.payee,
			                                     account=self.account,
			                                     amount=self.transfer_amount)

		step_definition(self,
		                step_description="Press on \"Send Payment\" button",
		                expected=True,
		                actual=True,
		                act=self.page.hit_send_payment_button,
		                click=True)

		step_definition(self,
		                step_description="Verify Bill Payment Complete title",
		                expected=BillPayContent.BILL_PAYMENT_COMPLETE_TITLE,
		                actual=self.page.bill_payment_complete_title,
		                act=None,
		                click=False)

		'''
		payment_complete_message = BillPayContent.PAYMENT_MESSAGE.replace("<full_name>",
		                                                                  (self.payee.FIRST_NAME +
		                                                                   ' ' +
		                                                                   self.payee.LAST_NAME))
		payment_complete_message = payment_complete_message.replace('<total_amount>',
		                                                            self.transfer_amount)
		self.payment_complete_message = payment_complete_message.replace('<account_number>',
		                                                                 self.account)
		step_definition(self,
		                step_description="Verify Bill Payment Complete message",
		                expected=self.payment_complete_message,
		                actual=self.page.payment_message,
		                act=None,
		                click=False)
		'''

		step_definition(self,
		                step_description="Verify more details message",
		                expected=BillPayContent.MORE_DETAILS_MESSAGE,
		                actual=self.page.more_details_message,
		                act=None,
		                click=False)

		with allure.step("Go back to \"Accounts Overview\""):
			print("Opening Accounts Overview web page...")
			self.page = self.page.hit_accounts_overview()

		step_definition(self,
		                step_description='Check Total Balance',
		                expected='${0:.2f}'.format(self.total_left),
		                actual=self.page.total_balance,
		                act=None,
		                click=False)

		# Log Out
		with allure.step('Hit "Log Out" link'):
			print("Logging out...")
			self.page = self.page.hit_log_out_button()
