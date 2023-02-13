
Feature: Search for rooms
  As a customer I want to search for rooms available

  Scenario: Search for rooms
    When i try to search for room  
    Then i should get the rooms available based on filters
    Then the api status code should be 201
    Then the api response content type should be json