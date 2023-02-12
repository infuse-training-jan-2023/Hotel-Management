Feature: get booking records
    As a user i can get booking records

    Scenario: get booking records
        When I get booking records
        Then I should get list of records
        Then The api status code should be 200
        Then The api Response type should be json