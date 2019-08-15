#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/
import collections
from unittest.test.testmock.testpatch import function

import allure


def step_definition(self, expected, actual, act=None, step_description='N/A', click=False):
	"""
	Unit Testing and the Arrange, Act and Assert (AAA) Pattern
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
