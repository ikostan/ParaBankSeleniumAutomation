from elements.element import Element
from page_models.base_page_model import BasePageModel
from page_models.base_personal_info_page_model import BasePersonalInfoPageModel
from page_locators.forgot_login_info_page_locator import ForgotLoginInfoPageLocator
from expected_results.page_context.forgot_login_info_page_context import ForgotLoginInfoPageContext


class RegisterPageModel(BasePersonalInfoPageModel):
	'''
	The page object pattern intends creating an object for each web page.
	By following this technique a layer of separation between the test code and technical implementation is created.
	'''

	_url = ForgotLoginInfoPageContext.URL



