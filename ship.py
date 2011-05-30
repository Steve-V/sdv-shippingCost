#!/usr/bin/env python

#import 

def toolingCost(supplier):
  if supplier == "A":
    return 15000
  if supplier == "B":
    return 10000
  if supplier == "C":
    return 20000

def distanceToSupplier(supplier):
  if supplier == "A":
    return 200
  if supplier == "B":
    return 50
  if supplier == "C":
    return 3520


def orderCost(supplier, amount):
  import math
  return math.fsum( shippingCost(supplier, amount), inventoryCost(amount), processingCost() )

def processingCost():
  return 100

def tonMiles(units, distance):
  return float( tons(units) * distance )

def tons(units):
  return float( (float(units) * 100) / 2000)

def freightCost(units, distance):
  if units == 300:
    return tonMiles(units, distance)
  if units < 300:
    return (1.3 * tonMiles(units, distance))
  if units > 300:
    return ( tonMiles(300, distance) + freightCost(units-300, distance) )

def getInventoryCost(supplier, amount):
  pass

def main():
  
  print getResult()
  
  
if __name__ == '__main__':
  main()