
Feature: Get discount for a customer
  As a customer I can get discount based on past order

  Scenario: Get discount for an existing customer
    When i am an existing customer on booking page 
    Then i should get discount based on number of past orders
    Then the api status code should be 200
    Then the api response content type should be json
  
  Scenario: Get discount for a new customer
    When i am a new customer on booking page
    Then i should not get discount 
    Then the api status code should be 200
    Then the api response content type should be json