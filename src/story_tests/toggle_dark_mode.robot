*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Clear Theme And Go Home
Library   OperatingSystem


*** Keywords ***
Clear Theme And Go Home
    Go To  ${HOME_URL}
    Execute JavaScript  localStorage.removeItem('theme')
    Reload Page


*** Test Cases ***
Dark mode toggle button should exist
    Element Should Be Visible  id:dark-mode-toggle

Clicking dark mode toggle should add dark class
    Click Button  id:dark-mode-toggle
    ${has_dark}=  Execute JavaScript  return document.documentElement.classList.contains('dark')
    Should Be True  ${has_dark}

Dark mode preference should be saved to localStorage
    Click Button  id:dark-mode-toggle
    ${theme}=  Execute JavaScript  return localStorage.getItem('theme')
    Should Be Equal  ${theme}  dark

Clicking dark mode toggle twice should remove dark class
    Click Button  id:dark-mode-toggle
    Click Button  id:dark-mode-toggle
    ${has_light}=  Execute JavaScript  return document.documentElement.classList.contains('light')
    Should Be True  ${has_light}

Light mode preference should be saved to localStorage
    Click Button  id:dark-mode-toggle
    Click Button  id:dark-mode-toggle
    ${theme}=  Execute JavaScript  return localStorage.getItem('theme')
    Should Be Equal  ${theme}  light

Dark mode preference should persist on page reload
    Click Button  id:dark-mode-toggle
    Reload Page
    ${has_dark}=  Execute JavaScript  return document.documentElement.classList.contains('dark')
    Should Be True  ${has_dark}
