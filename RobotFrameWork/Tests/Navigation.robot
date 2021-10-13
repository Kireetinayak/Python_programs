*** Settings ***
library  SeleniumLibrary

*** Test Cases ***
Navigation
    open browser  https://www.google.com/  gc
    maximize browser window

    ${loc}  get location
    log to console  ${loc}

    go to  https://www.bing.com/
    ${loc1}  get location
    log to console  ${loc1}

    go back
    ${loc2}  get location
    log to console  ${loc2}

    close all browsers
*** Keywords ***
Provided precondition
    Setup system under test