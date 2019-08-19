#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import time
import allure

from tests.config import Config
from utils.open_web_browser import open_web_browser
from page_object_models.admin_page_model import AdminPageModel
from expected_results.page_content.admin_page_content import AdminPageContent


def clean_database(config: Config):
	'''
	Clean and initialise database.
	Does not check for any errors.
	:return:
	'''

	page_model = AdminPageModel
	page_content = AdminPageContent

	print("Open web browser")
	page = open_web_browser(config=config,
	                        page_model=page_model,
	                        page_content=page_content)

	with allure.step("Press 'CLEAN' button"):
		print("\nCleaning database...")
		page.hit_clean_button()
		time.sleep(2)

	with allure.step("Press 'INITIALIZE' button"):
		print("\nInitializing database...")
		page.hit_initialize_button()
		time.sleep(2)

	with allure.step("Close web browser"):
		page.quit()
