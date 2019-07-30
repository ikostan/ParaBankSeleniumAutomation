class BasePageContext:
	'''
	Holds expected context values for relevant page items
	'''

	ROOT_URL = 'https://parabank.parasoft.com/parabank'
	URL = ROOT_URL + '/index.htm'

	TITLE = 'ParaBank | Welcome | Online Banking'
	SLOGAN = 'Experience the difference'

	LOGO = {
		'src': "/parabank/images/logo.gif",
		'alt': "ParaBank",
		'title': "ParaBank",
		'class': "logo"
	}

	LEFT_MENU_ITEMS = {
		'Solutions': None,
		'About Us': 'about.htm',
		'Services': 'services.htm',
		'Products': 'http://www.parasoft.com/jsp/products.jsp',
		'Locations': 'http://www.parasoft.com/jsp/pr/contacts.jsp',
		'Admin Page': 'admin.htm'
	}

	LOGIN_PANEL = {
		'title': 'Customer Login',
		'username title': 'Username',
		'password title': 'Password',
		'button label': "Log In"
	}

	REGISTER = {
		'text': 'Register',
		'href': "register.htm"}

	FORGOT_LOGIN = {
		'text': 'Forgot login info?',
		'href': "lookup.htm"
	}

	MENU_BUTTONS = {
		'home': "/parabank/index.htm",
		'about': "about.htm",
		'contact': "contact.htm"
	}

	FOOTER = {
		'footer_menu': {
			'home': {'text': 'Home',
			         'href': "/parabank/index.htm"},
			'about_us': {'text': 'About Us',
			             'href': "about.htm"},
			'services': {'text': 'Services',
			             'href': "services.htm"},
			'products': {'text': 'Products',
			             'href': "http://www.parasoft.com/jsp/products.jsp"},
			'locations': {'text': 'Locations',
			              'href': "http://www.parasoft.com/jsp/pr/contacts.jsp"},
			'forum': {'text': 'Forum',
			          'href': "https://forums.parasoft.com/"},
			'site_map': {'text': 'Site Map',
			             'href': "/parabank/index.htm"},
			'contact_us': {'text': 'Contact Us',
			               'href': "contact.htm"},
		},
		'copyright': '© Parasoft. All rights reserved.',
		'visit': {
			'text': 'Visit us at:www.parasoft.com',
			'href': "http://www.parasoft.com/"
		},
	}
