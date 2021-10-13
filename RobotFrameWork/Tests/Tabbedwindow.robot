*** Settings ***
Library  SeleniumLibrary

*** Variable ***
${browser}  gc
${url}  http://demowebshop.tricentis.com/

*** Test Cases ***
Tabbedwindow
    open browser  ${url}  ${browser}
    maximize browser window
    set selenium implicit wait  10s
    click link  Facebook

    select window  title=NopCommerce - Home | Facebook
    click link  Reviews

    close all browsers