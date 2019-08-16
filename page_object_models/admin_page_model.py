#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from element_object_models.element import Element
from page_object_models.base_page_model import BasePageModel
from page_locators.admin_page_locator import AdminPageLocator
from expected_results.page_content.admin_page_content import AdminPageContent


class AdminPageModel(BasePageModel):
	'''
	The page object pattern intends creating an object for each web page.
	By following this technique a layer of separation between the test code and technical implementation is created.
	'''

	_url = AdminPageContent.URL

	def hit_initialize_button(self):
		'''
		Hit Initialize button
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, AdminPageLocator.INITIALIZE_BUTTON)
		element.press_button()
		return None

	def hit_clean_button(self):
		'''
		Hit Clean button
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, AdminPageLocator.CLEAN_BUTTON)
		element.press_button()
		return None
