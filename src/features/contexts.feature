# Created by Mervin at 9/9/2020
Feature: test scenario context
  # Enter feature description here

  Scenario:  Scenario Context
    Given Open Browser
    Then I save label SIvCob as scenario context
    Then I set xpath //input[@name='q'] with Scenario:SIvCob
    And sleep 5 seconds
