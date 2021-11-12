from selenium import webdriver
import requests
import time
#from selenium.webdriver.chrome import options
#from selenium.webdriver.chrome.options import options

#Deklarasi Webdriver Chrome
options = webdriver.ChromeOptions()
options.headless = True

driver = webdriver.Chrome(options = options, executable_path='/home/psn/Downloads/chromedriver')
driver.get("https://www.youtube.com")
navigation_start = driver.execute_script(
        "return performance.timing.navigationStart")
load_eventend = driver.execute_script(
        "return performance.timing.loadEventEnd")
    #performance_data = driver.execute_script("return window.performance.getEntries();")
total_time = load_eventend - navigation_start

print(total_time)

def push_data_to_prtg(value_i) :
    try :
        url = f"http://prtg3.psn.co.id:5050/DBACF908-2C25-4E81-B8E5-A00BFF2CACD8?value={value_i}"

        req = requests.get(url, timeout=15)

        return req

    except requests.exceptions.Timeout as e:
        #print(f"{page_load_time(url):.2}")

        return False

state = push_data_to_prtg(total_time)
print(state.text)
time.sleep(1)
