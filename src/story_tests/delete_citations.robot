*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Citations
Library   OperatingSystem

*** Test Cases ***
Citation can be deleted
    Add citation  book  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999  10.1145/2380552.2380613  refactoring  design
    Check page contains citation  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999
    Go To  ${HOME_URL}
    Click Link  citation-item-link
    Click Element  delete
    Click Button  confirm
    Page Should Contain  No citations.

Citation deletion can be cancelled
    Add citation  book  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999  10.1145/2380552.2380613  refactoring  design
    Check page contains citation  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999
    Go To  ${HOME_URL}
    Click Link  citation-item-link
    Click Element  delete
    Click Button  cancel
    Check page contains citation  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999

Citation deletion shows confirmation box
    Add citation  book  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999  10.1145/2380552.2380613  refactoring  design
    Check page contains citation  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999
    Go To  ${HOME_URL}
    Click Link  citation-item-link
    Click Element  delete
    Page Should Contain  Delete Citation?

Deletion confirmation notification can be dismissed
    Add citation  book  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999  10.1145/2380552.2380613  refactoring  design
    Check page contains citation  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999
    Go To  ${HOME_URL}
    Click Link  citation-item-link
    Click Element  delete
    Click Button  confirm
    Page should contain  Citation deleted successfully!
    Dismiss notification

Deletion confirmation notification is not visible after dismissing
    Add citation  book  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999  10.1145/2380552.2380613  refactoring  design
    Check page contains citation  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999
    Go To  ${HOME_URL}
    Click Link  citation-item-link
    Click Element  delete
    Click Button  confirm
    Page should contain  Citation deleted successfully!
    Dismiss notification
    Sleep  1s
    Element Should Not Be Visible  close-notification-icon
    Go To  ${HOME_URL}
    Element Should Not Be Visible  close-notification-icon