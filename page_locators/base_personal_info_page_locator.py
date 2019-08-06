from page_locators.base_page_locator import BasePageLocator
from selenium.webdriver.common.by import By


class BasePersonalInfoPageLocator:
	'''
	Holds all shared locators for 'Register' and 'Forgot Login Info' page web elements.
	Each locator is a tuple.
	Separate the locator strings from the place where they are being used.
	'''

	HEADER = (By.XPATH, '//*[@id="rightPanel"]/h1')
	DESCRIPTION = (By.XPATH, '//*[@id="rightPanel"]/p')

	FIRST_NAME_TITLE = (By.XPATH, '//*[@id="customerForm"]/table/tbody/tr[1]/td[1]/b')
	FIRST_NAME_INPUT = (By.XPATH, '//*[@id="customer.firstName"]')

	LAST_NAME_TITLE = (By.XPATH, '//*[@id="customerForm"]/table/tbody/tr[2]/td[1]/b')
	LAST_NAME_INPUT = (By.XPATH, '//*[@id="customer.lastName"]')

	ADDRESS_TITLE = (By.XPATH, '//*[@id="customerForm"]/table/tbody/tr[3]/td[1]/b')
	ADDRESS_INPUT = (By.XPATH, '//*[@id="customer.address.street"]')

	CITY_TITLE = (By.XPATH, '//*[@id="customerForm"]/table/tbody/tr[4]/td[1]/b')
	CITY_INPUT = (By.XPATH, '//*[@id="customer.address.city"]')

	STATE_TITLE = (By.XPATH, '//*[@id="customerForm"]/table/tbody/tr[5]/td[1]/b')
	STATE_INPUT = (By.XPATH, '//*[@id="customer.address.state"]')

	ZIP_CODE_TITLE = (By.XPATH, '//*[@id="customerForm"]/table/tbody/tr[6]/td[1]/b')
	ZIP_CODE_INPUT = (By.XPATH, '//*[@id="customer.address.zipCode"]')

	PHONE_TITLE = (By.XPATH, '//*[@id="customerForm"]/table/tbody/tr[6]/td[1]/b')
	PHONE_INPUT = (By.XPATH, '//*[@id="customer.address.zipCode"]')

	SSN_TITLE = (By.XPATH, '//*[@id="customerForm"]/table/tbody/tr[6]/td[1]/b')
	SSN_INPUT = (By.XPATH, '//*[@id="customer.address.zipCode"]')
