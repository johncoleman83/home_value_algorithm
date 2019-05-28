#!/usr/bin/env python3
"""
Name: Home Value Algorithm
Version: 1
Actual Home Values derived from: https://www.realtor.com

Description:
This algo takes input of homes and home specs, & then
calculates an estimate price per individual item
using a weighted system & the estimated cost of an empty lot.

For example, price per sqaure foot, school rank or years from 1950
averages are calculated.

Then with all the averages across all homes, a final mean average
of these costs per item is created.

With the final mean average of the costs per item, an estimate is made
on the cost of the home.

Results:
average home cost: 409321
average home cost - LAND_VALUE: 194321

Grand Total for DESIRED_HOME: 387481
Grand Total for GREAT_HOME: 445492

TODO: import a Big Data Library or build off of someone else's home calculator algo
"""

neighborhood = "Willowbrook"

SOLD_HOMES = [
  { "sqft": 2700, "lot": 43560, "price_sold": 470000, "elementary": 7, "middle": 8, "HS": 8, "interior": 9, "year": 1988 },
  { "sqft": 2500, "lot": 21780, "price_sold": 530000, "elementary": 10, "middle": 8, "HS": 10, "interior": 10, "year": 1957 },
  { "sqft": 2500, "lot": 21780, "price_sold": 330000, "elementary": 9, "middle": 10, "HS": 10, "interior": 4, "year": 1978 },
  { "sqft": 1800, "lot": 21780, "price_sold": 425000, "elementary": 9, "middle": 10, "HS": 10, "interior": 7, "year": 1960 },
  { "sqft": 1600, "lot": 52272, "price_sold": 357000, "elementary": 8.5, "middle": 8, "HS": 10, "interior": 7, "year": 1976 },
  { "sqft": 1400, "lot": 21780, "price_sold": 340000, "elementary": 8.5, "middle": 8, "HS": 10, "interior": 10, "year": 1978 },
  { "sqft": 2200, "lot": 33105, "price_sold": 355000, "elementary": 7, "middle": 8, "HS": 8, "interior": 8, "year": 1975 },
  { "sqft": 1500, "lot": 26136, "price_sold": 300000, "elementary": 10, "middle": 8, "HS": 8, "interior": 10, "year": 1964 },
  { "sqft": 2364, "lot": 20037, "price_sold": 305000, "elementary": 10, "middle": 8, "HS": 8, "interior": 7, "year": 1956 },
  { "sqft": 2244, "lot": 11325, "price_sold": 417000, "elementary": 8.5, "middle": 8, "HS": 10, "interior": 7, "year": 1956 },
  { "sqft": 1849, "lot": 17424, "price_sold": 418500, "elementary": 9, "middle": 10, "HS": 10, "interior": 5, "year": 1960 },
  { "sqft": 3000, "lot": 10890, "price_sold": 536000, "elementary": 10, "middle": 8, "HS": 10, "interior": 10, "year": 1978 },
  { "sqft": 2250, "lot": 11325, "price_sold": 440000, "elementary": 10, "middle": 8, "HS": 10, "interior": 10, "year": 1978 },
  { "sqft": 2800, "lot": 13068, "price_sold": 507000, "elementary": 10, "middle": 8, "HS": 19, "interior": 9, "year": 1987 }
]

LAND_VALUE = 215000

HOME_SPEC_WEIGHT = {
  "sqft": 0.2,
  "lot": 0.05,
  "elementary": 0.15,
  "middle": 0.15,
  "HS": 0.15,
  "interior": 0.25,
  "year": 0.05
}

items_averages = {
    "sqft": { "list_of_values": [], "avg": 0},
    "lot": { "list_of_values": [], "avg": 0},
    "elementary": { "list_of_values": [], "avg": 0},
    "middle": { "list_of_values": [], "avg": 0},
    "HS": { "list_of_values": [], "avg": 0},
    "interior": { "list_of_values": [], "avg": 0},
    "year": { "list_of_values": [], "avg": 0}
  }

def calculate_and_show_basic_mean():
  """
  this is a basic mean of homes based soley on price
  """
  total = 0
  max_home = 0
  least_home = 999999
  for h in SOLD_HOMES:
    price = h["price_sold"]
    if price > max_home:
      max_home = price
    elif price < least_home:
      least_home = price
    total += price
  avg = round(total / len(SOLD_HOMES))
  print("average home cost: {}".format(avg))
  print("average home cost - LAND_VALUE: {}".format(avg - LAND_VALUE), end="\n\n")
  
def show_sold_homes_hash():
  """
  just show the output of homes input hash
  """
  for h in SOLD_HOMES:
    print(h, end="\n\n")

def resolve_averages(show_output = False):
  """
  loop the items_averages to find an average cost per individual unit
  """
  for item, val in items_averages.items():
    l = val["list_of_values"]
    avg = sum(l) / len(l)
    items_averages[item]["avg"] = avg
    if show_output:
      print("averaging cost per unit for")
      print("name: {}, list_of_values: {} avg: {}".format(item, l, avg), end="\n\n")

def average_out(name, val, cost):
  """
  take the costs of one home then add it to the total list of items_averages
  """
  if name in ["sqft", "lot"]:
    avg_per_item = cost / val
    items_averages[name]["list_of_values"].append(avg_per_item)
  if name in ["elementary", "middle", "HS", "interior"]:
    avg_per_item = cost / val
    items_averages[name]["list_of_values"].append(avg_per_item)
  if name == "year":
    time_from_fifty = val - 1950
    avg_per_item = cost / time_from_fifty
    items_averages[name]["list_of_values"].append(avg_per_item)

def loop_homes():
  """
  Loop sold homes and calculate the approximate cost of
  each indivial home specifier on a per home basis
  """
  for home in SOLD_HOMES:
    home_val = home["price_sold"] - LAND_VALUE
    home["home_value"] = home_val
    for name, val in home.items():
      if name == "price_sold" or name == "home_value":
        continue
      cost = home_val * HOME_SPEC_WEIGHT[name]
      item = { "name": val, "cost": cost }
      home[name] = item
      average_out(name, val, cost)

def calculate_home_cost(home_name, home_to_check):
  total_cost = LAND_VALUE
  for name, val in items_averages.items():
    if name == "year":
      time_from_fifty = home_to_check[name] - 1950
      total_cost += time_from_fifty * val["avg"]
      continue
    total_cost += home_to_check[name] * val["avg"]
  print("Grand Total for {}: {}".format(home_name, round(total_cost)))

def execute():
  """
  This executes main jobs
  and can be used to show / print info
  """
  calculate_and_show_basic_mean()
  loop_homes()
  resolve_averages()
  calculate_home_cost("DESIRED_HOME", DESIRED_HOME)
  calculate_home_cost("GREAT_HOME", GREAT_HOME)

DESIRED_HOME = { "sqft": 2900, "lot": 1.1, "price_sold": None, "elementary": 10, "middle": 8, "HS": 10, "interior": 3, "year": 1969 }
GREAT_HOME = { "sqft": 2900, "lot": 1.1, "price_sold": None, "elementary": 10, "middle": 10, "HS": 10, "interior": 10, "year": 1980 }


if __name__ == "__main__":
  """
  MAIN APP
  """
  execute()
