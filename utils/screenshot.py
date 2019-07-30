import os
import shutil
import datetime


def take_screen_shot(self):
    """Take a Screen-shot of the webpage when test Failed."""

    now = datetime.datetime.now()
    filename = 'screenshot-{}-{}.png'.format(self.driver.name, datetime.datetime.strftime(now, '%Y-%m-%d_%H-%M-%S'))
    self.driver.save_screenshot(filename)
    print('\nScreenshot saved as {}'.format(filename))


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