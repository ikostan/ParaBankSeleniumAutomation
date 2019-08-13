#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

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
	USERNAME_ERROR = (By.XPATH, '//*[@id="customer.username.errors"]')

	PASSWORD_TITLE = (By.XPATH, '//*[@id="customerForm"]/table/tbody/tr[11]/td[1]/b')
	PASSWORD_INPUT = (By.XPATH, '//*[@id="customer.password"]')
	PASSWORD_ERROR = (By.XPATH, '//*[@id="customer.password.errors"]')

	CONFIRM_TITLE = (By.XPATH, '//*[@id="customerForm"]/table/tbody/tr[12]/td[1]/b')
	CONFIRM_INPUT = (By.XPATH, '//*[@id="repeatedPassword"]')
	CONFIRM_ERROR = (By.XPATH, '//*[@id="repeatedPassword.errors"]')

	REGISTER_BUTTON = (By.XPATH, '//input[contains(@value, "Register")]')
