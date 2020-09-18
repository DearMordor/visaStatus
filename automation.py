from selenium import webdriver
from bs4 import BeautifulSoup
import re

import time
from selenium.webdriver.common.keys import Keys



print("Write your visa code in format:\n 12345/XX-YYYY\nWhere XX it is your application type "
      "\n(Available typos: DP,DV,PP,ZK,ZM,ST,TP,CD,VP,MK\n YYYY - Application's year )")
application = str(input())

if re.match(r"\d{5}\/[dp dv pp zk zm st tp cd vp mk DP DV PP ZK ZM ST TP CD VP MK]{2}\-\d{4}", application):

    application_parts = re.split(r"[\/-]", application)

    driver = webdriver.Chrome("C:/visa/chromedriver.exe")
    driver.get("https://frs.gov.cz/cs/ioff/application-status")

    applicationNumber = driver.find_element_by_id("edit-ioff-application-number")
    applicationNumber.send_keys(application_parts[0])

    type_of_apply = driver.find_element_by_id("edit-ioff-application-code")
    type_of_apply.send_keys(application_parts[1])

    year = driver.find_element_by_id("edit-ioff-application-year")
    year.send_keys(application_parts[2])

    button = driver.find_element_by_id("edit-submit-button")
    time.sleep(30)
    button.click()

else:
    print("Invalid application\nTry again in accordance with format")
