#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from expected_results.page_content.base_page_content import BasePageContent


class ContactPageContent(BasePageContent):
	"""
	Holds expected results/values for Contact web page
	"""

	URL = BasePageContent.URL + 'contact.htm'

	TITLE = BasePageContent.TITLE + 'Customer Care'

	DESCRIPTION = 'Email support is available by filling out the following form.'

	THANK_YOU = 'Thank you '

	SUCCESS_MESSAGE = 'A Customer Care Representative will be contacting you.'

	CONTACT_FORM = {
		'name': {'title': 'Name:',
		         'id': 'name',
		         "name": 'name',
		         'class': 'input',
		         'type': 'text',
		         'error': 'Name is required.'},
		'email': {'title': 'Email:',
		          'id': 'email',
		          "name": 'email',
		          'class': 'input',
		          'type': 'text',
		          'error': 'Email is required.'},
		"phone": {'title': 'Phone:',
		          'id': 'phone',
		          "name": 'phone',
		          'class': 'input',
		          'type': 'text',
		          'error': 'Phone is required.'},
		'message': {'title': 'Message:',
		            'id': 'message',
		            "name": 'message',
		            'class': 'input',
		            'type': 'text',
		            'error': 'Message is required.'},
		'button': {'value': 'Send to Customer Care',
		           'class': 'button',
		           'type': 'submit'}
	}
