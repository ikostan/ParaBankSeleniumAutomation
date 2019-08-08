import requests


def get_http_status_code(url):
	'''
	Returns HTTP status code
	Using requests library

	:return:
	'''
	try:
		r = requests.get(url)
		print("\nURL: {}\nHTTP Status code: {}".format(url, r.status_code))
	except ConnectionError as er:
		print('\n{}\n'.format(er))
	return None
