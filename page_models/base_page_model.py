import selenium.webdriver
from utils.driver import Driver
from selenium.webdriver.common.by import By
from page_context.base_page_context import BasePageContext
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, InvalidElementStateException


class BasePageModel:
	'''
	The page object pattern intends creating an object for each web page.
	By following this technique a layer of separation between the test code and technical implementation is created.
	'''

	_url = BasePageContext.URL

	def __init__(self, driver: Driver, implicit_wait_time=0):
		self._driver = self._set_driver(driver)
		self._set_implicit_wait(implicit_wait_time)

	@staticmethod
	def _set_driver(driver: selenium.webdriver):
		'''
		Check if driver of type: selenium.webdriver
		:param driver:
		:return:
		'''
		if type(driver) != Driver:
			raise TypeError('\nERROR: please instantiate selenium webdriver using custom Driver class.\n')

		return driver.get_driver()

	def _set_implicit_wait(self, implicit_wait_time: int):
		'''
		The default value of time that can be set using Implicit wait is zero.
		Its unit is in seconds.
		Implicit wait remains associated with the web element until it gets destroyed.
		:param implicit_wait_time:
		:return:
		'''
		if type(implicit_wait_time) != int:
			raise TypeError('\nERROR: wrong data type. Please set "implicit_wait_time" value as integer.\n')
		self._driver.implicitly_wait(implicit_wait_time)
		return None

	def go(self):
		'''
		Opens test web page
		:return:
		'''
		self._driver.get(self._url)
		try:
			WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'html')))
		except TimeoutException:
			raise Exception('\nERROR: The webpage \'{}\' is not available. Please check URL and retry.\n'.format(self._url))
		self._driver.maximize_window()
		return None

	def quit(self):
		'''
		Close web browser window (including all opened tabs)
		:return:
		'''
		if self._driver:
			self._driver.quit()
		return None

	def close(self):
		'''
		Close current tab
		:return:
		'''
		if self._driver:
			self._driver.close()
		return None

	@property
	def driver(self):
		'''
		Returns Selenium webdriver object
		:return:
		'''
		return self._driver

	@property
	def title(self):
		'''
		Returns web page title
		:return:
		'''
		return self._driver.title

	@property
	def url(self):
		'''
		Returns current URL
		:return:
		'''
		return self._driver.current_url
