from elements.base_element import BaseElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, \
	NoSuchElementException, \
	InvalidElementStateException, \
	NoSuchAttributeException


class Element(BaseElement):

	@property
	def element_src(self):
		'''
		Returns element src value
		:return:
		'''
		src = super().attribute('src')
		return src

	@property
	def element_class(self):
		'''
		Returns class value
		:return:
		'''
		cls = super().attribute('class')
		return cls

	@property
	def element_alt(self):
		'''
		Returns alt value
		:return:
		'''
		alt = super().attribute('alt')
		return alt

	@property
	def element_title(self):
		'''
		Returns title value
		:return:
		'''
		alt = super().attribute('title')
		return alt

	@property
	def element_href(self):
		'''
		Returns element href value
		:return:
		'''
		href = super().attribute('href')
		return href

	@property
	def element_type(self):
		'''
		Returns element type value
		:return:
		'''
		atr = super().attribute('type')
		return atr

	@property
	def element_name(self):
		'''
		Returns element name value
		:return:
		'''
		atr = super().attribute('name')
		return atr

	@property
	def element_value(self):
		'''
		Returns element value
		:return:
		'''
		atr = super().attribute('value')
		return atr

	@property
	def element_target(self):
		'''
		Returns element target
		:return:
		'''
		atr = super().attribute('target')
		return atr

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
			element = WebDriverWait(super().driver, super().explicit_wait_time).until(EC.element_to_be_clickable(super().locator))
			element.click()
			return None

		except TimeoutException:
			raise InvalidElementStateException('\nERROR: can not find element. The element is invisible or not clickable.\n')
