from selenium.webdriver.common.by import By


class BasePageLocator:
	'''
	Holds all relevant locators for any page web elements.
	Each locator is a tuple.
	Separate the locator strings from the place where they are being used.
	'''

	# Admin Logo:
	ADMIN_LOGO_HREF = (By.XPATH, '//*[@id="topPanel"]/a[contains(@href,"/parabank/admin.htm")]')
	ADMIN_LOGO_IMG = (By.XPATH, '//*[@id="topPanel"]/a[contains(@href,"/parabank/admin.htm")]/img')

	# ParaBank Logo:
	PARA_BANK_LOGO_HREF = (By.XPATH, '//*[@id="topPanel"]/a[contains(@href,"/parabank/index.htm")]')
	PARA_BANK_LOGO_IMG = (By.XPATH, '//*[@id="topPanel"]/'
	                                'a[contains(@href,"/parabank/index.htm")]/'
	                                'img[contains(@class,"logo")]')
	SLOGAN = (By.XPATH, '//*[@id="topPanel"]/p[contains(@class,"caption")]')

	# Menu Buttons:
	HOME_BUTTON = (By.XPATH, '//*[@id="headerPanel"]/ul[contains(@class,"button")]/li[contains(@class,"home")]/a')
	ABOUT_BUTTON = (By.XPATH, '//*[@id="headerPanel"]/ul[contains(@class,"button")]/li[contains(@class,"aboutus")]/a')
	CONTACT_BUTTON = (By.XPATH, '//*[@id="headerPanel"]/ul[contains(@class,"button")]/li[contains(@class,"contact")]/a')

	# Left Menu:
	SOLUTIONS = (By.XPATH, '//*[@id="headerPanel"]/'
	                       'ul[contains(@class,"leftmenu")]/'
	                       'li[contains(@class,"Solutions")]')
	ABOUT_US_MENU_ITEM = (By.XPATH, '//*[@id="headerPanel"]/'
	                                'ul[contains(@class,"leftmenu")]/'
	                                'li[2]/'
	                                'a[contains(@href, "about.htm")]')

	SERVICES_MENU_ITEM = (By.XPATH, '//*[@id="headerPanel"]/'
	                                'ul[contains(@class,"leftmenu")]/'
	                                'li[3]/'
	                                'a[contains(@href, "services.htm")]')

	PRODUCTS_MENU_ITEM = (By.XPATH, '//*[@id="headerPanel"]/ul[contains(@class,"leftmenu")]/li[4]/a[contains(@href, "http://www.parasoft.com/jsp/products.jsp")]')
	#PRODUCTS_MENU_ITEM = (By.XPATH, '//*[@id="headerPanel"]/ul[contains(@class,"leftmenu")]/li[4]/a')

	LOCATIONS_MENU_ITEM = (By.XPATH, '//*[@id="headerPanel"]/ul[contains(@class,"leftmenu")]/li[5]/a[contains(@href, "http://www.parasoft.com/jsp/pr/contacts.jsp")]')

	ADMIN_PAGE_MENU_ITEM = (By.XPATH, '//*[@id="headerPanel"]/ul[contains(@class,"leftmenu")]/li[6]/a[contains(@href, "admin.htm")]')

