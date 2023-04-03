Feature: Book Store
    As a online user,
    I want to search book,
    So that I can read online

Background: I navigate to the website

Scenario: Search a valid book
    Given the Homepage is displayed
    When the user enters valid name of the book "Git"
    Then the user should see that book

Scenario: open book
    Given the Homepage is displayed
    When the user enters name of the book "Git" and clicks on it
    Then the user should see book details