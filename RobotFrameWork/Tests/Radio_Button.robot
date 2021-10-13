*** Settings ***
Library  SeleniumLibrary

*** Variable ***
${browser}  gc
${url}  https://demo.nopcommerce.com/

*** Test Cases ***
Testing Radiobutton and check box
    open browser  ${url}  ${browser}
    maximize browser window
    set selenium speed  2s
    click link  xpath:/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a

    #select radio button
    select radio button     Gender  M

    #Select  and unselect check box
    unselect checkbox  Newsletter
    select checkbox  Newsletter

    close browser

*** Keywords ***
