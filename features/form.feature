Feature: Book Store
    As a online user,
    I want to submit form,
    So that I can read online

Background: I navigate to the website

Scenario: submit form
    Given the Homepage is form
    When the user goes to page and enter name "alex", email "alex@gmail.com", current address "xyz street" and permanent address "xyz street"
    And the user clicks on submit button
    Then the user can see details below
