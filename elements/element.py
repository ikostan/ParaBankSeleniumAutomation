#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from elements.base_element import BaseElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, \
	InvalidElementStateException, \
	NoSuchAttributeException


class Element(BaseElement):

	@property
	def element_src(self):
		'''
		Returns element src value
		:return:
		'''
		src = self.attribute('src')
		return src

	@property
	def element_class(self):
		'''
		Returns class value
		:return:
		'''
		cls = self.attribute('class')
		return cls

	@property
	def element_alt(self):
		'''
		Returns alt value
		:return:
		'''
		alt = self.attribute('alt')
		return alt

	@property
	def element_title(self):
		'''
		Returns title value
		:return:
		'''
		alt = self.attribute('title')
		return alt

	@property
	def element_href(self):
		'''
		Returns element href value
		:return:
		'''
		href = self.attribute('href')
		return href

	@property
	def element_type(self):
		'''
		Returns element type value
		:return:
		'''
		atr = self.attribute('type')
		return atr

	@property
	def element_name(self):
		'''
		Returns element name value
		:return:
		'''
		atr = self.attribute('name')
		return atr

	@property
	def element_value(self):
		'''
		Returns element value
		:return:
		'''
		atr = self.attribute('value')
		return atr

	@property
	def element_target(self):
		'''
		Returns element target
		:return:
		'''
		atr = self.attribute('target')
		return atr

	@property
	def text(self):
		'''
		Returns inner text or NoSuchElementException
		in case element is invisible or not present on the DOM
		:return:
		'''
		try:
			text = self.element.text
			return text

		except TimeoutException:
			raise NoSuchAttributeException(
				'\nERROR: The element has no attribute "text".\n'
				'LOCATOR: {}\n'.format(self.locator))

	def press_button(self):
		'''
		Clicks on web element or returns InvalidElementStateException
		in case the element is invisible or not clickable.
		:return:
		'''
		try:
			element = WebDriverWait(self.driver,
			                        self.explicit_wait_time).until(EC.element_to_be_clickable(self.locator))
			element.click()
			return None

		except TimeoutException:
			raise InvalidElementStateException(
				'\nERROR: can not find element. The element is invisible or not clickable.\n')

	def is_visible(self):
		'''
		Checks is element visible.
		Returns True on success.
		Returns False on failure.
		:return:
		'''
		try:
			element = WebDriverWait(self.driver,
			                        self.explicit_wait_time).until(EC.visibility_of_element_located(self.locator))
			return True
		except TimeoutException:
			return False

	def write(self, text):
		'''
		Clear the input field
		Writes into web element / input field
		:param text:
		:return:
		'''
		self.element.clear()
		self.element.send_keys(text)
		return None
