import selenium.webdriver
from utils.driver import Driver
from elements.element import Element
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from page_context.base_page_context import BasePageContext
from page_locators.base_page_locator import BasePageLocator
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, InvalidElementStateException


class BasePageModel:
	'''
	The page object pattern intends creating an object for each web page.
	By following this technique a layer of separation between the test code and technical implementation is created.
	'''

	_url = BasePageContext.URL

	def __init__(self, driver: Driver, implicit_wait_time=0, explicit_wait_time=0):
		self._driver = self._set_driver(driver)
		self._set_implicit_wait(implicit_wait_time)
		self._explicit_wait_time = self._set_explicit_wait(explicit_wait_time)

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

	@staticmethod
	def _set_explicit_wait(explicit_wait_time: int):
		'''
		The default value of explicit wait time.
		Its unit is in seconds.
		:param implicit_wait_time:
		:return:
		'''
		if type(explicit_wait_time) != int:
			raise TypeError('\nERROR: wrong data type. Please set "explicit_wait_time" value as integer.\n')
		return explicit_wait_time

	@property
	def explicit_wait_time(self):
		return self._explicit_wait_time

	def go(self):
		'''
		Opens test web page
		:return:
		'''
		self._driver.get(self._url)
		try:
			WebDriverWait(self._driver, self.explicit_wait_time).until(EC.presence_of_element_located((By.TAG_NAME, 'html')))
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
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.SLOGAN)
		return element.text

	@staticmethod
	def _formated_url(url):
		'''
		Removes following from href/url:

		1. https://parabank.parasoft.com/parabank/
		2. ;jsessionid=1219DE07E03D513449C6E1EEA9A73C43

		Result: images/clear.gif

		:param url:
		:return:
		'''
		url = url.replace(BasePageContext.URL, '')

		if ';' in url:
			url = url[:url.index(';')]

		if '/' in url:
			if url.index('/') == 0:
				url = url.replace('/', '')

		return url

	@property
	def _admin_logo_href(self):
		'''
		Returns href value from "Admin Logo" element
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.ADMIN_LOGO_HREF)
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
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.ADMIN_LOGO_IMG)
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
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.ADMIN_LOGO_IMG)
		return element.element_class

	@property
	def _para_bank_logo_href(self):
		'''
		Returns href value from "ParBank Logo" element
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.PARA_BANK_LOGO_HREF)
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
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.PARA_BANK_LOGO_IMG)
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
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.PARA_BANK_LOGO_IMG)
		return element.element_class

	@property
	def para_bank_logo_img_alt(self):
		'''
		Returns ParBank logo img alt value
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.PARA_BANK_LOGO_IMG)
		return element.element_alt

	@property
	def para_bank_logo_img_title(self):
		'''
		Returns ParBank logo img title value
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.PARA_BANK_LOGO_IMG)
		return element.element_title

	@property
	def _home_button_href(self):
		'''
		Returns non formated home button href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.HOME_BUTTON)
		return element.element_href

	@property
	def home_button_formated_href(self):
		'''
		Returns formated home button href
		:return:
		'''
		href = self._formated_url(self._home_button_href)
		return href

	@property
	def home_button_text(self):
		'''
		Returns home button text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.HOME_BUTTON)
		return element.text

	@property
	def _about_button_href(self):
		'''
		Returns non formated about button href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.ABOUT_BUTTON)
		return element.element_href

	@property
	def about_button_formated_href(self):
		'''
		Returns formated about button href
		:return:
		'''
		non_formated_href = self._about_button_href
		href = self._formated_url(non_formated_href)
		return href

	@property
	def about_button_text(self):
		'''
		Returns about button text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.ABOUT_BUTTON)
		return element.text

	@property
	def _contact_button_href(self):
		'''
		Returns non contact about button href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.CONTACT_BUTTON)
		return element.element_href

	@property
	def contact_button_formated_href(self):
		'''
		Returns formated contact button href
		:return:
		'''
		non_formated_href = self._contact_button_href
		href = self._formated_url(non_formated_href)
		return href

	@property
	def contact_button_text(self):
		'''
		Returns contact button text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.CONTACT_BUTTON)
		return element.text

	@property
	def solutions_menu_text(self):
		'''
		Returns SOLUTIONS button text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.SOLUTIONS)
		return element.text

	@property
	def solutions_menu_class(self):
		'''
		Returns SOLUTIONS button text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.SOLUTIONS)
		return element.element_class

	@property
	def _about_usmenu_item_href(self):
		'''
		Returns non formated about us menu item href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.ABOUT_BUTTON)
		return element.element_href

	@property
	def about_us_menu_item_formated_href(self):
		'''
		Returns formated about us menu item href
		:return:
		'''
		non_formated_href = self._about_button_href
		href = self._formated_url(non_formated_href)
		return href

	@property
	def about_us_menu_item_text(self):
		'''
		Returns about us menu item text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.ABOUT_US_MENU_ITEM)
		return element.text

	@property
	def _services_usmenu_item_href(self):
		'''
		Returns non formated services menu item href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.SERVICES_MENU_ITEM)
		return element.element_href

	@property
	def services_us_menu_item_formated_href(self):
		'''
		Returns formated services menu item href
		:return:
		'''
		non_formated_href = self._services_usmenu_item_href
		href = self._formated_url(non_formated_href)
		return href

	@property
	def services_us_menu_item_text(self):
		'''
		Returns services menu item text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.SERVICES_MENU_ITEM)
		txt = element.text
		return txt

	@property
	def _products_menu_item_href(self):
		'''
		Returns non formated products menu item href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.PRODUCTS_MENU_ITEM)
		return element.element_href

	@property
	def products_menu_item_formated_href(self):
		'''
		Returns formated products menu item href
		:return:
		'''
		non_formated_href = self._products_menu_item_href
		href = self._formated_url(non_formated_href)
		return href

	@property
	def products_menu_item_text(self):
		'''
		Returns products menu item text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.PRODUCTS_MENU_ITEM)
		txt = element.text
		return txt

	@property
	def _locations_menu_item_href(self):
		'''
		Returns non formated locations menu item href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.LOCATIONS_MENU_ITEM)
		return element.element_href

	@property
	def locations_menu_item_formated_href(self):
		'''
		Returns formated locations menu item href
		:return:
		'''
		non_formated_href = self._locations_menu_item_href
		href = self._formated_url(non_formated_href)
		return href

	@property
	def locations_menu_item_text(self):
		'''
		Returns locations menu item text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.LOCATIONS_MENU_ITEM)
		txt = element.text
		return txt

	@property
	def _admin_page_menu_item_href(self):
		'''
		Returns non formated admin_page menu item href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.ADMIN_PAGE_MENU_ITEM)
		return element.element_href

	@property
	def admin_page_menu_item_formated_href(self):
		'''
		Returns formated admin_page menu item href
		:return:
		'''
		non_formated_href = self._admin_page_menu_item_href
		href = self._formated_url(non_formated_href)
		return href

	@property
	def admin_page_menu_item_text(self):
		'''
		Returns admin_page menu item text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.ADMIN_PAGE_MENU_ITEM)
		txt = element.text
		return txt

	@property
	def customer_login_title(self):
		'''
		Returns customer login title
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.CUSTOMER_LOGIN_TITLE)
		txt = element.text
		return txt

	@property
	def username_login_title(self):
		'''
		Returns username login title
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.USERNAME_LOGIN_TITLE)
		txt = element.text
		return txt

	@property
	def password_login_title(self):
		'''
		Returns password login title
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.PASSWORD_LOGIN_TITLE)
		txt = element.text
		return txt

	@property
	def username_input_class(self):
		'''
		Returns Username login Input class
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.LOGIN_USERNAME_INPUT)
		atr = element.element_class
		return atr

	@property
	def username_input_type(self):
		'''
		Returns Username login Input type
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.LOGIN_USERNAME_INPUT)
		atr = element.element_type
		return atr

	@property
	def username_input_name(self):
		'''
		Returns Username login Input name
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.LOGIN_USERNAME_INPUT)
		atr = element.element_name
		return atr

	@property
	def password_input_class(self):
		'''
		Returns password login Input class
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.LOGIN_PASSWORD_INPUT)
		atr = element.element_class
		return atr

	@property
	def password_input_type(self):
		'''
		Returns password login Input type
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.LOGIN_PASSWORD_INPUT)
		atr = element.element_type
		return atr

	@property
	def password_input_name(self):
		'''
		Returns password login Input name
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.LOGIN_PASSWORD_INPUT)
		atr = element.element_name
		return atr

	@property
	def login_button_class(self):
		'''
		Returns login_button class
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.CUSTOMER_LOGIN_BUTTON)
		atr = element.element_class
		return atr

	@property
	def login_button_type(self):
		'''
		Returns login_button type
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.CUSTOMER_LOGIN_BUTTON)
		atr = element.element_type
		return atr

	@property
	def login_button_value(self):
		'''
		Returns login_button value
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.CUSTOMER_LOGIN_BUTTON)
		atr = element.element_value
		return atr

	@property
	def _forgot_login_href(self):
		'''
		Returns non formated forgot_login href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FORGOT_LOGIN)
		return element.element_href

	@property
	def forgot_login_formated_href(self):
		'''
		Returns formated forgot_login href
		:return:
		'''
		non_formated_href = self._forgot_login_href
		href = self._formated_url(non_formated_href)
		return href

	@property
	def forgot_login_text(self):
		'''
		Returns forgot_login text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FORGOT_LOGIN)
		txt = element.text
		return txt

	@property
	def _register_href(self):
		'''
		Returns non formated register href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.REGISTER)
		return element.element_href

	@property
	def register_formated_href(self):
		'''
		Returns formated register href
		:return:
		'''
		non_formated_href = self._register_href
		href = self._formated_url(non_formated_href)
		return href

	@property
	def register_text(self):
		'''
		Returns register text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.REGISTER)
		txt = element.text
		return txt

	@property
	def _footer_home_href(self):
		'''
		Returns non formated footer_home href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_HOME)
		return element.element_href

	@property
	def footer_home_formated_href(self):
		'''
		Returns formated footer_home href
		:return:
		'''
		non_formated_href = self._footer_home_href
		href = self._formated_url(non_formated_href)
		return href

	@property
	def footer_home_text(self):
		'''
		Returns footer_home text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_HOME)
		txt = element.text
		return txt

	@property
	def _footer_about_us_href(self):
		'''
		Returns non formated about_us href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_ABOUT_US)
		return element.element_href

	@property
	def footer_about_us_formated_href(self):
		'''
		Returns formated about_us href
		:return:
		'''
		non_formated_href = self._footer_about_us_href
		href = self._formated_url(non_formated_href)
		return href

	@property
	def footer_about_us_text(self):
		'''
		Returns about_us text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_ABOUT_US)
		txt = element.text
		return txt
