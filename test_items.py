import time
from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_card_button_is_displayed(browser):

    browser.get(link)
    time.sleep(30)
    try:
      browser.find_element_by_css_selector("button.btn-add-to-basket")
      found = True
    except NoSuchElementException:
      found = False

    assert found == True, "'Add to cart' button is not displayed on the page"


    
