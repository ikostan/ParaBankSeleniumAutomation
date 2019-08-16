#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


class Config:

	def __init__(self, env="system", browser="chrome"):

		self.base_url = {
			'system': 'https://parabank.parasoft.com'
		}[env.lower()]

		self.browser = {
			'chrome': 'chrome',
			'edge': 'edge',
			'firefox': 'mozilla'
		}[browser.lower()]

