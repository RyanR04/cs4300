Feature: Movie Listing

Scenario: User view available movies
    Given a movie exists
    When the user opens the movie listings page
    Then the movie title should appear 

