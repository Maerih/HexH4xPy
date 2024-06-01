# Author: Onyonka Maeri
# Date: 2024-05-30
# WARNING:
# This script is intended for educational purposes only.
# Unauthorized use of this script on systems you do not own or
# have explicit permission to test is illegal and unethical.
# Use responsibly and within the bounds of all applicable laws.


# Need browser driver file to drive web browser
# acts as an interface between selenium and browser
# create a settings.py for it ie for chrome
#     SELENIUM_DRIVER_NAME = 'chrome'
#     SELENIUM_DRIVER_EXECUTABLE_PATH = <location of driver>
#     SELENIUM_DRIVER_ARGUMENTS = []
#     SELENIUM_DRIVER_ARGUMENTS = ['--headless']

import scrapy
from scrapy_selenium import SaleniumRequest
import time

def wait(driver):
    time.sleep(1)
    return True

class PythonScraperSpider(scrapy_spder):
     
