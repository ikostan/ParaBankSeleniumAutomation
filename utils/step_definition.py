#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure


def step_definition(self, expected, actual, act=None, step_description='N/A'):
	"""
	Unit Testing and the Arrange, Act and Assert (AAA) Pattern
	:param self:
	:param expected:
	:param act:
	:param actual:
	:param step_description:
	:return:
	"""

	with allure.step(step_description):
		# Arrange
		expected = expected

		# Act
		if act:
			act(expected)

		# Assert
		actual_result = actual()

		# Log
		print('\nStep: {}\nExpected: {}\nActual: {}'.format(step_description,
		                                                    expected,
		                                                    actual_result))
		self.assertEqual(expected,
		                 actual_result,
		                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
		                                                                                    actual_result))

		return None
