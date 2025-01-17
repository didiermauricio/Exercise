from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class GoogleMapsHomePage:
    def __init__(self, driver):
        self.driver = driver

    # Google Maps - locators
    search_box_locator = (MobileBy.ID, "com.google.android.apps.maps:id/search_omnibox_text_box")
    search_box_locator_editable = (MobileBy.ID, "com.google.android.apps.maps:id/search_omnibox_edit_text")
    search_button_locator = (MobileBy.ID, "com.google.android.apps.maps:id/search_omnibox_search_button")
    street_thumbnail_locator = (MobileBy.ID, "com.google.android.apps.maps:id/street_view_thumbnail")

    

    def click_search_button(self):
        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.search_button_locator)
        )
        search_button.click()

    def is_map_displayed(self):
        try:
            map_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.street_thumbnail_locator)
            )
            return map_element.is_displayed()
        except:
            return False


    def is_SearchField_Displayed(self):
        try:
            searchField = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.search_box_locator)
            )
            return searchField.is_displayed()
        except:
            return False       

    def search_For_A_Destination(self):
        search_box = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.search_box_locator)
        )
        search_box.click()
        search_button_editable = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.search_box_locator_editable)
        )
        search_button_editable.send_keys("spain")
        self.driver.press_keycode(66)
