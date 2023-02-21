Feature: cancel booking
    As a user i can cancel room booking

    Scenario: cancel booking
        When I cancel booking
        Then I should get confirmation message
        Then The api status code should be 200
        Then The api Response type should be json