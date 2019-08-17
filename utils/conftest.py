#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from tests.config import Config
from pytest import fixture


def pytest_addoption(parser):

	parser.addoption('--env',
	                 action="store",
	                 help="Base URL/Environment")

	parser.addoption('--browser',
	                 action="store",
	                 help="Web browser name")


@fixture(scope='session')
def env(request):
	return request.config.getoption("--env")


@fixture(scope='session')
def browser(request):
	return request.config.getoption("--browser")


@fixture(scope='session')
def app_config():
	cfg = Config(env, browser)
	return cfg

