#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


class Config:
	"""
	Environment Configuration
	Source: https://www.udemy.com/elegant-automation-frameworks-with-python-and-pytest
	"""
	def __init__(self, env="localhost", browser="chrome", is_headless=True):

		self.base_url = {
			'production': 'https://parabank.parasoft.com',
			'localhost': 'http://localhost:8080',
		}[env.lower()]

		self.is_headless = is_headless

		self.browser = {
			'chrome': 'chrome',
			'edge': 'edge',
			'firefox': 'mozilla'
		}[browser.lower()]

		print('Run configurations -> Browser: {}\n'
		      'Run configurations -> Environment: {}\n'
		      'Run configurations -> Is Headless: {}'.format(self.browser, self.base_url, self.is_headless))

