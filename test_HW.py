import logging
import time
from testpage import OperationsHelper
from send_log import send_email_report

def test_step0(browser):
    logging.info("Test0 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("bobot2040")
    testpage.enter_pass("e37c848bc3")
    testpage.click_login_button()
    testpage.click_about()
    time.sleep(2)
#    assert testpage.get_text() == "About Page"
    header_font_size = testpage.get_header_font_size()
    assert header_font_size == 32, f"Header font size is {header_font_size}, expected 32"


