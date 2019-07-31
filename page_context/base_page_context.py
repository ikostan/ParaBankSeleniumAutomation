class BasePageContext:
	'''
	Holds expected context values for any relevant page items
	'''

	ROOT_URL = 'https://parabank.parasoft.com'
	URL = ROOT_URL +'/parabank/'

	TITLE = 'ParaBank | '

	SLOGAN = 'Experience the difference'

	ADMIN_LOGO = {
		'href': "admin.htm",
		'src': "images/clear.gif",
		'class': "admin"
	}

	PARA_BANK_LOGO = {
		'href': "index.htm",
		'src': "images/logo.gif",
		'alt': "ParaBank",
		'title': "ParaBank",
		'class': "logo"
	}

	MENU_BUTTONS = {
		'home': {'href': "index.htm",
		         'text': 'home'},
		'about': {'href': "about.htm",
		          'text': 'about'},
		'contact': {'href': "contact.htm",
		            'text': 'contact'}
	}

	LEFT_MENU_ITEMS = {
		'Solutions': {'class': 'Solutions',
		              'text': 'Solutions'},
		'About Us': {'href': 'about.htm',
		             'text': 'About Us'},
		'Services': {'href': 'services.htm',
		             'text': "Services"},
		'Products': {'href': 'http://www.parasoft.com/jsp/products.jsp',
		             'text': 'Products'},
		'Locations': {'href': 'http://www.parasoft.com/jsp/pr/contacts.jsp',
		              'text': 'Locations'},
		'Admin Page': {'href': 'admin.htm',
		               'text': 'Admin Page'}
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

	FOOTER = {
		'footer_menu': {
			'home': {'text': 'Home',
			         'href': "index.htm"},
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
			             'href': "index.htm"},
			'contact_us': {'text': 'Contact Us',
			               'href': "contact.htm"},
		},
		'copyright': '© Parasoft. All rights reserved.',
		'visit': {
			'text': 'Visit us at:www.parasoft.com',
			'href': "http://www.parasoft.com/"
		},
	}
