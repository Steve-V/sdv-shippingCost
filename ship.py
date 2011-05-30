#!/usr/bin/env python

#import 

def supplierCost(supplier):
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
    return 3250


def orderCost(supplier, amount):
  import math
  return math.fsum( shippingCost(supplier, amount), inventoryCost(amount), processingCost() )

def processingCost():
  return 100

def tonMiles(supplier, amount):
  return ( tons(amount) * distanceToSupplier(supplier) )

def tons(amount):
  return ( (amount * 100) / 2000)

def getInventoryCost(supplier, amount):
  pass

def main():
  
  print getResult()
  
  
if __name__ == '__main__':
  main()