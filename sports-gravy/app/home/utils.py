import requests
import json 
from app import cache

# @cache.cached(timeout=60*5, key_prefix="nfl_all_teams")
# def api_request(params):
#     try:
#         headers = {'Ocp-Apim-Subscription-Key': os.environ["OCP_APIM_SUBSCRIPTION_KEY"],}
#         url = "https://api.fantasydata.net"
#         conn = requests.get("https://api.fantasydata.net/" + params, headers=headers)
#         print conn.status_code
#         return conn.json()
#     except Exception as e:
#         print e
