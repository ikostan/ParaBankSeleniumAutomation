#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from elements.element import Element
from page_locators.login_page_locator import LoginPageLocator
from page_object_models.base_page_model import BasePageModel
from expected_results.page_content.login_page_content import LoginPageContent


class LoginPageModel(BasePageModel):
	'''
	The page object pattern intends creating an object for each web page.
	By following this technique a layer of separation between the test code and technical implementation is created.
	'''

	_url = LoginPageContent.URL

	# @property
	def error_title(self):
		'''
		Returns error title text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, LoginPageLocator.ERROR_TITLE)
		txt = element.text
		return txt

	# @property
	def error_message(self):
		'''
		Returns error message text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, LoginPageLocator.ERROR_MESSAGE)
		txt = element.text
		return txt


