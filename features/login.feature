Feature: Book Store
    As a online user,
    I want to login,
    So that I can read online

Background: I navigate to the website

Scenario: login as user
    Given the Homepage is login
    When the user goes to login page and enter username "alex1" and password "Apple123*"
    And the user clicks on login button
    Then the user is logged in successfully


