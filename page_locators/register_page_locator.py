from selenium.webdriver.common.by import By
from page_locators.base_page_locator import BasePageLocator
from page_locators.base_personal_info_page_locator import BasePersonalInfoPageLocator


class RegisterPageLocator(BasePageLocator, BasePersonalInfoPageLocator):
	'''
	Holds all relevant locators for 'Register' page web elements.
	Each locator is a tuple.
	Separate the locator strings from the place where they are being used.
	'''

	USERNAME_TITLE = (By.XPATH, '//*[@id="customerForm"]/table/tbody/tr[10]/td[1]/b')
	USERNAME_INPUT = (By.XPATH, '//*[@id="customer.username"]')

	PASSWORD_TITLE = (By.XPATH, '//*[@id="customerForm"]/table/tbody/tr[11]/td[1]/b')
	PASSWORD_INPUT = (By.XPATH, '//*[@id="customer.password"]')

	CONFIRM_TITLE = (By.XPATH, '//*[@id="customerForm"]/table/tbody/tr[12]/td[1]/b')
	CONFIRM_INPUT = (By.XPATH, '//*[@id="repeatedPassword"]')

	REGISTER_BUTTON = (By.XPATH, '//*[@id="customerForm"]/table/tbody/tr[13]/td[2]/input[contains(@value, "Register")]')
