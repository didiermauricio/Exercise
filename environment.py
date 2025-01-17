from appium import webdriver
from pages.googlemapshomepage import GoogleMapsHomePage
import time

def before_all(context):
    # create a new instance of driver per each scenario
    desired_caps = {
    "platformName": "Android",
    "platformVersion": "15",  
    "deviceName": "ANDROID_EMULATOR",  
    "automationName": "UiAutomator2",
    "appPackage": "com.google.android.apps.maps",  
    "appActivity": "com.google.android.maps.MapsActivity", 
    "noReset": True,
    "unicodeKeyboard": True,
    "resetKeyboard": True
}
    context.driver = webdriver.Remote(command_executor='http://localhost:4723',
        desired_capabilities=desired_caps)
    context.maps_page = GoogleMapsHomePage(context.driver)

    time.sleep(15)  # wait some sec in order to have the app loaded / pending configure a implicit wait

def after_all(context):
    if context.driver:
        context.driver.terminate_app("com.google.android.apps.maps") # terminate the app after each scenario