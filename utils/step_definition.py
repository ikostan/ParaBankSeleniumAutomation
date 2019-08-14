#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure


def step_definition(self, expected, actual, step_description='N/A'):

	with allure.step(step_description):
		print('\nStep: {}\nExpected: {}\nActual: {}'.format(step_description,
		                                                    expected,
		                                                    actual))
		self.assertEqual(expected,
		                 actual,
		                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
		                                                                                    actual))
