#!/usr/bin/env python3
"""
WILLOWBROOK SOLD HOMES
"""

neighborhood = "Willowbrook"


# "elementary", "middle", "HS", "renovations" score out of 10
SOLD_HOMES = [
  { "sqft": 2700, "lot": 43560, "price_sold": 470000, "elementary": 7, "middle": 8, "HS": 8, "renovations": 9, "year": 1988 },
  { "sqft": 2500, "lot": 21780, "price_sold": 530000, "elementary": 10, "middle": 8, "HS": 10, "renovations": 10, "year": 1957 },
  { "sqft": 2500, "lot": 21780, "price_sold": 330000, "elementary": 9, "middle": 10, "HS": 10, "renovations": 4, "year": 1978 },
  { "sqft": 1800, "lot": 21780, "price_sold": 425000, "elementary": 9, "middle": 10, "HS": 10, "renovations": 7, "year": 1960 },
  { "sqft": 1600, "lot": 52272, "price_sold": 357000, "elementary": 8.5, "middle": 8, "HS": 10, "renovations": 7, "year": 1976 },
  { "sqft": 1400, "lot": 21780, "price_sold": 340000, "elementary": 8.5, "middle": 8, "HS": 10, "renovations": 10, "year": 1978 },
  { "sqft": 2200, "lot": 33105, "price_sold": 355000, "elementary": 7, "middle": 8, "HS": 8, "renovations": 8, "year": 1975 },
  { "sqft": 1500, "lot": 26136, "price_sold": 300000, "elementary": 10, "middle": 8, "HS": 8, "renovations": 10, "year": 1964 },
  { "sqft": 2364, "lot": 20037, "price_sold": 305000, "elementary": 10, "middle": 8, "HS": 8, "renovations": 7, "year": 1956 },
  { "sqft": 2244, "lot": 11325, "price_sold": 417000, "elementary": 8.5, "middle": 8, "HS": 10, "renovations": 7, "year": 1956 },
  { "sqft": 1849, "lot": 17424, "price_sold": 418500, "elementary": 9, "middle": 10, "HS": 10, "renovations": 5, "year": 1960 },
  { "sqft": 3000, "lot": 10890, "price_sold": 536000, "elementary": 10, "middle": 8, "HS": 10, "renovations": 10, "year": 1978 },
  { "sqft": 2250, "lot": 11325, "price_sold": 440000, "elementary": 10, "middle": 8, "HS": 10, "renovations": 10, "year": 1978 },
  { "sqft": 2800, "lot": 13068, "price_sold": 507000, "elementary": 10, "middle": 8, "HS": 19, "renovations": 9, "year": 1987 }
]

LAND_VALUE = 215000

DESIRED_HOME = { "sqft": 2900, "lot": 30560, "price_sold": None, "elementary": 10, "middle": 8, "HS": 10, "renovations": 3, "year": 1969 }
PERFECT_HOME = { "sqft": 2900, "lot": 43560, "price_sold": None, "elementary": 10, "middle": 10, "HS": 10, "renovations": 10, "year": 1990 }
