*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}     localhost:5001
${DELAY}      0.5 seconds
${HOME_URL}   http://${SERVER}
${RESET_URL}  http://${SERVER}/reset_db
${BROWSER}    chrome
${HEADLESS}   false

*** Keywords ***
Open And Configure Browser
    IF  $BROWSER == 'chrome'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
        Call Method  ${options}  add_argument  --incognito
    ELSE IF  $BROWSER == 'firefox'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].FirefoxOptions()  sys
        Call Method  ${options}  add_argument  --private-window
    END
    IF  $HEADLESS == 'true'
        Set Selenium Speed  0.01 seconds
        Call Method  ${options}  add_argument  --headless
    ELSE
        Set Selenium Speed  ${DELAY}
    END
    Open Browser  browser=${BROWSER}  options=${options}

Reset Citations
    Go To  ${RESET_URL}

Add Citation
    [Arguments]  ${citation_type}  ${author}  ${title}  ${publisher}  ${year}  ${doi}  @{tags}
    Go To  ${HOME_URL}
    Click Link  New citation
    Select From List By Value  citation_type  ${citation_type}
    Input Text  author  ${author}
    Input Text  title  ${title}
    Input Text  publisher  ${publisher}
    Input Text  year  ${year}
    Input Text  doi  ${doi}
    FOR  ${tag}  IN  @{tags}
        Input Text  new-tag  ${tag}
        Click Button  Add Tag
    END
    Click Button  add_citation_button

Check page contains citation
    [Arguments]  ${author}  ${title}  ${publisher}  ${year}  @{tags}
    Page Should Contain  ${author}
    Page Should Contain  ${title}
    Page Should Contain  ${publisher}
    Page Should Contain  ${year}
    FOR  ${tag}  IN  @{tags}
        Page Should Contain  ${tag}
    END

Dismiss notification
    Wait Until Element Is Visible  id=close-notification-icon
    Click Element  id=close-notification-icon