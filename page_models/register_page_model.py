from elements.element import Element
from page_models.base_page_model import BasePageModel
from page_locators.register_page_locator import RegisterPageLocator
from page_models.base_personal_info_page_model import BasePersonalInfoPageModel
from expected_results.page_context.register_page_context import RegisterPageContext


class RegisterPageModel(BasePersonalInfoPageModel):
	'''
	The page object pattern intends creating an object for each web page.
	By following this technique a layer of separation between the test code and technical implementation is created.
	'''

	_url = RegisterPageContext.URL

	@property
	def username_title(self):
		'''
		Returns username title text
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, RegisterPageLocator.USERNAME_TITLE)
		txt = element.text
		return txt

	def type_username(self, username: str):
		'''
		Write text into username input field
		:param username:
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, RegisterPageLocator.USERNAME_INPUT)
		element.write(username)
		return None

	@property
	def password_title(self):
		'''
		Returns password title text
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, RegisterPageLocator.PASSWORD_TITLE)
		txt = element.text
		return txt

	def type_password(self, password: str):
		'''
		Write text into password input field
		:param password:
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, RegisterPageLocator.PASSWORD_INPUT)
		element.write(password)
		return None

	@property
	def confirm_title(self):
		'''
		Returns confirm title text
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, RegisterPageLocator.CONFIRM_TITLE)
		txt = element.text
		return txt

	def type_confirm(self, password: str):
		'''
		Write text into confirm input field
		:param password:
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, RegisterPageLocator.CONFIRM_INPUT)
		element.write(password)
		return None

	@property
	def register_btn_label(self):
		'''
		Returns register button label
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, RegisterPageLocator.REGISTER_BUTTON)
		txt = element.element_value
		return txt

	@property
	def click_register_btn(self):
		'''
		Click on register button
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, RegisterPageLocator.REGISTER_BUTTON)
		element.click()
		return None



