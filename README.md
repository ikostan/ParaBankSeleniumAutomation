[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](http://unlicense.org/)
# Selenium Automation for Para Bank Web App

<div align="center"> 
<img width="50%" height="50%" src="https://github.com/ikostan/ParaBankSeleniumAutomation/blob/master/images/selenium-python-logo.png" hspace="10">
</div>

### Table of Contents:<br/>
1. <a href="#parabank">PARA BANK ParaSoft Demo App</a>
2. <a href="#doc">Official Documentation</a>
3. <a href="#dev">Dev Environment</a>
4. <a href="#tech_issues">Tech Issues and Problem Solving</a>
5. [Docs](https://github.com/ikostan/ParaBankSeleniumAutomation/tree/master/docs):<br/>
    - [Parasoft: Setting Up ParaBank](https://github.com/ikostan/ParaBankSeleniumAutomation/blob/master/docs/Setting_Up_ParaBank.pdf)
6. [Selenium Webdriver](https://github.com/ikostan/ParaBankSeleniumAutomation/tree/master/drivers):<br/>
    - [ChromeDriver](https://github.com/ikostan/ParaBankSeleniumAutomation/tree/master/drivers/chrome)<br/>
    - [Microsoft WebDriver](https://github.com/ikostan/ParaBankSeleniumAutomation/tree/master/drivers/microsoft_edge)<br/>
    - [geckodriver](https://github.com/ikostan/ParaBankSeleniumAutomation/tree/master/drivers/mozilla_geckodriver)<br/>
7. [Web Element](https://github.com/ikostan/ParaBankSeleniumAutomation/tree/master/elements)<br/>
8. [Expected Results](https://github.com/ikostan/ParaBankSeleniumAutomation/tree/master/expected_results)<br/>
9. [Page/Element Locators](https://github.com/ikostan/ParaBankSeleniumAutomation/tree/master/page_locators)<br/>
    - [UML diagram](https://github.com/ikostan/ParaBankSeleniumAutomation/tree/master/page_locators/uml)
10. [Page Object Model (POM)](https://github.com/ikostan/ParaBankSeleniumAutomation/tree/master/page_object_models)<br/>
11. [Tests](https://github.com/ikostan/ParaBankSeleniumAutomation/tree/master/tests)<br/>   
    i. [Content Tests](https://github.com/ikostan/ParaBankSeleniumAutomation/tree/master/tests/content_tests)<br/>
    - [Base Cases](https://github.com/ikostan/ParaBankSeleniumAutomation/tree/master/tests/content_tests/base_cases)<br/>
    - [Base Content Tests](https://github.com/ikostan/ParaBankSeleniumAutomation/tree/master/tests/content_tests/base_content_tests)<br/>
    - [Unique Content Tests](https://github.com/ikostan/ParaBankSeleniumAutomation/tree/master/tests/content_tests/base_content_tests)
   
    ii. [End To End Tests](https://github.com/ikostan/ParaBankSeleniumAutomation/tree/master/tests/e2e_tests)<br/>
    - [Log In / Log Out](https://github.com/ikostan/ParaBankSeleniumAutomation/tree/master/tests/e2e_tests/login_logout)<br/>
    - [User Registration](https://github.com/ikostan/ParaBankSeleniumAutomation/tree/master/tests/e2e_tests/user_registration)<br/>
12. [Utils](https://github.com/ikostan/ParaBankSeleniumAutomation/tree/master/utils)<br/>

### [PARA BANK ParaSoft Demo Website](https://parabank.parasoft.com/parabank/index.htm)<br/>
<a id="parabank"></a>ParaBank is a demo site used for demonstration of Parasoft software solutions. 
All materials herein are used solely for simulating a realistic online banking website.<br/>

In other words: ParaBank is not a real bank!<br/>

**Parasoft Resources:**<br/>

- [Demo Website](https://parabank.parasoft.com/parabank/index.htm)<br/>
- [Read more about Para Bank demo website available services](https://parabank.parasoft.com/parabank/services.htm)<br/>
- [The ParaBank demo application from Parasoft](https://github.com/parasoft/parabank)<br/>
- [Parasoft Virtualize Community Edition](https://software.parasoft.com/virtualize/community-edition/)<br/>
- ['SOAtest & Virtualize' System Requirements](https://docs.parasoft.com/display/SOAVIRT9104CTP311/Windows+Standalone+Installation)
- [SOAtest Desktop Installation](https://docs.parasoft.com/display/SOAVIRT9104CTP311/SOAtest+Desktop+Installation)
- [Video: how to install Parasoft 'SOAtest & Virtualize' software](https://fast.wistia.com/embed/iframe/8c9iur4w0r)<br/>
- [How To Videos](https://docs.parasoft.com/display/SOAVIRT9107/Video+Tutorials)
- [SOAtest Videos](https://docs.parasoft.com/display/SOA9106/Video+Tutorials)
- [API Testing How-to Videos](https://www.parasoft.com/tutorial/soatest-how-to-videos)
- [FAQs](https://forums.parasoft.com/discussion/2797?_hsenc=p2ANqtz-9OlPgT9U7LIa94hEEyPsZosYJ1j9Tb1wI5KlUFiy4OXZ67UJHyAuLjwRdNgemdCwziXX9rxmby63LPqTO2DLHIhuMZvg&_hsmi=40626961&utm_content=40626961&utm_medium=email&utm_source=hs_automation)<br/>

### Official Documentation:<br/>
<a id="doc"></a>

- [Selenium Documentation](https://seleniumhq.github.io/selenium/docs/api/py/api.html)<br/>
- [Full Pytest documentation](http://doc.pytest.org/en/latest/contents.html)<br/>
- ['Selenium with Python' official documentation webpage](https://selenium-python.readthedocs.io)<br/>
- [PyCharm - Manage dependencies using requirements.txt](https://www.jetbrains.com/help/pycharm/managing-dependencies.html)<br/>
- [Allure Framework](https://docs.qameta.io/allure/)<br/>
- [Parasoft Documentation and Resources](https://docs.parasoft.com/)

### Dev Environment:<br/>
<a id="dev"></a>

1. [Python 3.7.4](https://www.python.org/downloads/release/python-374/)<br/>
2. [Selenium 3.141.0](https://pypi.org/project/selenium/)<br/>
3. [PyTest 5.0.0](https://pypi.org/project/pytest/)<br/>
4. [Allure Framework 2.12.1](http://allure.qatools.ru/)<br/>
5. [Win 10 (64 bit)](https://www.microsoft.com/en-ca/software-download/windows10)<br/>
6. [PyCharm 2019.2 (Community Edition)](https://www.jetbrains.com/pycharm/download/#section=windows)<br/>
7. [GitHub Desktop 2.1.0](https://desktop.github.com/)<br/>
8. [GIT 2.22.0.windows.1](https://git-scm.com/download/win)<br/>
9. [Java SE 8](https://www.oracle.com/technetwork/java/javase/overview/index.html)
10. [Scoop](https://scoop.sh/)

### Python Packages:<br/>
Full list of dependencies see [here.](https://github.com/ikostan/ParaBankSeleniumAutomation/blob/master/requirements.txt)

### Nice to have tools:
1. [Fiddler](https://www.telerik.com/fiddler)
2. [Kite](https://kite.com/)
3. [Ragnorex: Smart Selector Generator](https://www.ranorex.com/selocity/browser-extension)
4. [Pynsource](https://www.pynsource.com/index.html)

**Note:** In order to instantiate webdriver I use Driver class of my own. For more info please look [here](https://github.com/ikostan/ParaBankSeleniumAutomation/tree/master/utils).<br/>

### Supported/tested browsers:
- Chrome: v75 (64 bit)
- Firefox: v68 (64  bit)
- Edge: v17 and above

### Tech Issues and Problem Solving:<br/>
<a id="tech_issues"></a>

<details>
  <summary><b>Changing the project interpreter in the PyCharm project settings</b></summary>

<br/>1. In the **Settings/Preferences dialog** (Ctrl+Alt+S), select **Project <project name> | Project Interpreter**.<br/>
2. Expand the list of the available interpreters and click the **Show All** link.<br/>
3. Select the target interpreter. When PyCharm stops supporting any of the outdated Python versions, the corresponding project interpreter is marked as unsupported.<br/>
4. The Python interpreter name specified in the **Name** field, becomes visible in the list of available interpreters. Click **OK** to apply the changes.<br/>

For more info please check [here](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html)<br/>

</details>


<details>
  <summary><b>PyCharm - Choosing Your Testing Framework</b></summary>
 
<br/>1. Open the Settings/Preferences dialog, and under the node Tools, click the page **Python Integrated Tools**.<br/>
2. On this page, click the **Default Test Runner** field.<br/>
3. Choose the desired test runner:<br/>

<br/>   
<div align="center"> 
<img width="60%" height="60%" src="https://github.com/ikostan/SELENIUM_WEBDRIVER_WORKING_WITH_ELEMENTS/blob/master/testing_selenium_capabilities/img/py_choosing_test_runner.png" hspace="20">
</div>
<br/>

For more info please see [Enable Pytest for you project](https://www.jetbrains.com/help/pycharm/pytest.html)
</details>


<details>
  <summary><b>Setting up Python3 virtual environment on Windows machine</b></summary>
<br/>

1. open CMD<br/>
2. navigate to project directory, for example:<br/> 

```bash
cd C:\Users\superadmin\Desktop\Python\CodinGame
```

3. run following command:<br/> 

```bash 
pip install virtualenv
```

4. run following command:<br/> 

```bash 
virtualenv venv --python=python
```
    
</details>


<details>
  <summary><b>Auto generate requirements.txt</b></summary>

<br/>Any application typically has a set of dependencies that are required for that application to work. The requirements file is a way to specify and install specific set of package dependencies at once.<br/>
Use pip’s freeze command to generate a requirements.txt file for your project:<br/>

   ```python
    pip freeze > requirements.txt
```

If you save this in requirements.txt, you can follow this guide: [PyCharm - Manage dependencies using requirements.txt](https://www.jetbrains.com/help/pycharm/managing-dependencies.html), or you can:<br/>
   
   ```python
    pip install -r requirements.txt
```   
Source: https://www.idiotinside.com/2015/05/10/python-auto-generate-requirements-txt/<br/>
</details>


<details>
  <summary><b>How to fix in case .gitignore is ignored by Git</b></summary>

<br/>Even if you haven't tracked the files so far, Git seems to be able to "know" about them even after you add them to .gitignore.<br/> 

**NOTE:**<br/>
    - First commit your current changes, or you will lose them.<br/> 
    - Then run the following commands from the top folder of your Git repository:<br/> 
    
   ```bash 
    git rm -r --cached .
    git add .
    git commit -m "fixed untracked files"
   ```
    
</details>


<details>
  <summary><b>Common Selenium errors</b></summary>

<br/>- **[How to fix common Selenium errors?](https://www.ultimateqa.com/common-selenium-webdriver-errors-fix/)**<br/>

</details>


<details>
  <summary><b>Microsoft webdriver for edge 18 and above</b></summary>

<br/>MS made WebDriver a Windows Feature on Demand (FoD), which ensures that it’s always up to date automatically, and enables some new ways to get Microsoft WebDriver.<br/>
    
The simplest way to get started is simply to enable Developer Mode. Simply open the Settings app and go to “Update & Security,” “For developers,” and select “Developer Mode.” The appropriate version of WebDriver will be automatically installed.<br/>
    
You can also install a standalone version of WebDriver in one of two ways:<br/>
    * Search “Manage optional features” from Start, then select “Add a Feature,” “WebDriver.”<br/>
    * Install via DISM by running the following command in an elevated command prompt:
    <br/>```DISM.exe /Online /Add-Capability /CapabilityName:Microsoft.WebDriver~~~~0.0.1.0```<br/>
    
This also means that we will no longer be providing standalone downloads for Microsoft WebDriver going forward<br/>
Source: https://blogs.windows.com/msedgedev/2018/06/14/webdriver-w3c-recommendation-feature-on-demand/#Rg8g2hRfjBQQVRXy.97

</details>


<details>
  <summary><b>Test are failed due to slow performance of WebDriver</b></summary>
  
<br/>Explicit wait is used to specify wait condition for a particular element.<br/> 
Here we define to wait for a certain condition to occur before proceeding further in the code.

   ```python
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec
    
    # Wait for element to appear:
    wait = WebDriverWait(self.driver, 10)
    wait.until(ec.title_is(self.new_window_name))
```

</details>


<details>
  <summary><b>How to Get Selenium to Wait for Page Load After a Click</b></summary>
  
<br/>It turns out Selenium has a built-in condition called staleness_of, as well as its own wait-for implementation. 
Use them, alongside the @contextmanager decorator and the magical-but-slightly-scary yield keyword, and you get:

   ```python
    from contextlib import contextmanager
    from selenium.webdriver.support.ui import WebDriverWait 
    from selenium.webdriver.support.expected_conditions import staleness_of
    
    class MySeleniumTest(SomeFunctionalTestClass): 
      # assumes self.browser is a selenium webdriver
    
      @contextmanager
      def wait_for_page_load(self, timeout=30):
        old_page = self.browser.find_element_by_tag_name('html')
        yield
        WebDriverWait(self.browser, timeout).until(
          staleness_of(old_page)
        )
        
      def test_stuff(self):
        # example use
        with self.wait_for_page_load(timeout=10):
          self.browser.find_element_by_link_text('a link')
```
    
**Note** that this solution only works for “non-JavaScript” clicks, i.e., clicks that will cause the browser to load a brand new page, and thus load a brand new HTML body element.
<br/>Source: https://blog.codeship.com/get-selenium-to-wait-for-page-load/

</details>