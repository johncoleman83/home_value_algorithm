#!/usr/bin/env python3
"""
ATTOM API
https://api.developer.attomdata.com
"""
import copy
import requests
from attom import secrets
from attom import defaults

URL = 'https://search.onboard-apis.com/propertyapi/v1.0.0'
KEY = secrets.API_KEY
HEADERS_DEFAULT = {
  'Accept': 'application/json',
  'accept': 'application/json',
}
headers = copy.deepcopy(HEADERS_DEFAULT)
headers['apikey'] = KEY

def ping():
  """
  'https://search.onboard-apis.com/propertyapi/v1.0.0/property/detail?id=18471319108031'
  """
  path = "property/detail"
  params = "id={}".format(defaults.ID)
  headers['apikey'] = defaults.API_KEY

  url = "{}/{}?{}".format(URL, path, params)

  return requests.get(url, headers=headers)
