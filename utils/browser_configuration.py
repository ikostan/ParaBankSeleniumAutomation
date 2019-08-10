#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def browser_configuration():
	'''
	Returns browser name from dictionary
	:return:
	'''

	browsers = {1: 'chrome',
	            2: 'edge',
	            3: 'mozilla'}

	browser = browsers[1]
	print('Run configuration: {}'.format(browser))

	return browser
