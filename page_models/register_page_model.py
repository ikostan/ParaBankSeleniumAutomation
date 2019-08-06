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



