*** Settings ***
Library  SeleniumLibrary

*** Variable ***
${browser}  gc
${url}  http://demowebshop.tricentis.com/

*** Test Cases ***
Speed test
    open browser  ${url}  ${browser}
    maximize browser window
    capture element screenshot  xpath:/html/body/div[4]/div[1]/div[1]/div[1]/a/img   log.png
    capture page screenshot   page.png

*** Keywords ***
Provided precondition
    Setup system under test