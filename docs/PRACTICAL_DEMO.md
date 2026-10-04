# Practical Demonstration Guide

## Project
**Online Appointment Booking System**

## Goal
Demonstrate how Scrum and Kanban were applied during development using GitHub.

## 1. Start with the Repository
Open the repository README and explain the problem, objective, technology, sprint plan, and Agile practices.

## 2. Show the Kanban Board
Open the GitHub Project named **Online Appointment Booking – Agile Project**.

Explain the workflow:
**Backlog → To Do → In Progress → Code Review → Testing → Done**

Explain that an issue represents a unit of work and its status changes as the work progresses.

## 3. Show the Sprint Backlog
Open the **Sprint Backlog** view.

Show the Sprint field:
- Sprint 1 – Planning & Foundation
- Sprint 2 – Users & Providers
- Sprint 3 – Appointment Booking
- Sprint 4 – Testing & Finalization

Explain that the backlog is divided into small increments that can be delivered and reviewed.

## 4. Show a User Story
Open an issue such as **#11 Implement appointment booking**.

Explain:
- User Story states who needs the feature and why.
- Acceptance Criteria define what must be true before it is considered complete.
- Priority and Sprint help planning.

## 5. Show Development History
Open the merged pull requests:
- PR #21 – Provider search
- PR #22 – Appointment rescheduling
- PR #23 – Test coverage and retrospective
- PR #25 – Continuous integration

Explain the flow:
**Issue → Branch → Code → Pull Request → Review → Merge**

## 6. Show Testing
Open tests/test_app.py and docs/TEST_PLAN.md.

Explain that the project covers:
- unit testing;
- provider search;
- booking;
- duplicate-booking prevention;
- cancellation;
- rescheduling;
- functional and regression-oriented testing.

## 7. Show Continuous Integration
Open .github/workflows/tests.yml.

Explain that GitHub Actions installs the dependencies and runs pytest automatically on pushes to main and on pull requests.

## 8. Demonstrate the Application
Run the Flask application locally and show:
1. Provider list.
2. Search provider/service.
3. Book appointment.
4. Open appointment dashboard.
5. Cancel appointment.
6. Reschedule appointment.

## 9. Viva Explanation
Say:

> We selected an Online Appointment Booking System and followed an Agile approach. Requirements were converted into user stories with acceptance criteria and organized into four sprints. GitHub Projects was used as the Kanban board with Backlog, To Do, In Progress, Code Review, Testing, and Done stages. Development was tracked with Issues, branches, pull requests, testing, and continuous integration. The team can inspect progress frequently and move work based on its current state.

## 10. Important Agile Terms to Mention
**Product Backlog:** complete list of planned work.

**Sprint:** a short development period with a defined goal.

**Sprint Backlog:** work selected for the current sprint.

**User Story:** requirement written from the user's point of view.

**Acceptance Criteria:** conditions used to decide whether a story is complete.

**Kanban:** visual workflow for tracking work.

**WIP Limit:** limit on the amount of work being actively handled.

**Pull Request:** proposed code change sent for review before merging.

**Continuous Integration:** automated validation of changes as code is pushed or proposed.

**Retrospective:** team reflection on what went well, what could improve, and the next actions.
