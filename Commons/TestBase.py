class TestBase():

    #TO-DO
    # Wait until elemnt is enabled
    def wait_for_element_to_be_clickable(locator, timeout=10):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.element_to_be_enabled(locator)
            )
            return element
        except Exception as e:
            print(f"Error waitng for the element: {e}")
            return None