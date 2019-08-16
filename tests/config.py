#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


class Config:
	"""
	Environment Configuration
	Source: https://www.udemy.com/elegant-automation-frameworks-with-python-and-pytest
	"""
	def __init__(self, env="system", browser="chrome"):

		self.base_url = {
			'system': 'https://parabank.parasoft.com'
		}[env.lower()]

		self.browser = {
			'chrome': 'chrome',
			'edge': 'edge',
			'firefox': 'mozilla'
		}[browser.lower()]

		print('Run configurations -> Browser: {}\n'
		      'Run configurations -> Environment: {}\n'.format(self.browser, self.base_url))

