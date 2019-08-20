#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from tests.config import Config
from utils.driver import Driver

from element_object_models.element import Element
from selenium.common.exceptions import NoSuchElementException
from page_locators.forgot_login_info_page_locator import ForgotLoginInfoPageLocator
from page_object_models.base_personal_info_page_model import BasePersonalInfoPageModel
from expected_results.page_content.forgot_login_info_page_content import ForgotLoginInfoPageContent


class ForgotLoginInfoPageModel(BasePersonalInfoPageModel):
	'''
	The page object pattern intends creating an object for each web page.
	By following this technique a layer of separation between the test code and technical implementation is created.
	'''

	#_url = ForgotLoginInfoPageContent.URL

	def __init__(self, config: Config, driver: Driver, implicit_wait_time, explicit_wait_time):
		super().__init__(config, driver, implicit_wait_time, explicit_wait_time)
		self._url = config.base_url + ForgotLoginInfoPageContent.URL

	# @property
	def find_info_btn_label(self):
		'''
		Returns "FIND MY LOGIN INFO" button label
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, ForgotLoginInfoPageLocator.FIND_MY_LOGIN_INFO_BUTTON)
		txt = element.element_value
		return txt

	def hit_find_info_btn(self):
		'''
		Click on "FIND MY LOGIN INFO" button
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, ForgotLoginInfoPageLocator.FIND_MY_LOGIN_INFO_BUTTON)
		element.press_button()
		return ForgotLoginInfoPageModel(config=self._config,
		                                driver=self.driver,
		                                implicit_wait_time=5,
		                                explicit_wait_time=5)

	'''
	def hit_log_out_button(self):
		"""
		1. Click on "Log Out"
		2. Wait until URL changes
		3. Returns HomePageModel object on success

		:return:
		"""

		super().hit_log_out_button()
		from page_object_models.home_page_model import HomePageModel
		return HomePageModel(driver=self.driver,
		                     implicit_wait_time=5,
		                     explicit_wait_time=10)
	'''

	# @property
	def username_password(self):
		'''
		Returns Username/Password.
		Returns None in case of failure.
		:return:
		'''
		try:
			element = Element(self.driver, self.explicit_wait_time, ForgotLoginInfoPageLocator.USERNAME_PASSWORD)
			txt = element.text
			return txt
		except NoSuchElementException:
			return None

	def error_title(self):
		"""
		Return error title or None
		:return:
		"""
		try:
			element = Element(self.driver, self.explicit_wait_time, ForgotLoginInfoPageLocator.ERROR_TITLE)
			txt = element.text
			return txt
		except NoSuchElementException:
			return None

	def error_message(self):
		"""
		Returns error message or None
		:return:
		"""
		try:
			element = Element(self.driver, self.explicit_wait_time, ForgotLoginInfoPageLocator.ERROR_MESSAGE)
			txt = element.text
			return txt
		except NoSuchElementException:
			return None

