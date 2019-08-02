import os
import shutil
import datetime
import allure
from allure_commons.types import AttachmentType
from functools import partialmethod


def take_screen_shot(driver):
    """
    Take a Screen-shot of the webpage when test Failed.
    Integrated with Allure Reports
    """

    #now = datetime.datetime.now()
    #filename = 'screenshot-{}-{}.png'.format(driver.name, datetime.datetime.strftime(now, '%Y-%m-%d_%H-%M-%S'))
    #driver.save_screenshot(filename)
    #print('\nScreenshot saved as {}. Please check your \'tests\\screenshots\' folder.\n'.format(filename + '.png'))

    # Allure reports can display many different types of provided attachments
    # that can complement a test, step or fixture result.
    # Attachments can be created either with invocation of allure.attach(body, name, attachment_type, extension):
    # Source: https://docs.qameta.io/allure/
    allure.attach(source=driver.get_screenshot_as_png(), name=driver.name, attachment_type=AttachmentType.PNG)


def screenshots_collector():
    '''
    Collect all screenshots and put them into screenshots directory
    :return:
    '''

    screenshots_folder = 'screenshots'
    if not os.path.exists(os.curdir + '\\screenshots'):
        os.mkdir(screenshots_folder)

    now = datetime.datetime.now()
    folder_name = '{}\\screenshots_{}'.format(screenshots_folder, datetime.datetime.strftime(now, '%Y-%m-%d_%H-%M-%S'))

    files = os.listdir(os.curdir)
    for file in files:
        if '.png' in str(file):
            if not os.path.exists(os.curdir + '\\' + folder_name):
                os.mkdir(folder_name)
            shutil.move(file.split('\\')[-1], os.curdir + '\\' + folder_name)


def screenshot_on_fail(browser_attr='page'):
    '''
    Here is a solution using a decorator that wrapps every method on a class that starts test_
    with a wrapper that takes a screenshot if the method raises and Exception.
    The browser_attr is used to tell the decorator how to obtain the web browser (driver).

    Source: https://stackoverflow.com/questions/12024848/automatic-screenshots-when-test-fail-by-selenium-webdriver-in-python
    :param browser_attr:
    :return:
    '''
    def decorator(cls):
        def with_screen_shot(self, fn, *args, **kwargs):
            """Take a Screen-shot of the drive page, when a function fails."""

            try:
                return fn(self, *args, **kwargs)

            except Exception:
                # This will only be reached if the test fails
                page = getattr(self, browser_attr)

                # You have to check first if page object is None
                # otherwise you will get an Exception
                # in case some text was marked as '@unittest.skip('N/A')'
                if page:
                    take_screen_shot(page.driver)
                raise

        for attr, fn in cls.__dict__.items():
            if attr[:5] == 'test_' and callable(fn):
                setattr(cls, attr, partialmethod(with_screen_shot, fn))

        return cls
    return decorator
