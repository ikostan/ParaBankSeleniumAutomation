#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from expected_results.page_content.login_page_content import LoginPageContent
from expected_results.page_content.overview_page_content import OverviewPageContent
from utils.driver import Driver
from elements.element import Element

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_locators.base_page_locator import BasePageLocator
from expected_results.page_content.base_page_content import BasePageContent
from page_locators.account_services_menu_locator import AccountServicesMenuLocator


class BasePageModel:
	'''
	The page object pattern intends creating an object for each web page.
	By following this technique a layer of separation between the test code and technical implementation is created.
	'''

	_url = BasePageContent.URL

	def __init__(self, driver: Driver, implicit_wait_time=5, explicit_wait_time=10):
		self._driver = self._set_driver(driver)
		self._set_implicit_wait(implicit_wait_time)
		self._explicit_wait_time = self._set_explicit_wait(explicit_wait_time)

	@staticmethod
	def _set_driver(driver):
		'''
		Check if driver of type: selenium.webdriver
		:param driver:
		:return:
		'''

		print('\nDriver type: {}'.format(type(driver)))  # debug only

		if isinstance(driver, Driver):
			return driver.get_driver()

		return driver

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

	@property
	def implicit_wait_time(self):
		return self._implicit_wait_time

	def go(self):
		'''
		Opens test web page
		:return:
		'''

		self._driver.get(self._url)
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

	# @property
	def title(self):
		'''
		Returns web page title
		:return:
		'''
		return self._driver.title

	# @property
	def url(self):
		'''
		Returns current URL
		:return:
		'''
		url = self._driver.current_url

		if ';' in url:
			url = url[:url.index(';')]

		if '?ConnType=JDBC' in url:
			url = url[:url.index('?ConnType=JDBC')]

		return url

	# @property
	def slogan(self):
		'''
		Returns slogan text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.SLOGAN)
		return element.text

	@staticmethod
	def _formated_url(url: str):
		'''
		Removes following from href/url:

		1. https://parabank.parasoft.com/parabank/
		2. ;jsessionid=1219DE07E03D513449C6E1EEA9A73C43

		Result: images/clear.gif

		:param url:
		:return:
		'''
		url = url.replace(BasePageContent.URL, '')

		if ';' in url:
			if '?_wadl&_type=xml' in url:
				url = url[:url.index(';')] + '?_wadl&_type=xml'
			else:
				url = url[:url.index(';')]

		return url

	# @property
	def admin_logo_formated_href(self):
		'''
		Returns href value from "Admin Logo" element
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.ADMIN_LOGO_HREF)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def admin_logo_formated_img_src(self):
		'''
		Returns admin logo img src value
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.ADMIN_LOGO_IMG)
		src = self._formated_url(element.element_src)
		return src

	# @property
	def admin_logo_img_class(self):
		'''
		Returns admin logo img src value
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.ADMIN_LOGO_IMG)
		return element.element_class

	# @property
	def para_bank_logo_formated_href(self):
		'''
		Returns href value from "ParBank Logo" element
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.PARA_BANK_LOGO_HREF)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def para_bank_logo_formated_img_src(self):
		'''
		Returns ParBank logo img src value
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.PARA_BANK_LOGO_IMG)
		src = self._formated_url(element.element_src)
		return src

	# @property
	def para_bank_logo_img_class(self):
		'''
		Returns ParBank logo img class value
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.PARA_BANK_LOGO_IMG)
		return element.element_class

	# @property
	def para_bank_logo_img_alt(self):
		'''
		Returns ParBank logo img alt value
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.PARA_BANK_LOGO_IMG)
		return element.element_alt

	# @property
	def para_bank_logo_img_title(self):
		'''
		Returns ParBank logo img title value
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.PARA_BANK_LOGO_IMG)
		return element.element_title

	# @property
	def home_button_formated_href(self):
		'''
		Returns formated home button href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.HOME_BUTTON)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def home_button_text(self):
		'''
		Returns home button text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.HOME_BUTTON)
		return element.text

	# @property
	def about_button_formated_href(self):
		'''
		Returns formated about button href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.ABOUT_BUTTON)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def about_button_text(self):
		'''
		Returns about button text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.ABOUT_BUTTON)
		return element.text

	# @property
	def contact_button_formated_href(self):
		'''
		Returns formated contact button href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.CONTACT_BUTTON)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def contact_button_text(self):
		'''
		Returns contact button text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.CONTACT_BUTTON)
		return element.text

	# @property
	def solutions_menu_text(self):
		'''
		Returns SOLUTIONS button text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.SOLUTIONS)
		return element.text

	# @property
	def solutions_menu_class(self):
		'''
		Returns SOLUTIONS button text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.SOLUTIONS)
		return element.element_class

	# @property
	def about_us_menu_item_formated_href(self):
		'''
		Returns formated about us menu item href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.ABOUT_BUTTON)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def about_us_menu_item_text(self):
		'''
		Returns about us menu item text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.ABOUT_US_MENU_ITEM)
		return element.text

	# @property
	def services_us_menu_item_formated_href(self):
		'''
		Returns formated services menu item href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.SERVICES_MENU_ITEM)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def services_us_menu_item_text(self):
		'''
		Returns services menu item text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.SERVICES_MENU_ITEM)
		txt = element.text
		return txt

	# @property
	def products_menu_item_formated_href(self):
		'''
		Returns formated products menu item href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.PRODUCTS_MENU_ITEM)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def products_menu_item_text(self):
		'''
		Returns products menu item text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.PRODUCTS_MENU_ITEM)
		txt = element.text
		return txt

	# @property
	def locations_menu_item_formated_href(self):
		'''
		Returns formated locations menu item href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.LOCATIONS_MENU_ITEM)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def locations_menu_item_text(self):
		'''
		Returns locations menu item text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.LOCATIONS_MENU_ITEM)
		txt = element.text
		return txt

	# @property
	def admin_page_menu_item_formated_href(self):
		'''
		Returns formated admin_page menu item href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.ADMIN_PAGE_MENU_ITEM)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def admin_page_menu_item_text(self):
		'''
		Returns admin_page menu item text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.ADMIN_PAGE_MENU_ITEM)
		txt = element.text
		return txt

	# @property
	def customer_login_title(self):
		'''
		Returns customer login title
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.CUSTOMER_LOGIN_TITLE)
		txt = element.text
		return txt

	# @property
	def username_login_title(self):
		'''
		Returns username login title
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.USERNAME_LOGIN_TITLE)
		txt = element.text
		return txt

	# @property
	def password_login_title(self):
		'''
		Returns password login title
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.PASSWORD_LOGIN_TITLE)
		txt = element.text
		return txt

	# @property
	def username_input_class(self):
		'''
		Returns Username login Input class
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.LOGIN_USERNAME_INPUT)
		atr = element.element_class
		return atr

	# @property
	def username(self):
		'''
		Returns Username value
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.LOGIN_USERNAME_INPUT)
		value = element.element_value
		return value

	# @property
	def username_input_type(self):
		'''
		Returns Username login Input type
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.LOGIN_USERNAME_INPUT)
		atr = element.element_type
		return atr

	def enter_username(self, username):
		'''
		Type username into Username input field
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.LOGIN_USERNAME_INPUT)
		element.write(username)
		return None

	# @property
	def username_input_name(self):
		'''
		Returns Username login Input name
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.LOGIN_USERNAME_INPUT)
		atr = element.element_name
		return atr

	# @property
	def password(self):
		'''
		Returns Password value
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.LOGIN_PASSWORD_INPUT)
		value = element.element_value
		return value

	# @property
	def password_input_class(self):
		'''
		Returns password login Input class
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.LOGIN_PASSWORD_INPUT)
		atr = element.element_class
		return atr

	# @property
	def password_input_type(self):
		'''
		Returns password login Input type
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.LOGIN_PASSWORD_INPUT)
		atr = element.element_type
		return atr

	# @property
	def password_input_name(self):
		'''
		Returns password login Input name
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.LOGIN_PASSWORD_INPUT)
		atr = element.element_name
		return atr

	def enter_password(self, password):
		'''
		Type password into Password input field
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.LOGIN_PASSWORD_INPUT)
		element.write(password)
		return None

	# @property
	def login_button_class(self):
		'''
		Returns login_button class
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.CUSTOMER_LOGIN_BUTTON)
		atr = element.element_class
		return atr

	# @property
	def login_button_type(self):
		"""
		Returns login_button type
		:return:
		"""
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.CUSTOMER_LOGIN_BUTTON)
		atr = element.element_type
		return atr

	# @property
	def login_button_value(self):
		"""
		Returns login_button value
		:return:
		"""
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.CUSTOMER_LOGIN_BUTTON)
		atr = element.element_value
		return atr

	def hit_login_button(self, ErrorPageModel=None):
		"""
		1. Click on Log In button
		2. Wait until URL changes
		3. Returns OverviewPageModel object on success
		4. Return TimeOut exception on failure
		:return:
		"""
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.CUSTOMER_LOGIN_BUTTON)
		current_url = self.url()
		element.press_button()
		WebDriverWait(self.driver, self.explicit_wait_time).until(EC.url_changes(current_url))

		if self.url() == OverviewPageContent.URL:
			from page_object_models.overview_page_model import OverviewPageModel
			return OverviewPageModel(driver=self.driver,
			                         implicit_wait_time=5,
			                         explicit_wait_time=10)

		if self.url() == LoginPageContent.URL:
			from page_object_models.login_page_model import LoginPageModel
			return LoginPageModel(driver=self.driver,
			                      implicit_wait_time=5,
			                      explicit_wait_time=10)

		raise Exception("Unknown URL: {} > Flow is not implemented".format(self.driver.current_url))

	# @property
	def forgot_login_formated_href(self):
		"""
		Returns formated forgot_login href
		:return:
		"""
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FORGOT_LOGIN)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def forgot_login_text(self):
		"""
		Returns forgot_login text
		:return:
		"""
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FORGOT_LOGIN)
		txt = element.text
		return txt

	# @property
	def register_formated_href(self):
		'''
		Returns formated register href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.REGISTER)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def register_text(self):
		'''
		Returns register text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.REGISTER)
		txt = element.text
		return txt

	# @property
	def footer_home_formated_href(self):
		'''
		Returns formated footer_home href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_HOME)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def footer_home_text(self):
		'''
		Returns footer_home text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_HOME)
		txt = element.text
		return txt

	# @property
	def footer_about_us_formated_href(self):
		'''
		Returns formated about_us href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_ABOUT_US)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def footer_about_us_text(self):
		'''
		Returns about_us text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_ABOUT_US)
		txt = element.text
		return txt

	# @property
	def footer_services_formated_href(self):
		'''
		Returns formated services href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_SERVICES)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def footer_services_text(self):
		'''
		Returns services text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_SERVICES)
		txt = element.text
		return txt

	# @property
	def footer_products_formated_href(self):
		'''
		Returns formated products href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_PRODUCTS)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def footer_products_text(self):
		'''
		Returns products text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_PRODUCTS)
		txt = element.text
		return txt

	# @property
	def footer_locations_formated_href(self):
		'''
		Returns formated locations href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_LOCATIONS)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def footer_locations_text(self):
		'''
		Returns products text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_LOCATIONS)
		txt = element.text
		return txt

	# @property
	def footer_forum_formated_href(self):
		'''
		Returns formated forum href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_FORUM)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def footer_forum_text(self):
		'''
		Returns forum text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_FORUM)
		txt = element.text
		return txt

	# @property
	def footer_site_map_formated_href(self):
		'''
		Returns formated site_map href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_SITE_MAP)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def footer_site_map_text(self):
		'''
		Returns site_map text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_SITE_MAP)
		txt = element.text
		return txt

	# @property
	def footer_contact_us_formated_href(self):
		'''
		Returns formated contact_us href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_CONTACT_US)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def footer_contact_us_text(self):
		'''
		Returns contact_us text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_CONTACT_US)
		txt = element.text
		return txt

	# @property
	def footer_copyright_text(self):
		'''
		Returns copyright text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_COPYRIGHT)
		txt = element.text
		return txt

	# @property
	def footer_copyright_class(self):
		'''
		Returns copyright class
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_COPYRIGHT)
		atr = element.element_class
		return atr

	# @property
	def footer_visit_link_formated_href(self):
		'''
		Returns formated visit link href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_VISIT_US_LINK)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def footer_visit_link_text(self):
		'''
		Returns visit link text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_VISIT_US_LINK)
		txt = element.text
		return txt

	# @property
	def footer_visit_link_target(self):
		'''
		Returns visit us target
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_VISIT_US_LINK)
		atr = element.element_target
		return atr

	# @property
	def footer_visit_us_text(self):
		'''
		Returns visit us text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_VISIT_US)
		txt = element.text
		return txt

	# Account Services Menu - visible only when user logged in
	# @property
	def welcome_message(self):
		'''
		Returns 'welcome' message that appears above "Account Services" menu
		:param user:
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, AccountServicesMenuLocator.WELCOME_MESSAGE)
		txt = element.text
		return txt

	# @property
	def account_services_menu_title(self):
		'''
		Returns "Account Services" menu header
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, AccountServicesMenuLocator.ACCOUNT_SERVICES_HEADER)
		txt = element.text
		return txt

	# @property
	def account_services_menu_is_visible(self):
		'''
		Returns is "Account Services" menu header visible
		:return:
		'''
		try:
			element = Element(self.driver, self.explicit_wait_time, AccountServicesMenuLocator.ACCOUNT_SERVICES_HEADER)
			is_visible = element.is_visible()
			return is_visible
		except NoSuchElementException:
			return False

	def open_new_account(self):
		'''
		Click on "Open New Account"
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, AccountServicesMenuLocator.OPEN_NEW_ACCOUNT)
		element.press_button()
		return None

	def accounts_overview(self):
		'''
		Click on "Account Overview"
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, AccountServicesMenuLocator.ACCOUNTS_OVERVIEW)
		element.press_button()
		return None

	def transfer_funds(self):
		'''
		Click on "Transfer Funds"
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, AccountServicesMenuLocator.TRANSFER_FUNDS)
		element.press_button()
		return None

	def bill_pay(self):
		'''
		Click on "Bill Pay"
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, AccountServicesMenuLocator.BILL_PAY)
		element.press_button()
		return None

	def find_transactions(self):
		'''
		Click on "Find Transactions"
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, AccountServicesMenuLocator.FIND_TRANSACTIONS)
		element.press_button()
		return None

	def update_contact_info(self):
		'''
		Click on "Update Contact Info"
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, AccountServicesMenuLocator.UPDATE_CONTACT_INFO)
		element.press_button()
		return None

	def request_loan(self):
		'''
		Click on "Request Loan"
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, AccountServicesMenuLocator.REQUEST_LOAN)
		element.press_button()
		return None

	def hit_log_out_button(self):
		'''
		1. Click on "Log Out"
		2. Wait until URL changes
		3. Returns HomePageModel on success
		4. Return TimeoutException on failure

		An expectation for checking the current url.
        url is the expected url, which must not be an exact match
        returns True if the url is different, false otherwise.

        Source: https://seleniumhq.github.io/selenium/docs/api/py/_modules/selenium/webdriver/support/expected_conditions.html#url_changes
		:return:
		'''

		current_url = self.driver.current_url
		element = Element(self.driver, self.explicit_wait_time, AccountServicesMenuLocator.LOG_OUT)
		element.press_button()
		WebDriverWait(self.driver, self.explicit_wait_time).until(EC.url_changes(current_url))
		from page_object_models.home_page_model import HomePageModel
		return HomePageModel(driver=self.driver,
		                     implicit_wait_time=5,
		                     explicit_wait_time=10)
