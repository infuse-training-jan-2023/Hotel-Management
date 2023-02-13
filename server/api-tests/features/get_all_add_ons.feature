
Feature: Get all add ons
  As a user I want to see all the add ons available

  Scenario: Get all add ons
    When I want to see add ons
    Then I should be able to see all the add ons
    Then the api status code should be 200
    Then the api response content type should be json