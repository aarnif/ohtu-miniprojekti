*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Citations
Library   OperatingSystem

*** Test Cases ***
Citation can be edited
    Add citation  book  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999  10.1145/2380552.2380613  refactoring  design
    Check page contains citation  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999
    Go To  ${HOME_URL}
    Click Link  citation-item-link
    Click Element  edit
    Input Text  title  Edited title
    Click Button  edit_citation_button
    Check page contains citation  Martin Fowler  Edited title  Addison-Wesley  1999

Citation editing can be cancelled
    Add citation  book  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999  10.1145/2380552.2380613  refactoring  design
    Check page contains citation  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999
    Go To  ${HOME_URL}
    Click Link  citation-item-link
    Click Element  edit
    Input Text  title  Edited title
    Click Button  Cancel
    Check page contains citation  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999

Citation editing shows confirmation notification
    Add citation  book  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999  10.1145/2380552.2380613  refactoring  design
    Check page contains citation  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999
    Go To  ${HOME_URL}
    Click Link  citation-item-link
    Click Element  edit
    Input Text  title  Edited title
    Click Button  edit_citation_button
    Check page contains citation  Martin Fowler  Edited title  Addison-Wesley  1999
    Page should contain  Citation edited successfully!

Confirmation notification can be dismissed
    Add citation  book  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999  10.1145/2380552.2380613  refactoring  design
    Check page contains citation  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999
    Go To  ${HOME_URL}
    Click Link  citation-item-link
    Click Element  edit
    Input Text  title  Edited title
    Click Button  edit_citation_button
    Check page contains citation  Martin Fowler  Edited title  Addison-Wesley  1999
    Page should contain  Citation edited successfully!
    Dismiss notification

Confirmation notification is not visible after dismissing
    Add citation  book  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999  10.1145/2380552.2380613  refactoring  design
    Check page contains citation  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999
    Go To  ${HOME_URL}
    Click Link  citation-item-link
    Click Element  edit
    Input Text  title  Edited title
    Click Button  edit_citation_button
    Check page contains citation  Martin Fowler  Edited title  Addison-Wesley  1999
    Page should contain  Citation edited successfully!
    Dismiss notification
    Sleep  1s
    Element Should Not Be Visible  close-notification-icon
    Go To  ${HOME_URL}
    Element Should Not Be Visible  close-notification-icon