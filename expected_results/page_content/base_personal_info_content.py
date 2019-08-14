#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


class BasePersonalInfoContent:
	'''
	Holds shared fields/data from "Forgot Login Info" and "Register" forms.
	Error messages also included (fields validation).
	'''

	FORM = {
		'first name': {
			'title': 'First Name:',
			'input': {
				'name': "customer.firstName",
				'class': 'input',
				'type': 'text'
			},
			'error': 'First name is required.',
		},
		'last name': {
			'title': 'Last Name:',
			'input': {
				'name': "customer.lastName",
				'class': 'input',
				'type': 'text'
			},
			'error': 'Last name is required.'
		},
		'address': {
			'title': 'Address:',
			'input': {
				'name': "customer.address.street",
				'class': 'input',
				'type': 'text'
			},
			'error': 'Address is required.'
		},
		'city': {
			'title': 'City:',
			'input': {
				'name': "customer.address.city",
				'class': 'input',
				'type': 'text'
			},
			'error': 'City is required.'
		},
		'state': {
			'title': 'State:',
			'input': {
				'name': "customer.address.state",
				'class': 'input',
				'type': 'text'
			},
			'error': 'State is required.'
		},
		'zip code': {
			'title': 'Zip Code:',
			'input': {
				'name': "customer.address.zipCode",
				'class': 'input',
				'type': 'text'
			},
			'error': 'Zip Code is required.'
		},
		'phone': {
			'title': 'Phone #:',
			'input': {
				'name': "customer.phoneNumber",
				'class': 'input',
				'type': 'text'
			}
		},
		'ssn': {
			'title': 'SSN:',
			'input': {
				'name': "customer.ssn",
				'class': 'input',
				'type': 'text'
			},
			'error': 'Social Security Number is required.'
		},
		'username': {
			'title': 'Username:',
			'input': {
				'name': "customer.username",
				'class': 'input',
				'type': 'text'
			},
			'error': 'Username is required.'
		},
		'password': {
			'title': 'Password:',
			'input': {
				'name': "customer.password",
				'class': 'input',
				'type': 'password'
			},
			'error': 'Password is required.'
		},
		'confirm': {
			'title': 'Confirm:',
			'input': {
				'name': "repeatedPassword",
				'class': 'input',
				'type': 'password'
			},
			'error': 'Password confirmation is required.'
		},
	}
