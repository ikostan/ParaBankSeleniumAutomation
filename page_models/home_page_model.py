import selenium.webdriver
from utils.driver import Driver
from selenium.webdriver.common.by import By
from page_models.base_page_model import BasePageModel
from page_context.home_page_context import HomePageContext
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, InvalidElementStateException


class HomePageModel(BasePageModel):
	'''
	The page object pattern intends creating an object for each web page.
	By following this technique a layer of separation between the test code and technical implementation is created.
	'''

	_url = HomePageContext.URL
