from behave import given, when, then
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.googlemapshomepage import GoogleMapsHomePage
import time


@given('Open maps app')
def step_impl(context):
    pass
  
@when('Search Field is visible')
def step_impl(context):
    assert context.maps_page.is_SearchField_Displayed()

@when('I search for a destination')
def step_impl(context):
    context.maps_page.search_For_A_Destination()

@then('Destination is located in the map')
def step_impl(context):
    assert context.maps_page.is_map_displayed()