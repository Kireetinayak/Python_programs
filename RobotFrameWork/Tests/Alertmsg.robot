*** Settings ***
Library  SeleniumLibrary

*** Variable ***
${browser}  gc
${url}  http://demowebshop.tricentis.com/

*** Test Cases ***
Testing Alert msg
    open browser  ${url}  ${browser}
    maximize browser window
    set selenium implicit wait  10s
    click element  xpath:/html/body/div[4]/div[1]/div[1]/div[3]/form/input[2]

    # Alert Msg #click OK
    #handle alert  accept
    #handle alert  dissmis # click cancle
    #handle alert  leave

    #Alert text validation
    ${text}  alert should be present  Please enter some search keyword
    log to console  ${text}
    #alert should not be present   keyword
    close browser



*** Keywords ***
