from expected_results.page_context.base_page_context import BasePageContext
from expected_results.page_context.base_personal_info_context import BasePersonalInfoContext


class RegisterPageContext(BasePageContext, BasePersonalInfoContext):
	'''
	Holds fields/data from "Register" form
	'''

	TITLE = BasePageContext.TITLE + 'Register for Free Online Account Access'

	URL = BasePageContext.URL + 'register.htm'

	HEADER = {
		'class': "title",
		'text': 'Signing up is easy!'
	}

	DESCRIPTION = {'text': 'If you have an account with us you can sign-up for free instant online access. '
	                       'You will have to provide some personal information.'}

	REGISTER_FORM = {
		'password': {
			'title': 'Password:',
			'input': {
				'name': "customer.password",
				'class': 'input',
				'type': 'password'
			}
		},
		'confirm': {
			'title': 'Confirm:',
			'input': {
				'name': "repeatedPassword",
				'class': 'input',
				'type': 'password'
			}
		}
	}

	REGISTER_BUTTON = {
		'type': "submit",
		'class': "button",
		'value': "Register"
	}

	WELCOME_MESSAGE = {
		'header': 'Welcome ',
		'message': 'Your account was created successfully. You are now logged in.'
	}
