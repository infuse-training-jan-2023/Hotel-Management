Feature: Customer Review
    As a customer i can give review to a hotel room

    Scenario: Customer Review
        When Customer gives a review
        Then Customer review should be saved to database
        Then Api status code should be 201