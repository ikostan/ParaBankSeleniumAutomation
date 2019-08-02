from elements.element import Element
from page_models.base_page_model import BasePageModel
from page_context.home_page_context import HomePageContext
from page_locators.home_page_locator import HomePageLocator


class HomePageModel(BasePageModel):
	'''
	The page object pattern intends creating an object for each web page.
	By following this technique a layer of separation between the test code and technical implementation is created.
	'''

	_url = HomePageContext.URL

	@property
	def atm_title(self):
		'''
		Returns title from ATM Services section
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, HomePageLocator.ATM_SERVICES_TITLE)
		txt = element.text
		return txt

	@property
	def atm_withdraw_funds_text(self):
		'''
		Returns withdraw_funds_text from ATM Services section
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, HomePageLocator.WITHDRAW_FUNDS)
		txt = element.text
		return txt

	@property
	def atm_withdraw_funds_formated_href(self):
		'''
		Returns withdraw_funds_href from ATM Services section
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, HomePageLocator.WITHDRAW_FUNDS)
		href = super()._formated_url(element.element_href)
		return href

	@property
	def atm_transfer_funds_text(self):
		'''
		Returns transfer_funds_text from ATM Services section
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, HomePageLocator.TRANSFER_FUNDS)
		txt = element.text
		return txt

	@property
	def atm_transfer_funds_formated_href(self):
		'''
		Returns transfer_funds_href from ATM Services section
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, HomePageLocator.TRANSFER_FUNDS)
		href = super()._formated_url(element.element_href)
		return href

