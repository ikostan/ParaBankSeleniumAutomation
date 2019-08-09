import time
from utils.http_status_code import get_http_status_code
from utils.open_web_browser import open_web_browser
from page_models.admin_page_model import AdminPageModel
from expected_results.page_context.admin_page_context import AdminPageContext


def clean_database():
	'''
	Clean and initialise database.
	Does not check for any errors.
	:return:
	'''

	page_model = AdminPageModel
	page_context = AdminPageContext
	browser = 'chrome'

	print("Open web browser")
	get_http_status_code(AdminPageContext.URL)
	page = open_web_browser(browser=browser,
	                        page_model=page_model,
	                        page_context=page_context)

	print("\nCleaning database...")
	page.hit_clean_button()
	time.sleep(2)

	print("\nInitializing database...")
	page.hit_initialize_button()
	time.sleep(2)

	print("\nClose web browser")
	page.quit()
