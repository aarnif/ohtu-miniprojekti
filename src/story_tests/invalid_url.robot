*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Citations

*** Test Cases ***
Invalid URL shows 404 page
    Go To  ${HOME_URL}/invalid-page
    Page Should Contain  Page Not Found
    Page Should Contain  The page you are looking for does not exist.

Invalid URL has 404 status code
    Go To  ${HOME_URL}/this-does-not-exist
    Page Should Contain  Page Not Found

Invalid citation ID shows 404 page
    Go To  ${HOME_URL}/citations/99999
    Page Should Contain  Citation Not Found

Invalid citation ID with non-numeric value shows 404 page
    Go To  ${HOME_URL}/citations/invalid-id
    Page Should Contain  Citation Not Found

Can navigate back to home from 404 page
    Go To  ${HOME_URL}/invalid-url
    Page Should Contain  Page Not Found
    Click Link  Back to Home
    Title Should Be  Citations app
    
Can navigate back to home from invalid citation page
    Go To  ${HOME_URL}/citations/99999
    Page Should Contain  Citation Not Found
    Click Link  Back to Home
    Title Should Be  Citations app
