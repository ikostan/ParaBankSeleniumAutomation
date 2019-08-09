from elements.element import Element
from page_models.base_page_model import BasePageModel
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_locators.account_services_menu_locator import AccountServicesMenuLocator


class AccountServicesMenu(BasePageModel):

	@property
	def welcome_message(self):
		'''
		Returns 'welcome' message that appears above "Account Services" menu
		:param user:
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, AccountServicesMenuLocator.WELCOME_MESSAGE)
		txt = element.text
		return txt

	@property
	def menu_title(self):
		'''
		Returns "Account Services" menu header
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, AccountServicesMenuLocator.HEADER)
		txt = element.text
		return txt

	def open_new_account(self):
		'''
		Click on "Open New Account"
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, AccountServicesMenuLocator.OPEN_NEW_ACCOUNT)
		element.press_button()
		return None

	def accounts_overview(self):
		'''
		Click on "Account Overview"
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, AccountServicesMenuLocator.ACCOUNTS_OVERVIEW)
		element.press_button()
		return None

	def transfer_funds(self):
		'''
		Click on "Transfer Funds"
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, AccountServicesMenuLocator.TRANSFER_FUNDS)
		element.press_button()
		return None

	def bill_pay(self):
		'''
		Click on "Bill Pay"
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, AccountServicesMenuLocator.BILL_PAY)
		element.press_button()
		return None

	def find_transactions(self):
		'''
		Click on "Find Transactions"
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, AccountServicesMenuLocator.FIND_TRANSACTIONS)
		element.press_button()
		return None

	def update_contact_info(self):
		'''
		Click on "Update Contact Info"
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, AccountServicesMenuLocator.UPDATE_CONTACT_INFO)
		element.press_button()
		return None

	def request_loan(self):
		'''
		Click on "Request Loan"
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, AccountServicesMenuLocator.REQUEST_LOAN)
		element.press_button()
		return None

	def log_out(self):
		'''
		Click on "Log Out"
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, AccountServicesMenuLocator.LOG_OUT)
		element.press_button()
		return None

