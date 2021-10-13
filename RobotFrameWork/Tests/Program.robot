*** Setting ***
Documentation
Library  SeleniumLibrary
*** Variable ***
${URl}  https://demo.nopcommerce.com/
${browser}  gc
*** Test Cases ***
Testcases1
  open browser   ${URl}  ${browser}
  Login page
  Close Browser
*** Keywords ***
Login page
    click link  xpath:/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a
    input text  id:Email   kireetinayak@gmail.com
    input text  id:Password   kireeti
    click button  xpath:/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]/div[2]/form/div[3]/input
    sleep  3s
