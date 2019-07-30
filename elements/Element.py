from elements.base_element import BaseElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class Element(BaseElement):

	@property
	def text(self):
		try:
			element = WebDriverWait(super().driver, 10).until(EC.visibility_of_element_located(super().locator))
			text = element.text
			return text.strip()

		except TimeoutException as ec:
			raise NoSuchElementException('ERROR: can not find element. The element is not present on the DOM or invisible.')

	def click(self):
		try:
			element = WebDriverWait(super().driver, 10).until(EC.element_to_be_clickable(super().locator))
			text = element.click()
			return None

		except TimeoutException as ec:
			raise NoSuchElementException('ERROR: can not find element. The element is invisible or not clickable.')
