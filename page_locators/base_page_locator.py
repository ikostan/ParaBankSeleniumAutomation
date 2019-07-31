from selenium.webdriver.common.by import By


class BasePageLocator:
	'''
	Holds all relevant locators for any page web elements.
	Each locator is a tuple.
	Separate the locator strings from the place where they are being used.
	'''

	SLOGAN = (By.XPATH, '//*[@id="topPanel"]/p[contains(@class,"caption")]')

	ADMIN_LOGO_HREF = (By.XPATH, '//*[@id="topPanel"]/a[contains(@href,"/parabank/admin.htm")]')
	ADMIN_LOGO_IMG = (By.XPATH, '//*[@id="topPanel"]/a[contains(@href,"/parabank/admin.htm")]/img')

	PARA_BANK_LOGO_HREF = (By.XPATH, '//*[@id="topPanel"]/a[contains(@href,"/parabank/index.htm")]')
	PARA_BANK_LOGO_IMG = (By.XPATH, '//*[@id="topPanel"]/'
	                                'a[contains(@href,"/parabank/index.htm")]/'
	                                'img[contains(@class,"logo")]')


