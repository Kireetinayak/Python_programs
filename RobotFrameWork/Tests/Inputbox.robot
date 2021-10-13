*** Settings ***
Library    SeleniumLibrary

*** Variable ***
${Browser}  gc
${URL}  https://demo.nopcommerce.com/
*** Test Cases ***
Inputbox tets
    open browser  ${URL}  ${Browser}
    maximize browser window
    title should be  nopCommerce demo store
    click link  xpath:/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a
    ${Email_textbox}  set variable  id:Email

    element should be visible  ${Email_textbox}
    #element should not be visible  ${Email_textbox}
    element should be enabled  ${Email_textbox}
    #element should not be enable  ${Email_textbox}
    sleep  3s

    input text  ${Email_textbox}  nayak@gmail.com
    sleep  2s
    clear element text  ${Email_textbox}


*** Keywords ***
Provided precondition
    Setup system under test