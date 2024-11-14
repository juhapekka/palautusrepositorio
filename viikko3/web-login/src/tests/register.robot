*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
  Set Username  juha
  Set Password  juha1234
  Set PasswordConfirmation  juha1234
  Click Button  Register
  Title Should Be  Welcome to Ohtu Application!


Register With Too Short Username And Valid Password
  Set Username  j
  Set Password  juha1234
  Set PasswordConfirmation  juha1234
  Click Button  Register
  Register Should Fail With Message  Username must be at least three characters long

Register With Valid Username And Too Short Password
  Set Username  juha
  Set Password  juha123
  Set PasswordConfirmation  juha123
  Click Button  Register
  Register Should Fail With Message  Password must be at least eight characters long

Register With Valid Username And Invalid Password
  Set Username  juha
  Set Password  juhajuha
  Set PasswordConfirmation  juhajuha
  Click Button  Register
  Register Should Fail With Message  Password must contain at least one non-letter character

Register With Nonmatching Password And Password Confirmation
  Set Username  juha
  Set Password  juha1234
  Set PasswordConfirmation  juhb1234
  Click Button  Register
  Register Should Fail With Message  Passwords do not match

Register With Username That Is Already In Use
  Set Username  kalle
  Set Password  kalle123
  Set PasswordConfirmation  kalle123
  Click Button  Register
  Register Should Fail With Message  User with username kalle already exists

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set PasswordConfirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}
