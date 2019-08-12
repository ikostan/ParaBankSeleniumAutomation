#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


class BasePersonalInfoContent:
	'''
	Holds shared fields/data from "Forgot Login Info" and "Register" forms
	'''

	FORM = {
		'first_name': {
			'title': 'First Name:',
			'input': {
				'name': "customer.firstName",
				'class': 'input',
				'type': 'text'
			}
		},
		'last_name': {
			'title': 'Last Name:',
			'input': {
				'name': "customer.lastName",
				'class': 'input',
				'type': 'text'
			}
		},
		'address': {
			'title': 'Address:',
			'input': {
				'name': "customer.address.street",
				'class': 'input',
				'type': 'text'
			}
		},
		'city': {
			'title': 'City:',
			'input': {
				'name': "customer.address.city",
				'class': 'input',
				'type': 'text'
			}
		},
		'state': {
			'title': 'State:',
			'input': {
				'name': "customer.address.state",
				'class': 'input',
				'type': 'text'
			}
		},
		'zip_code': {
			'title': 'Zip Code:',
			'input': {
				'name': "customer.address.zipCode",
				'class': 'input',
				'type': 'text'
			}
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
			}
		},
		'username': {
			'title': 'Username:',
			'input': {
				'name': "customer.username",
				'class': 'input',
				'type': 'text'
			}
		},
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
		},
	}
