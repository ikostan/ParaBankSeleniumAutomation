from elements.base_element import BaseElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, InvalidElementStateException


class Element(BaseElement):

	@property
	def text(self):
		'''
		Returns inner text or NoSuchElementException
		in case element is invisible or not present on the DOM
		:return:
		'''
		try:
			element = WebDriverWait(super().driver, 10).until(EC.visibility_of_element_located(super().locator))
			text = element.text
			return text

		except TimeoutException:
			raise NoSuchElementException('\nERROR: can not find element. The element is not present on the DOM or invisible.\n')

	def click(self):
		'''
		Clicks on web element or returns InvalidElementStateException
		in case the element is invisible or not clickable.
		:return:
		'''
		try:
			element = WebDriverWait(super().driver, 10).until(EC.element_to_be_clickable(super().locator))
			text = element.click()
			return None

		except TimeoutException:
			raise InvalidElementStateException('\nERROR: can not find element. The element is invisible or not clickable.\n')
