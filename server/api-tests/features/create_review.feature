Feature: User Review
    As a user i can give review to a hotel room

    Scenario: User Review
        When User gives a review
        Then User review should be saved to database
        Then api api status code should be 201