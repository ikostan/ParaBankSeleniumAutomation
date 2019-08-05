from expected_results.page_context.base_page_context import BasePageContext
from expected_results.page_context.base_personal_info import BasePersonalInfo


class RegisterPageContext(BasePageContext, BasePersonalInfo):
	'''
	Holds fields/data from "Register" form
	'''

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
