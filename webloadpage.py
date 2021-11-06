from urllib.request import urlopen
import time
import requests

def get_load_time(url):
    """This function takes a user defined url as input
    and returns the time taken to load that url in seconds.
    Args:
        url (string): The user defined url.
    Returns:
        time_to_load (float): The time taken to load the website in seconds.
    """

    if ("https" or "http") in url:  # Checking for presence of protocols
        open_this_url = urlopen(url)  # Open the url as entered by the user
    else:
        open_this_url = urlopen("https://" + url)  # Adding https to the url
    start_time = time.time()  # Time stamp before the reading of url starts
    open_this_url.read()  # Reading the user defined url
    end_time = time.time()  # Time stamp after the reading of the url
    open_this_url.close()  # Closing the instance of the urlopen object
    time_to_load = end_time - start_time

    return time_to_load


#========push to PRTG ==============================================
def push_data_to_prtg(value_i) :
    try :
        url = f"http://prtg3.psn.co.id:5050/9E8AF46A-48FB-418F-A66C-3280B5AA657C?value={value_i}"

        req = requests.get(url, timeout=10)

        return req

    except requests.exceptions.Timeout as e:
        print(f"{get_load_time(url):.2}")

        return False
    

if __name__ == '__main__':
    #url = input("Enter the url whose loading time you want to check: ")
    url = ["www.youtube.com"]
    for i in url:
        #print(f"\nThe time taken to load {url} is {get_load_time(url):.2} seconds.")
        #load = print(f"{get_load_time(url):.2}")
        load = get_load_time(url)
        
        #print(f"{load:.2}")

        state = push_data_to_prtg(load)
        print(state.text)





