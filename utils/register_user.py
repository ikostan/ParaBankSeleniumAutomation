#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import time
import allure

from utils.open_web_browser import open_web_browser
from page_object_models.register_page_model import RegisterPageModel
from expected_results.page_content.register_page_content import RegisterPageContent
from utils.step_definition import step_definition


def register_user(user, config):
    '''
    Registers a new user.
    Does not check for any errors.
    Using Selenium webdriver + chrome browser by default
    :param page:
    :param user:
    :return:
    '''

    page_model = RegisterPageModel
    page_context = RegisterPageContent

    print("\nUser registration procedure...")
    print("\n1. Open web browser...")
    page = open_web_browser(config=config,
                            page_model=page_model,
                            page_content=page_context)

    with allure.step("Fill out Register web form"):
        print("\n2. Filling out user data...")
        page.type_first_name(user.first_name)

        page.type_last_name(user.last_name)

        page.type_address(user.address)

        page.type_city(user.city)

        page.type_state(user.state)

        page.type_zip_code(user.zip_code)

        page.type_phone(user.phone)

        page.type_ssn(user.ssn)

        page.type_username(user.username)

        page.type_password(user.password)

        page.type_confirm(user.password)

    with allure.step("Hit 'REGISTER' button"):
        print("\n3. Hit 'REGISTER' button...")
        page.hit_register_btn()
        time.sleep(3)

    with allure.step("Verify \"Welcome\" message"):
        print('Verify "Welcome" message...')
        expected = RegisterPageContent.WELCOME_MESSAGE['message']
        actual = page.welcome_message
        if expected == actual:
            print("OK: Welcome message detected")
        else:
            print("ERROR: Welcome message does not appear")

    with allure.step("Do Log Out"):
        print("\n4. Do Log Out...")
        page.hit_log_out_button()
        time.sleep(3)

    with allure.step("Close web browser"):
        print("\n5. Close web browser...")
        page.quit()
