from selenium.webdriver.common.by import By
from page_locators.base_page_locator import BasePageLocator
from page_locators.base_personal_info_page_locator import BasePersonalInfoPageLocator


class ForgotLoginInfoPageLocator(BasePageLocator, BasePersonalInfoPageLocator):
	'''
	Holds all relevant locators for 'Forgot Login Info' page web elements.
	Each locator is a tuple.
	Separate the locator strings from the place where they are being used.
	'''

	FIND_MY_LOGIN_INFO_BUTTON = (By.XPATH,
	                             '//*[@id="lookupForm"]/table/tbody/tr[8]/td[2]/'
	                             'input[contains(@value, "Find My Login Info")])')
