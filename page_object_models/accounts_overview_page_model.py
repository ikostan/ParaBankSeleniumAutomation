#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from tests.config import Config
from utils.driver import Driver
from element_object_models.element import Element

from page_object_models.base_page_model import BasePageModel
from expected_results.page_content.accounts_overview_page_content import AccountsOverviewPageContent
from page_locators.accounts_overview_page_locator import AccountsOverviewPageLocator


class AccountsOverviewPageModel(BasePageModel):
	"""
	The page object pattern intends creating an object for each web page.
	By following this technique a layer of separation between the test code and technical implementation is created.
	"""

	# _url = OverviewPageContent.URL

	def __init__(self, config: Config, driver: Driver, implicit_wait_time, explicit_wait_time):
		super().__init__(config, driver, implicit_wait_time, explicit_wait_time)
		_url = config.base_url + AccountsOverviewPageContent.URL

	def total_balance(self):
		"""
		Returns total balance value
		:return:
		"""
		element = Element(driver=self.driver,
		                  explicit_wait_time=self.explicit_wait_time,
		                  locator=AccountsOverviewPageLocator.TOTAL_VALUE)

		txt = element.text
		return txt


