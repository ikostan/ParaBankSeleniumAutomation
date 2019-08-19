#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from pytest import fixture


def pytest_addoption(parser):
	"""
	Pass different values to a test function, depending on command line options
	Source: https://docs.pytest.org/en/latest/example/simple.html
	:param parser:
	:return:
	"""

	parser.addoption('--env',
	                 action="store",
	                 help="Base URL/Environment")

	parser.addoption('--browser',
	                 action="store",
	                 help="Web browser name")

	parser.addoption('--is_headless',
	                 action="store",
	                 help="Headless browser run without a UI")


@fixture(scope='session')
def env(request):
	return request.config.getoption("--env")


@fixture(scope='session')
def browser(request):
	return request.config.getoption("--browser")


@fixture(scope='session')
def is_headless(request):
	return request.config.getoption("--is_headless")

