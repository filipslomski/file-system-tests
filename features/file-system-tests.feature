@file-system
Feature: I want to test to file system features
  Let's assume that 1000 is a max number of items in a directory/tree
  Let's assume I'm testing file system mapped to a system that exposes an API (it would be similar in case of commands)

  Scenario: Test the AddFile function
    Given I have no directories and no files in my root directory
     When I call the AddFile function
     Then I should see 1 file and 0 directories
     When I call the AddFile function 999 times
     Then I should see 1000 files and 0 directories
     When I call the AddFile function
     Then I should see a warning for AddFile
      And I should see 1000 files and 0 directories

  Scenario: Test the AddDirectory function
    Given I have no directories and no files in my root directory
     When I call the AddDirectory function
     Then I should see 0 files and 1 directory
     When I call the AddDirectory function 999 times
     Then I should see 0 files and 1000 directories
     When I call the AddDirectory function
     Then I should see a warning for AddDirectory
      And I should see 0 files and 1000 directories

  Scenario: Test the ChangeDir function
    Given I have 2 directories and 2 files in my root directory
     When I call the ChangeDir function for a random directory
     Then I should be in the chosen directory
     When I call the ChangeDir function for a non-existing directory
     Then I should see a warning for ChangeDir
      And I should be in the chosen directory

  Scenario: Test the DirUp function
    Given I have 2 directories and 2 files in my root directory
     When I go inside the directory
      And I call the DirUp function
     Then I should be in the root directory
     When I call the DirUp function
     Then I should see a warning for DirUp
      And I should be in the root directory

  Scenario: Test the Pwd function
    Given I have 2 directories and 0 files in my root directory
     When I call the Pwd function
     Then I should see the correct root path
     When I go inside the directory
      And I call the Pwd function
     Then I should see the correct directory path

  Scenario: Test function's speed
    Given I have a correct file system prepared
     When I call the AddFile 100 times
     Then I should see a satisfying speed result for AddFile
     When I call the AddDir 100 times
     Then I should see a satisfying speed result for AddDir
     When I call the ChangeDir 100 times
     Then I should see a satisfying speed result for ChangeDir
     When I call the DirUp 100 times
     Then I should see a satisfying speed result for DirUp
     When I call the Pwd 100 times
     Then I should see a satisfying speed result for Pwd


  Scenario: More complex integration case
    #TBA
