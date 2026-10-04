# Test Plan

## Test Levels
1. Unit Testing – individual functions and modules.
2. Functional Testing – feature behavior against requirements.
3. Integration Testing – interaction between authentication, availability and booking.
4. Regression Testing – verify old functionality after changes.

## Core Test Cases
| ID | Test | Expected Result |
|---|---|---|
| T01 | Register with valid data | Account created |
| T02 | Login with valid credentials | Dashboard opens |
| T03 | Login with invalid credentials | Error shown |
| T04 | Search provider | Matching providers shown |
| T05 | View slot availability | Available slots shown |
| T06 | Book available slot | Appointment created |
| T07 | Book already reserved slot | Booking rejected |
| T08 | Cancel appointment | Status becomes Cancelled and slot is released |
| T09 | Reschedule appointment | New slot stored and old slot released |
| T10 | Provider views booking | Booking visible in provider dashboard |

## Exit Criteria
- Critical test cases pass.
- No known critical defects remain.
- Regression testing is completed.
- Documentation reflects the released behavior.
