Feature: Booking Listing

Scenario: User view Booking History
    Given a booking was made
    When the user opens the booking history page
    Then the booking will appear
