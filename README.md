[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](http://unlicense.org/)
# Selenium Automation for Para Bank Web App

<div align="center"> 
<img width="50%" height="50%" src="https://github.com/ikostan/ParaBankSeleniumAutomation/blob/master/images/selenium-python-logo.png" hspace="10">
</div>

### ParaSoft Demo Website<br/>
ParaBank is a demo site used for demonstration of Parasoft software solutions. 
All materials herein are used solely for simulating a realistic online banking website.

In other words: ParaBank is not a real bank!

[Demo Website](https://parabank.parasoft.com/parabank/index.htm)<br/>
[Read more about Para Bank demo website available services](https://parabank.parasoft.com/parabank/services.htm)<br/>

### Dev Environment:<br/>
1. Python 3.7<br/>
2. selenium 3.141.0<br/>
3. PyCharm 2019.1.3 (Community Edition)<br/>
4. Win 10 (64 bit)<br/>

[PyCharm - Manage dependencies using requirements.txt](https://www.jetbrains.com/help/pycharm/managing-dependencies.html)<br/>

<br/>**Setting up Python3 virtual environment on Windows machine:**<br/>

1. open CMD
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

<br/>**Changing the project interpreter in the PyCharm project settings:**<br/>
1. In the **Settings/Preferences dialog** (Ctrl+Alt+S), select **Project <project name> | Project Interpreter**.<br/>
2. Expand the list of the available interpreters and click the **Show All** link.<br/>
3. Select the target interpreter. When PyCharm stops supporting any of the outdated Python versions, the corresponding project interpreter is marked as unsupported.<br/>
4. The Python interpreter name specified in the **Name** field, becomes visible in the list of available interpreters. Click **OK** to apply the changes.<br/>

For more info please check [here](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html)<br/>

### Tech Issues and Problem Solving:<br/>

**How to fix in case .gitignore is ignored by Git:**<br/>

Even if you haven't tracked the files so far, Git seems to be able to "know" about them even after you add them to .gitignore.<br/> 

**NOTE:**<br/>
- First commit your current changes, or you will lose them.<br/> 
- Then run the following commands from the top folder of your Git repository:<br/> 
```bash 
git rm -r --cached .
git add .
git commit -m "fixed untracked files"
```
