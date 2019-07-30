class BasePageContext:
	'''
	Holds expected context values for relevant page items
	'''

	ROOT_URL = 'https://parabank.parasoft.com/parabank'
	URL = ROOT_URL + '/index.htm'

	TITLE = 'ParaBank | Welcome | Online Banking'
	SLOGAN = 'Experience the difference'

	LEFT_MENU_ITEMS = {
		'Solutions': None,
		'About Us': 'about.htm',
		'Services': 'services.htm',
		'Products': 'http://www.parasoft.com/jsp/products.jsp',
		'Locations': 'http://www.parasoft.com/jsp/pr/contacts.jsp',
		'Admin Page': 'admin.htm'
	}

	MENU_BUTTONS = {
		'home': "/parabank/index.htm",
		'about': "about.htm",
		'contact': "contact.htm"
	}
