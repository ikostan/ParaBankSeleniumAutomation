#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from elements.element import Element
from page_object_models.base_page_model import BasePageModel
from page_locators.about_page_locator import AboutPageLocator
from expected_results.page_content.about_page_content import AboutPageContent


class AboutPageModel(BasePageModel):
	'''
	The page object pattern intends creating an object for each web page.
	By following this technique a layer of separation between the test code and technical implementation is created.
	'''

	_url = AboutPageContent.URL

	# @property
	def description_title(self):
		'''
		Returns title from about text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, AboutPageLocator.DESCRIPTION_TITLE)
		txt = element.text
		return txt

	# @property
	def description_first_line(self):
		'''
		Returns text from description_first_line
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, AboutPageLocator.FIRST_LINE)
		txt = element.text
		return txt

	# @property
	def description_second_line(self):
		'''
		Returns text from description_second_line
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, AboutPageLocator.SECOND_LINE)
		txt = element.text
		return txt

	# @property
	def description_third_line(self):
		'''
		Returns text from description_third_linet
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, AboutPageLocator.THIRD_LINE)
		txt = element.text
		return txt

	# @property
	def description_link(self):
		'''
		Returns href from description text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, AboutPageLocator.LINK)
		href = element.element_href
		return href

