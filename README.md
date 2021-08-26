<h1 align="center">openlxp-test-automation-scripts ReadMe</h1>


## Features
This following scripts will work together to test various features of the Enterprise Course Catalog
## Prerequisite
- Python
- Selenium
- HTML

## Built with
- Python 3.9
- Selenium 3.141.0

## Directory Structure
> [`pageobjects`](https://github.com/OpenLXP/openlxp-test-automation-scripts/tree/main/pageobjects "pageobjects folder"): The python scripts found in this folder use Selenium to search and identify the presences of various HTML elements via their XPATH on the webpage which will be tested. These elements will later be referenced in other test scripts which will perform various actions with the HTML elements.

> [`reports`](https://github.com/OpenLXP/openlxp-test-automation-scripts/tree/main/reports "reports folder"): Upon execution of test cases, HTMLTestRunner will generate HTML reports into this folder. These reports are automatically generated after each execution of the test case. These reports can be customized via various parameters found within the HTMLTestRunner python package. Output is in the form of HTML and can be viewed in a web browser.
- testcases
- values
