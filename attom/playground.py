#!/usr/bin/env python3
"""
testing out package
"""
import api
from file_io import io
import json
import time

def get_avm_for_properties_list():
  """
  loop through all addresses to get avms
  """
  for number_street, city_state in api.addresses.ADDRESSES_FOR_AVM.items():
    property_avm = api.attomized_avm.get_avm_by_address(number_street, city_state)
    print(property_avm)
    io.append_to_file_storage(json.dumps(property_avm))
    time.sleep(2)

def execute():
  get_avm_for_properties_list()

if __name__ == "__main__":
    """
    MAIN APP
    """
    execute()