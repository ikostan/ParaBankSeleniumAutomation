#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from selenium.webdriver.common.by import By


class BasePersonalInfoPageLocator:
	'''
	Holds all shared locators for 'Register' and 'Forgot Login Info' page web elements.
	Each locator is a tuple.
	Separate the locator strings from the place where they are being used.
	'''

	HEADER = (By.XPATH, '//*[@id="rightPanel"]/h1[@class="title"]')
	DESCRIPTION = (By.XPATH, '//*[@id="rightPanel"]/p')

	FIRST_NAME_TITLE = (By.XPATH, '//*[@id="customerForm"]/table/tbody/tr[1]/td[1]/b')
	FIRST_NAME_INPUT = (By.XPATH, '//*[@id="customer.firstName"]')
	FIRST_NAME_ERROR = (By.XPATH, '//*[@id="customer.firstName.errors"]')

	LAST_NAME_TITLE = (By.XPATH, '//*[@id="customerForm"]/table/tbody/tr[2]/td[1]/b')
	LAST_NAME_INPUT = (By.XPATH, '//*[@id="customer.lastName"]')
	LAST_NAME_ERROR = (By.XPATH, '//*[@id="customer.lastName.errors"]')

	ADDRESS_TITLE = (By.XPATH, '//*[@id="customerForm"]/table/tbody/tr[3]/td[1]/b')
	ADDRESS_INPUT = (By.XPATH, '//*[@id="customer.address.street"]')
	ADDRESS_ERROR = (By.XPATH, '//*[@id="customer.address.street.errors"]')

	CITY_TITLE = (By.XPATH, '//*[@id="customerForm"]/table/tbody/tr[4]/td[1]/b')
	CITY_INPUT = (By.XPATH, '//*[@id="customer.address.city"]')
	CITY_ERROR = (By.XPATH, '//*[@id="customer.address.city.errors"]')

	STATE_TITLE = (By.XPATH, '//*[@id="customerForm"]/table/tbody/tr[5]/td[1]/b')
	STATE_INPUT = (By.XPATH, '//*[@id="customer.address.state"]')
	STATE_ERROR = (By.XPATH, '//*[@id="customer.address.state.errors"]')

	ZIP_CODE_TITLE = (By.XPATH, '//*[@id="customerForm"]/table/tbody/tr[6]/td[1]/b')
	ZIP_CODE_INPUT = (By.XPATH, '//*[@id="customer.address.zipCode"]')
	ZIP_CODE_ERROR = (By.XPATH, '//*[@id="customer.address.zipCode.errors"]')

	PHONE_TITLE = (By.XPATH, '//*[@id="customerForm"]/table/tbody/tr[7]/td[1]/b')
	PHONE_INPUT = (By.XPATH, '//*[@id="customer.phoneNumber"]')

	SSN_TITLE = (By.XPATH, '//*[@id="customerForm"]/table/tbody/tr[8]/td[1]/b')
	SSN_INPUT = (By.XPATH, '//*[@id="customer.ssn"]')
	SSN_ERROR = (By.XPATH, '//*[@id="customer.ssn.errors"]')
