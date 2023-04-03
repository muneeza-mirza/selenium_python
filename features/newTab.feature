Feature: Book Store
    As a online user,
    I want to open new tab,
    So that I can search things separately

Background: I navigate to the website

Scenario: open new tab as user
    Given the website is open
    When the user clicks on new tab
    Then the user should see a new tab open

Scenario: open new window as user
    Given the website is open
    When the user clicks on new window
    Then the user should see a new window open

Scenario: open new window message as user
    Given the website is open
    When the user clicks on new window message
    Then the user should see a pop up message