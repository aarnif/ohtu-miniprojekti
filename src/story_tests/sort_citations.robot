*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Citations
Library   OperatingSystem


*** Test Cases ***
Sort by title should return citations in alphabetical order
    Add citation  book  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999  10.1145/2380552.2380613  refactoring  design
    Add citation  book  Robert C. Martin  Clean Code: A Handbook of Agile Software Craftsmanship  Prentice Hall  2008  10.1145/1869452.1869473  practices  clean-code
    Add citation  book  Eric Evans  Domain-Driven Design: Tackling Complexity in the Heart of Software  Addison-Wesley  2003  10.1145/1234567.1234568  design  architecture
    Select From List By Value  sort  title
    Check page contains citation  Robert C. Martin  Clean Code: A Handbook of Agile Software Craftsmanship  Prentice Hall  2008
    Check page contains citation  Eric Evans  Domain-Driven Design: Tackling Complexity in the Heart of Software  Addison-Wesley  2003
    Check page contains citation  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999

Sort by author should return citations sorted by author
    Add citation  book  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999  10.1145/2380552.2380613  refactoring  design
    Add citation  book  Robert C. Martin  Clean Code: A Handbook of Agile Software Craftsmanship  Prentice Hall  2008  10.1145/1869452.1869473  practices  clean-code
    Add citation  book  Eric Evans  Domain-Driven Design: Tackling Complexity in the Heart of Software  Addison-Wesley  2003  10.1145/1234567.1234568  design  architecture
    Select From List By Value  sort  author
    Check page contains citation  Eric Evans  Domain-Driven Design: Tackling Complexity in the Heart of Software  Addison-Wesley  2003
    Check page contains citation  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999
    Check page contains citation  Robert C. Martin  Clean Code: A Handbook of Agile Software Craftsmanship  Prentice Hall  2008

Sort by publisher should return citations sorted by publisher
    Add citation  book  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999  10.1145/2380552.2380613  refactoring  design
    Add citation  book  Robert C. Martin  Clean Code: A Handbook of Agile Software Craftsmanship  Prentice Hall  2008  10.1145/1869452.1869473  practices  clean-code
    Add citation  book  Eric Evans  Domain-Driven Design: Tackling Complexity in the Heart of Software  Addison-Wesley  2003  10.1145/1234567.1234568  design  architecture
    Select From List By Value  sort  publisher
    Check page contains citation  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999
    Check page contains citation  Eric Evans  Domain-Driven Design: Tackling Complexity in the Heart of Software  Addison-Wesley  2003
    Check page contains citation  Robert C. Martin  Clean Code: A Handbook of Agile Software Craftsmanship  Prentice Hall  2008

Sort by year should return citations sorted by year
    Add citation  book  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999  10.1145/2380552.2380613  refactoring  design
    Add citation  book  Robert C. Martin  Clean Code: A Handbook of Agile Software Craftsmanship  Prentice Hall  2008  10.1145/1869452.1869473  practices  clean-code
    Add citation  book  Eric Evans  Domain-Driven Design: Tackling Complexity in the Heart of Software  Addison-Wesley  2003  10.1145/1234567.1234568  design  architecture
    Select From List By Value  sort  year
    Check page contains citation  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999
    Check page contains citation  Eric Evans  Domain-Driven Design: Tackling Complexity in the Heart of Software  Addison-Wesley  2003
    Check page contains citation  Robert C. Martin  Clean Code: A Handbook of Agile Software Craftsmanship  Prentice Hall  2008
