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

TODO: import a Big Data Library or build off of someone else's home calculator algo
"""
from sold_homes import *

# SET THESE TO THE NEIGHBORHOOD OF CHOICE
homes_data = willowbrook.SOLD_HOMES
land_value = willowbrook.LAND_VALUE
desired_home = willowbrook.DESIRED_HOME
perfect_home = willowbrook.PERFECT_HOME

# Currently these are updated manually,
# but should be automatically updated,
# i.e. "trained" based on the results from
# verify_predictability()
HOMES_ATTRIBUTES_WEIGHTED_VALUES = {
  "sqft":        0.125,
  "lot":         0.1,
  "elementary":  0.1,
  "middle":      0.1,
  "HS":          0.1,
  "renovations": 0.3,
  "year":        0.175,
}

items_averages = {
    "sqft": { "list_of_values": [], "avg": 0},
    "lot": { "list_of_values": [], "avg": 0},
    "elementary": { "list_of_values": [], "avg": 0},
    "middle": { "list_of_values": [], "avg": 0},
    "HS": { "list_of_values": [], "avg": 0},
    "renovations": { "list_of_values": [], "avg": 0},
    "year": { "list_of_values": [], "avg": 0}
  }

def base_year():
  return min([h["year"] for h in homes_data]) - 10

def weight_check():
  """
  make sure the weighted values add up to 100% of home cost
  """
  if sum(HOMES_ATTRIBUTES_WEIGHTED_VALUES.values()) < 0.9999999999:
    print("Miscalculation of weights")
    exit(1)

def calculate_and_show_basic_mean():
  """
  this is a basic mean of homes based soley on price
  """
  print("min home cost: {}".format(min([h["price_sold"] for h in homes_data])))
  print("max home cost: {}".format(max([h["price_sold"] for h in homes_data])))

  total = sum([h["price_sold"] for h in homes_data])
  avg = round(total / len(homes_data))
  print("mean home cost: {}".format(avg))
  print("average home cost - land_value: {}".format(avg - land_value), end="\n\n")
  
def show_sold_homes_hash():
  """
  just show the output of homes input hash
  """
  for h in homes_data:
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

def average_out_items(name, val, cost):
  """
  input the name, amount and cost of one home item,
  add it to the total list of items_averages
  """
  if name in ["sqft", "lot"]:
    avg_per_item = cost / val
    items_averages[name]["list_of_values"].append(avg_per_item)
  if name in ["elementary", "middle", "HS", "renovations"]:
    # this is the same calculation, the distinction is
    # only since these values are all out of 10
    avg_per_item = cost / val
    items_averages[name]["list_of_values"].append(avg_per_item)
  if name == "year":
    time_from_base = val - base_year()
    avg_per_item = cost / time_from_base
    items_averages[name]["list_of_values"].append(avg_per_item)

def loop_homes():
  """
  Loop sold homes and calculate the approximate cost of
  each indivial home specifier on a per home basis
  """
  for home in homes_data:
    home_val = home["price_sold"] - land_value
    home["home_value"] = home_val
    for name, val in home.items():
      if name == "price_sold" or name == "home_value":
        continue
      cost = home_val * HOMES_ATTRIBUTES_WEIGHTED_VALUES[name]
      average_out_items(name, val, cost)

def predict_home_cost(home):
  predicted_cost = land_value

  for name, val in items_averages.items():
    if name == "year":
      time_from_base = home[name] - base_year()
      predicted_cost += time_from_base * val["avg"]
      continue
    predicted_cost += home[name] * val["avg"]
  return predicted_cost

def predict_homes_sale_price():
  homes_predicted = {
    "desired_home": desired_home,
    "perfect_home": perfect_home
  }
  for home_name, home in homes_predicted.items():
    predicted_cost = predict_home_cost(home)

    print("Grand Total for {}: {}".format(home_name, round(predicted_cost)))

def verify_predictability():
  total_difference = 0
  for home in homes_data:
    predicted_cost = predict_home_cost(home)

    print("Actual Cost: {}".format(home.get("price_sold")))
    print("Predicted Cost: {}".format(round(predicted_cost)))
    cost_difference = home.get("price_sold") - round(predicted_cost)
    print("Difference: {}".format(cost_difference))
    total_difference += cost_difference
  print("Average Difference: {}".format(round(total_difference / len(homes_data))), end="\n\n")



def execute():
  """
  This executes main jobs
  and can be used to show / print info
  """
  weight_check()
  calculate_and_show_basic_mean()
  loop_homes()
  resolve_averages()
  verify_predictability()
  predict_homes_sale_price()

if __name__ == "__main__":
  """
  MAIN APP
  """
  execute()
