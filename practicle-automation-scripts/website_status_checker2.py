# Script 16 Website Status Checker 2
import sys
import os
path=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','file-and-text-scripts'))
sys.path.append(path)
print(path)
import to_do_list as td
td.main()
# import requests
# from requests.exceptions import RequestException
# url=input("Enter the website URL (including http:// or https://): ")
# try:
#     response=requests.get(url)
#     if response.status_code==200:
#         print(f"{url} is UP!")
#     else:
#         print(f"{url} return status code {response.status_code} (may be DOWN or Have an Issue)) ")
# except RequestException as e:
#     print(f"{url} is DOWN!")
#     print(f"Error: {e}")