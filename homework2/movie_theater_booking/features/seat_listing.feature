Feature: Seat Listing

Scenario: User view available seats
    Given a movie seat exists
    When the user opens the booking page
    Then all seats should appear
