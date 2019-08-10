#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from elements.element import Element
from page_models.base_personal_info_page_model import BasePersonalInfoPageModel
from page_locators.forgot_login_info_page_locator import ForgotLoginInfoPageLocator
from expected_results.page_context.forgot_login_info_page_context import ForgotLoginInfoPageContext


class ForgotLoginInfoPageModel(BasePersonalInfoPageModel):
	'''
	The page object pattern intends creating an object for each web page.
	By following this technique a layer of separation between the test code and technical implementation is created.
	'''

	_url = ForgotLoginInfoPageContext.URL

	@property
	def find_info_btn_label(self):
		'''
		Returns "FIND MY LOGIN INFO" button label
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, ForgotLoginInfoPageLocator.FIND_MY_LOGIN_INFO_BUTTON)
		txt = element.element_value
		return txt

	@property
	def click_find_info_btn(self):
		'''
		Click on "FIND MY LOGIN INFO" button
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, ForgotLoginInfoPageLocator.FIND_MY_LOGIN_INFO_BUTTON)
		element.click()
		return None

