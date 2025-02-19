# This file could contain functions to interact with APIs,
# reducing code duplication in your task modules.  For example:

# import requests

# def make_api_request(url, method='GET', headers=None, data=None):
#     try:
#         response = requests.request(method, url, headers=headers, json=data)
#         response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
#         return response.json()
#     except requests.exceptions.RequestException as e:
#         print(f"API Request Error: {e}")
#         return None