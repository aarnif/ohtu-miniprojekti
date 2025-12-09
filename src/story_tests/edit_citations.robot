*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Citations
Library   OperatingSystem

*** Test Cases ***
Citation can be edited
    Add citation  book  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999  10.1145/2380552.2380613
    Check page contains citation  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999
    Go To  ${HOME_URL}
    Click Link  citation-item-link
    Click Element  update
    Input Text  title  Edited title
    Click Button  edit_citation_button
    Check page contains citation  Martin Fowler  Edited title  Addison-Wesley  1999
