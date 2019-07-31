import selenium.webdriver
from utils.driver import Driver
from selenium.webdriver.common.by import By
from page_context.base_page_context import BasePageContext
from page_locators.base_page_locator import BasePageLocator
from elements.element import Element
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

	@property
	def slogan(self):
		'''
		Returns slogan text
		:return:
		'''
		element = Element(self.driver, BasePageLocator.SLOGAN)
		return element.text

	@staticmethod
	def _formated_url(url):
		'''
		Removes following from href/url:

		1. https://parabank.parasoft.com/parabank
		2. ;jsessionid=1219DE07E03D513449C6E1EEA9A73C43

		Result: /parabank/images/clear.gif

		:param url:
		:return:
		'''
		url = url.replace(BasePageContext.ROOT_URL, '')
		url = url[:url.index(';')]
		return url

	@property
	def _admin_logo_href(self):
		'''
		Returns href value from "Admin Logo" element
		:return:
		'''
		element = Element(self.driver, BasePageLocator.ADMIN_LOGO_HREF)
		return element.element_href

	@property
	def admin_logo_formated_href(self):
		'''
		Returns href value from "Admin Logo" element
		:return:
		'''
		href = self._formated_url(self._admin_logo_href)
		return href

	@property
	def _admin_logo_img_src(self):
		'''
		Returns admin logo img src value
		:return:
		'''
		element = Element(self.driver, BasePageLocator.ADMIN_LOGO_IMG)
		return element.element_src

	@property
	def admin_logo_formated_img_src(self):
		'''
		Returns admin logo img src value
		:return:
		'''
		src = self._formated_url(self._admin_logo_img_src)
		return src

	@property
	def admin_logo_img_class(self):
		'''
		Returns admin logo img src value
		:return:
		'''
		element = Element(self.driver, BasePageLocator.ADMIN_LOGO_IMG)
		return element.element_class

	@property
	def _para_bank_logo_href(self):
		'''
		Returns href value from "ParBank Logo" element
		:return:
		'''
		element = Element(self.driver, BasePageLocator.PARA_BANK_LOGO_HREF)
		return element.element_href

	@property
	def para_bank_logo_formated_href(self):
		'''
		Returns href value from "ParBank Logo" element
		:return:
		'''
		href = self._formated_url(self._para_bank_logo_href)
		return href

	@property
	def _para_bank_logo_img_src(self):
		'''
		Returns ParBank logo img src value
		:return:
		'''
		element = Element(self.driver, BasePageLocator.PARA_BANK_LOGO_IMG)
		return element.element_src

	@property
	def para_bank_logo_formated_img_src(self):
		'''
		Returns ParBank logo img src value
		:return:
		'''
		src = self._formated_url(self._para_bank_logo_img_src)
		return src

	@property
	def para_bank_logo_img_class(self):
		'''
		Returns ParBank logo img class value
		:return:
		'''
		element = Element(self.driver, BasePageLocator.PARA_BANK_LOGO_IMG)
		return element.element_class

	@property
	def para_bank_logo_img_alt(self):
		'''
		Returns ParBank logo img alt value
		:return:
		'''
		element = Element(self.driver, BasePageLocator.PARA_BANK_LOGO_IMG)
		return element.element_alt

	@property
	def para_bank_logo_img_title(self):
		'''
		Returns ParBank logo img title value
		:return:
		'''
		element = Element(self.driver, BasePageLocator.PARA_BANK_LOGO_IMG)
		return element.element_title
