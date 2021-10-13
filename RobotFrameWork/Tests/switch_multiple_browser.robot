*** Settings ***
library  SeleniumLibrary

*** Test Cases ***
switch browser
    open browser  https://www.google.com/  gc
    maximize browser window

    open browser  https://www.bing.com/  gc
    maximize browser window

    switch browser  1
    ${title}  get title
    log to console  ${title}

    switch browser  2
    ${title2}  get title
    log to console  ${title2}

    close all browsers


*** Keywords ***
Provided precondition
    Setup system under test