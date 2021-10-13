*** Settings ***
Library  SeleniumLibrary

*** Variable ***
${browser}  gc
${url}  https://demo.nopcommerce.com/

*** Test Cases ***
Drop down
    open browser  ${url}  ${browser}
    maximize browser window
    set selenium speed  2s

    click link  xpath://*[@id="topcartlink"]/a

    select from list by label  customerCurrency  Euro

    select from list by index  customerCurrency  0

    click link  xpath:/html/body/div[6]/div[2]/ul[1]/li[1]/a
   # click link  Xpath:/html/body/div[6]/div[2]/ul[1]/li[1]/ul/li[1]/a

*** Keywords ***
