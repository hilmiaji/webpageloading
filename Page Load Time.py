from selenium import webdriver
import requests
import time
import os

#Deklarasi Webdriver Chrome
driver = webdriver.Chrome(r"C:\Users\moder\Downloads\chromedriver.exe")
url2 = "http://www.youtube.com"

#Fungsi pageloadtime
def page_load_time(driver, url2):
    driver.get(url2)

    # Use the browser Navigation Timing API to get some numbers:
    # https://developer.mozilla.org/en-US/docs/Web/API/Navigation_timing_API
    #navigation_start2 = driver.execute_script(
       # "return window.performance.timing.navigationStart")
    #dom_complete2 = driver.execute_script(
        #"return window.performance.timing.domComplete")
    navigation_start = driver.execute_script(
        "return performance.timing.navigationStart")
    load_eventend = driver.execute_script(
        "return performance.timing.loadEventEnd")
    #performance_data = driver.execute_script("return window.performance.getEntries();")
    total_time = load_eventend - navigation_start

    print(f"Time {total_time}ms")
    return total_time

def push_data_to_prtg(value_i) :
    try :
        url = f"http://prtg3.psn.co.id:5050/C28A3955-ADE4-49FF-AF89-19BAA6045155?value={value_i}"

        req = requests.get(url, timeout=15)

        return req

    except requests.exceptions.Timeout as e:
        print(f"{page_load_time(url):.2}")

        return False


#url = input("Enter the url whose loading time you want to check: ")
#url2 = ["http://www.youtube.com"]

time.sleep(2)
load = page_load_time(driver, url2) / 1000
#time.sleep(10)   
#print(f"{load:.2}")

print(load)
state = push_data_to_prtg(load)
print(state.text)
time.sleep(1)
os.system("taskkill /im chrome.exe /f")

   