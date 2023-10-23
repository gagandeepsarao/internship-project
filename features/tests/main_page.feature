# Created by gagan at 10/12/2023
Feature: Test scenario for website
  # Enter feature description here

  Scenario: The user clicks on “Connect Agency” button and sees the right number of UI elements
      Given Open the main page
      When Log in to the page
      And Click on “Connect the Company”
      Then Switch to the new tab
      Then Verify there are 4 steps in the description
      And Verify “Subscription plans” button is clickable