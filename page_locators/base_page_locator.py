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
	PARA_BANK_LOGO_HREF = (By.XPATH, '//*[@id="topPanel"]/'
	                                 'a[contains(@href,"/'
	                                 'parabank/index.htm")]')

	PARA_BANK_LOGO_IMG = (By.XPATH, '//*[@id="topPanel"]/'
	                                'a[contains(@href,"/'
	                                'parabank/index.htm")]/'
	                                'img[contains(@class,"logo")]')

	SLOGAN = (By.XPATH, '//*[@id="topPanel"]/'
	                    'p[contains(@class,"caption")]')

	# Menu Buttons:
	HOME_BUTTON = (By.XPATH, '//*[@id="headerPanel"]/'
	                         'ul[contains(@class,"button")]/'
	                         'li[contains(@class,"home")]/a')

	ABOUT_BUTTON = (By.XPATH, '//*[@id="headerPanel"]/'
	                          'ul[contains(@class,"button")]/'
	                          'li[contains(@class,"aboutus")]/a')

	CONTACT_BUTTON = (By.XPATH, '//*[@id="headerPanel"]/'
	                            'ul[contains(@class,"button")]/'
	                            'li[contains(@class,"contact")]/a')

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

	PRODUCTS_MENU_ITEM = (By.XPATH, '//*[@id="headerPanel"]/'
	                                'ul[contains(@class,"leftmenu")]/'
	                                'li[4]/'
	                                'a[contains(@href, "http://www.parasoft.com/jsp/products.jsp")]')

	LOCATIONS_MENU_ITEM = (By.XPATH, '//*[@id="headerPanel"]/'
	                                 'ul[contains(@class,"leftmenu")]/'
	                                 'li[5]/'
	                                 'a[contains(@href, "http://www.parasoft.com/jsp/pr/contacts.jsp")]')

	ADMIN_PAGE_MENU_ITEM = (By.XPATH, '//*[@id="headerPanel"]/'
	                                  'ul[contains(@class,"leftmenu")]/'
	                                  'li[6]/'
	                                  'a[contains(@href, "admin.htm")]')

	# Customer Login
	CUSTOMER_LOGIN_TITLE = (By.XPATH, '//*[@id="leftPanel"]/h2')
	# Username
	USERNAME_LOGIN_TITLE = (By.XPATH, '//*[@id="loginPanel"]/form/p[1]/b')
	LOGIN_USERNAME_INPUT = (By.XPATH, '//*[@id="loginPanel"]/'
	                                  'form/'
	                                  'div[contains(@class, "login")]/'
	                                  'input[contains(@name, "username")]')
	# Password
	PASSWORD_LOGIN_TITLE = (By.XPATH, '//*[@id="loginPanel"]/form/p[2]/b')
	LOGIN_PASSWORD_INPUT = (By.XPATH, '//*[@id="loginPanel"]/'
	                                  'form/'
	                                  'div[contains(@class, "login")]/'
	                                  'input[contains(@name, "password")]')
	# Button
	CUSTOMER_LOGIN_BUTTON = (By.XPATH, '//*[@id="loginPanel"]/'
	                                   'form/'
	                                   'div[contains(@class, "login")]/'
	                                   'input[contains(@type, "submit")]')

	FORGOT_LOGIN = (By.XPATH, '//*[@id="loginPanel"]/p/a[contains(@href, "lookup.htm")]')
	REGISTER = (By.XPATH, '//*[@id="loginPanel"]/p/a[contains(@href, "register.htm")]')

	# Footer
	FOOTER_HOME = (By.XPATH, '//*[@id="footerPanel"]/ul[1]/li[1]/a[contains(@href, "parabank/index.htm")]]')
	FOOTER_ABOUT_US = (By.XPATH, '//*[@id="footerPanel"]/ul[1]/li[2]/a[contains(@href, "about.htm")]')
	FOOTER_SERVICES = (By.XPATH, '//*[@id="footerPanel"]/ul[1]/li[3]/a[contains(@href, "services.htm")]')
	FOOTER_PRODUCTS = (By.XPATH, '//*[@id="footerPanel"]/ul[1]/li[4]/a[contains(@href, "http://www.parasoft.com/jsp/products.jsp")]')
	FOOTER_LOCATIONS = (By.XPATH, '//*[@id="footerPanel"]/ul[1]/li[5]/a[contains(@href, "http://www.parasoft.com/jsp/contacts.jsp")]')
	FOOTER_FORUM = (By.XPATH, '//*[@id="footerPanel"]/ul[1]/li[6]/a[contains(@href, "http://www.parasoft.com/")]')
	FOOTER_SITE_MAP = (By.XPATH, '//*[@id="footerPanel"]/ul[1]/li[7]/a[contains(@href, "parabank/sitemap.htm")]')
	FOOTER_CONTACT_US = (By.XPATH, '//*[@id="footerPanel"]/ul[1]/li[8]/a[contains(@href, "contact.htm")]')

