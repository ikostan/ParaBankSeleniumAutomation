#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import collections
import allure


def step_definition(self, step_description, expected, actual, act=None, click=False):
	"""
	Unit Testing and the Arrange, Act and Assert (AAA) Pattern

	The function is grouping following functional sections:

	1. Arrange all necessary preconditions and inputs.
	2. Act on the object or method under test.
	3. Assert that the expected results have occurred.

	:param click:
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
		# check if a function just a click (no parameters required)
		if act:
			if not click:
				act(expected)
			else:
				act()

		# Assert
		# check if an object is a function
		if isinstance(actual, collections.Callable):
			actual_result = actual()
		else:
			actual_result = actual

		# Log
		print('\nStep: {}\nExpected: {}\nActual: {}'.format(step_description,
		                                                    expected,
		                                                    actual_result))
		self.assertEqual(expected,
		                 actual_result,
		                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
		                                                                                    actual_result))

		return None
