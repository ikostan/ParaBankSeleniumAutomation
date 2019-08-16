#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/
from selenium.common.exceptions import NoSuchElementException

from element_object_models.element import Element
from page_object_models.base_personal_info_page_model import BasePersonalInfoPageModel
from page_locators.forgot_login_info_page_locator import ForgotLoginInfoPageLocator
from expected_results.page_content.forgot_login_info_page_content import ForgotLoginInfoPageContent


class ForgotLoginInfoPageModel(BasePersonalInfoPageModel):
	'''
	The page object pattern intends creating an object for each web page.
	By following this technique a layer of separation between the test code and technical implementation is created.
	'''

	_url = ForgotLoginInfoPageContent.URL

	# @property
	def find_info_btn_label(self):
		'''
		Returns "FIND MY LOGIN INFO" button label
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, ForgotLoginInfoPageLocator.FIND_MY_LOGIN_INFO_BUTTON)
		txt = element.element_value
		return txt

	def click_find_info_btn(self):
		'''
		Click on "FIND MY LOGIN INFO" button
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, ForgotLoginInfoPageLocator.FIND_MY_LOGIN_INFO_BUTTON)
		element.press_button()
		return ForgotLoginInfoPageModel(driver=self.driver,
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

