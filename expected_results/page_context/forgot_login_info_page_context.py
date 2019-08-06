from expected_results.page_context.base_page_context import BasePageContext
from expected_results.page_context.base_personal_info_context import BasePersonalInfoContext


class ForgotLoginInfoPageContext(BasePageContext, BasePersonalInfoContext):
	'''
	Holds fields/data from "Forgot Login Info" form
	'''

	TITLE = BasePageContext.TITLE + 'Customer Lookup'

	URL = BasePageContext.URL + 'lookup.htm'

	HEADER = {
		'class': "title",
		'text': 'Customer Lookup'
	}

	DESCRIPTION = {'text': 'Please fill out the following information in order to validate your account.'}

	FIND_MY_LOGIN_INFO_BUTTON = {
		'type': "submit",
		'class': "button",
		'value': "Find My Login Info"
	}
