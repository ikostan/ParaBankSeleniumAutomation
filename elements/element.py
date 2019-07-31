from elements.base_element import BaseElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, \
	NoSuchElementException, \
	InvalidElementStateException, \
	NoSuchAttributeException


class Element(BaseElement):

	@property
	def img_src(self):
		'''
		Returns src value
		:return:
		'''
		src = super().attribute('src')
		return src

	@property
	def img_class(self):
		'''
		Returns class value
		:return:
		'''
		src = super().attribute('class')
		return src

	@property
	def href(self):
		'''
		Returns href value
		:return:
		'''
		href = super().attribute('href')
		return href

	@property
	def text(self):
		'''
		Returns inner text or NoSuchElementException
		in case element is invisible or not present on the DOM
		:return:
		'''
		try:
			text = super().element.text
			return text

		except TimeoutException:
			raise NoSuchAttributeException(
				'\nERROR: The element has no attribute "text".\n'
				'LOCATOR: {}\n'.format(super().locator))

	def click(self):
		'''
		Clicks on web element or returns InvalidElementStateException
		in case the element is invisible or not clickable.
		:return:
		'''
		try:
			element = WebDriverWait(super().driver, 10).until(EC.element_to_be_clickable(super().locator))
			element.click()
			return None

		except TimeoutException:
			raise InvalidElementStateException('\nERROR: can not find element. The element is invisible or not clickable.\n')
