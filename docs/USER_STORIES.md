# User Stories and Acceptance Criteria

## US-01 User Registration
As a new customer, I want to create an account so that I can use the appointment system.

**Acceptance Criteria**
- Required details can be entered.
- Invalid data is rejected.
- New user data is stored.
- Duplicate accounts are handled.

## US-02 User Login
As a registered user, I want to log in so that I can access my dashboard.

**Acceptance Criteria**
- Valid credentials allow access.
- Invalid credentials show an error.
- User can log out.

## US-03 Provider Search
As a customer, I want to search providers so that I can choose a suitable service.

**Acceptance Criteria**
- Providers are listed.
- Search/filter works.
- Provider details can be opened.

## US-04 Availability
As a provider, I want to manage time slots so that customers can see available appointments.

**Acceptance Criteria**
- Slots can be added.
- Slots can be removed.
- Booked slots become unavailable.

## US-05 Appointment Booking
As a customer, I want to select a provider and time slot so that I can book an appointment.

**Acceptance Criteria**
- Provider can be selected.
- Available slot can be selected.
- Appointment is created.
- Booked slot cannot be double-booked.
- Confirmation is shown.

## US-06 Cancellation
As a customer, I want to cancel an appointment so that I can change my plans.

**Acceptance Criteria**
- Existing appointment can be selected.
- Appointment status changes to Cancelled.
- Slot becomes available again.

## US-07 Rescheduling
As a customer, I want to reschedule an appointment so that I can choose another available time.

**Acceptance Criteria**
- Existing appointment is identified.
- New slot is available.
- Old slot is released.
- New time is stored.

## US-08 Customer Dashboard
As a customer, I want to see my appointments in one place so that I can manage my bookings easily.

**Acceptance Criteria**
- Upcoming appointments are visible.
- Completed and cancelled appointments can be identified.
- Provider and time details are shown.

## US-09 Provider Dashboard
As a provider, I want to view bookings so that I can manage my schedule.

**Acceptance Criteria**
- Upcoming bookings are listed.
- Customer details are shown.
- Status can be updated.

## US-10 Quality Validation
As a project team, we want the booking flow tested so that the released system is reliable.

**Acceptance Criteria**
- Unit tests cover core logic.
- End-to-end booking flow is tested.
- Bugs are tracked and resolved.
- Regression testing is completed.
