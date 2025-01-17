Feature: Home Maps 
  Scenario: Open Maps and execute a new destination search
    Given Open maps app
    When Search Field is visible
    When I search for a destination
    Then Destination is located in the map

  
    
    
    
    