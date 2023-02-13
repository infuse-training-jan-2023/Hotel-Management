Feature: Get customer details
    As a customer I should be able to see my details

    Scenario: Get customer details
        When customer wants to see profile
        Then customer should be able to see details
        Then the api status code should be 200
        Then the api response content type should be json