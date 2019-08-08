import allure
import unittest


def assert_equal_step(expected, actual, description, step, severity):

	allure.dynamic.severity(severity)
	with allure.step(description):
		print('\nStep: {}. Expected: {}. Actual: {}.\n'.format(step, expected, actual))
		unittest.TestCase.assertEqual(expected, actual)
