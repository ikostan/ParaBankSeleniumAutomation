#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from element_object_models.element import Element

from page_locators.home_page_locator import HomePageLocator
from page_object_models.base_page_model import BasePageModel

from expected_results.page_content.home_page_content import HomePageContent


class HomePageModel(BasePageModel):
	'''
	The page object pattern intends creating an object for each web page.
	By following this technique a layer of separation between the test code and technical implementation is created.
	'''

	_url = HomePageContent.URL

	'''
	def hit_login_button(self):
		"""
		1. Click on Log In button
		2. Wait until URL changes
		3. Returns OverviewPageModel object on success
		4. Return LoginPageModel object on failure
		:return:
		"""
		super().hit_login_button()
		if self.url() == OverviewPageContent.URL:
			from page_object_models.overview_page_model import OverviewPageModel
			return OverviewPageModel(driver=self.driver,
			                         implicit_wait_time=5,
			                         explicit_wait_time=10)
		else:
			from page_object_models.login_page_model import LoginPageModel
			return LoginPageModel(driver=self.driver,
			                      implicit_wait_time=5,
			                      explicit_wait_time=10)
	'''

	# @property
	def atm_title(self):
		"""
		Returns title from ATM Services section
		:return:
		"""
		element = Element(self.driver, self.explicit_wait_time, HomePageLocator.ATM_SERVICES_TITLE)
		txt = element.text
		return txt

	# @property
	def atm_withdraw_funds_text(self):
		"""
		Returns withdraw_funds_text from ATM Services section
		:return:
		"""
		element = Element(self.driver, self.explicit_wait_time, HomePageLocator.WITHDRAW_FUNDS)
		txt = element.text
		return txt

	# @property
	def atm_withdraw_funds_formated_href(self):
		"""
		Returns withdraw_funds_href from ATM Services section
		:return:
		"""
		element = Element(self.driver, self.explicit_wait_time, HomePageLocator.WITHDRAW_FUNDS)
		href = super()._formated_url(element.element_href)
		return href

	# @property
	def atm_transfer_funds_text(self):
		"""
		Returns transfer_funds_text from ATM Services section
		:return:
		"""
		element = Element(self.driver, self.explicit_wait_time, HomePageLocator.ATM_TRANSFER_FUNDS)
		txt = element.text
		return txt

	# @property
	def atm_transfer_funds_formated_href(self):
		'''
		Returns transfer_funds_href from ATM Services section
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, HomePageLocator.ATM_TRANSFER_FUNDS)
		href = super()._formated_url(element.element_href)
		return href

	# @property
	def atm_check_balances_text(self):
		'''
		Returns check_balances_text from ATM Services section
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, HomePageLocator.CHECK_BALANCES)
		txt = element.text
		return txt

	# @property
	def atm_check_balances_formated_href(self):
		'''
		Returns check_balances_href from ATM Services section
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, HomePageLocator.CHECK_BALANCES)
		href = super()._formated_url(element.element_href)
		return href

	# @property
	def atm_make_deposits_text(self):
		'''
		Returns make_deposits_text from ATM Services section
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, HomePageLocator.MAKE_DEPOSITS)
		txt = element.text
		return txt

	# @property
	def atm_make_deposits_formated_href(self):
		'''
		Returns make_deposits_href from ATM Services section
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, HomePageLocator.MAKE_DEPOSITS)
		href = super()._formated_url(element.element_href)
		return href

	# @property
	def online_services_title(self):
		'''
		Returns title from online_services section
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, HomePageLocator.ONLINE_SERVICES_TITLE)
		txt = element.text
		return txt

	# @property
	def bill_pay_formated_href(self):
		'''
		Returns bill_pay href from ATM Services section
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, HomePageLocator.BILL_PAY)
		href = super()._formated_url(element.element_href)
		return href

	# @property
	def bill_pay_title(self):
		'''
		Returns title from bill_pay section
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, HomePageLocator.BILL_PAY)
		txt = element.text
		return txt

	# @property
	def account_history_formated_href(self):
		'''
		Returns account_history href from ATM Services section
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, HomePageLocator.ACCOUNT_HISTORY)
		href = super()._formated_url(element.element_href)
		return href

	# @property
	def account_history_title(self):
		'''
		Returns title from account_history section
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, HomePageLocator.ACCOUNT_HISTORY)
		txt = element.text
		return txt

	# @property
	def online_transfer_funds_formated_href(self):
		'''
		Returns transfer_funds href from ATM Services section
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, HomePageLocator.ONLINE_TRANSFER_FUNDS)
		href = super()._formated_url(element.element_href)
		return href

	# @property
	def online_transfer_funds_title(self):
		'''
		Returns title from transfer_funds section
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, HomePageLocator.ONLINE_TRANSFER_FUNDS)
		txt = element.text
		return txt

	# @property
	def read_more_services_formated_href(self):
		'''
		Returns read_more_services href from ATM Services section
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, HomePageLocator.READ_MORE_SERVICES)
		href = super()._formated_url(element.element_href)
		return href

	# @property
	def read_more_services_title(self):
		'''
		Returns title from read_more_services section
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, HomePageLocator.READ_MORE_SERVICES)
		txt = element.text
		return txt

	# @property
	def read_more_news_formated_href(self):
		'''
		Returns read_more_news href from ATM Services section
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, HomePageLocator.READ_MORE_NEWS)
		href = super()._formated_url(element.element_href)
		return href

	# @property
	def read_more_news_title(self):
		'''
		Returns title from read_more_news section
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, HomePageLocator.READ_MORE_NEWS)
		txt = element.text
		return txt

	# @property
	def latest_news_title(self):
		'''
		Returns title from latest_news section
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, HomePageLocator.LATEST_NEWS)
		txt = element.text
		return txt
