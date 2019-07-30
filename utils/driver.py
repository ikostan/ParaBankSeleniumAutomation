from drivers.path_config import DriverPath
from selenium.common.exceptions import WebDriverException, SessionNotCreatedException
from selenium.webdriver.opera.options import Options
from selenium import webdriver
import platform
import os


class Driver:

    _driver_path = {

        'chrome': DriverPath.CHROME_WEB_DRIVER_PATH,
        'ie': DriverPath.IE_WEB_DRIVER_PATH,
        'opera': DriverPath.OPERA_WEB_DRIVER_PATH,
        'mozilla': DriverPath.MOZILLA_WEB_DRIVER_PATH,
        'edge': DriverPath.EDGE_WEB_DRIVER_PATH
    }

    def __init__(self, browser: str):

        if browser not in self._driver_path.keys():
            raise NameError("Invalid browser name: {}."
                            "\nOnly following browsers supported: {}".format(browser,
                                                                             ', '.join([key for key in self._driver_path.keys()])))

        self.browser = browser
        self._set_driver()

    def _set_driver(self):

        if self.browser == 'opera':

            options = Options()
            options.binary_location = DriverPath.OPERA_BINARY_PATH
            print('\nBinary Path: {}'.format(DriverPath.OPERA_BINARY_PATH))

            try:
                self.driver = webdriver.Opera(options=options)

            except SessionNotCreatedException as e:
                print('\nSessionNotCreatedException:', e.msg)
                raise

            except WebDriverException as e:

                print('\nWebDriverException:', e.msg)
                path = self._get_driver_path()
                print('Trying to look for a \'operadriver\' under:\n{}'.format(path))
                self.driver = webdriver.Opera(options=options, executable_path=path)

        if self.browser == 'chrome':
            try:
                self.driver = webdriver.Chrome()

            except WebDriverException as e:
                print('\nPlease note:', e.msg)
                path = self._get_driver_path()
                print('Trying to look for a \'chromedriver\' under:\n{}'.format(path))
                self.driver = webdriver.Chrome(executable_path=path)

        if self.browser == 'ie':
            try:
                self.driver = webdriver.Ie()

            except WebDriverException as e:
                print('\nPlease note:', e.msg)
                path = self._get_driver_path()
                print('Trying to look for a \'IEDriverServer\' under:\n{}'.format(path))
                self.driver = webdriver.Ie(executable_path=path)

        if self.browser == 'mozilla':
            try:
                self.driver = webdriver.Firefox()
                
            except WebDriverException as e:
                print('\nPlease note:', e.msg)
                path = self._get_driver_path()
                print('Trying to look for a \'geckodriver\' under:\n{}'.format(path))
                self.driver = webdriver.Firefox(executable_path=path)

        if self.browser == 'edge':

            # Purpose:	Probe the underlying platform’s hardware, operating system,
            # and interpreter version information.

            # print('Version tuple:', platform.python_version_tuple())
            # print('Compiler     :', platform.python_compiler())
            # print('Build        :', platform.python_build())
            if sum(int(i) for i in platform.python_version_tuple()) > 13:
                print('\nVersion:', platform.python_version())
                print('WebDriver is now a Feature On Demand')
                print('For more info please check: {}'.format(
                    'https://blogs.windows.com/msedgedev/2018/06/14/'
                    'webdriver-w3c-recommendation-feature-on-demand/#Rg8g2hRfjBQQVRXy.97\n'))
                self.driver = webdriver.Edge()
            else:
                path = self._get_driver_path()
                print('Trying to look for a \'MicrosoftWebDriver\' under:\n{}'.format(path))
                self.driver = webdriver.Edge(executable_path=path)

    @staticmethod
    def _get_root_dir():
        root_dir = os.path.dirname(os.path.realpath(__file__)).split('\\')
        dir_list = [str(i) for i in root_dir]
        root_dir_index = dir_list.index("SELENIUM_WEBDRIVER_WORKING_WITH_ELEMENTS")
        root = '\\'.join(root_dir[:root_dir_index + 1])
        print('ROOT DIR:\n', root)
        return root

    def _get_driver_path(self):
        return self._get_root_dir() + self._driver_path[self.browser]

    def get_driver(self):
        return self.driver
