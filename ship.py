#!/usr/bin/env python

#import 

def toolingCost(supplier):
  if supplier == "A":
    return 15000
  if supplier == "B":
    return 10000
  if supplier == "C":
    return 20000

def warehouseCost():
  return 10000

def distanceToSupplier(supplier):
  if supplier == "A":
    return 200
  if supplier == "B":
    return 50
  if supplier == "C":
    return 3520

def supplierUnitPrices(supplier, orderSize):
  if supplier == "A":
    if orderSize < 400: return 350
    if orderSize < 600: return 325
    return 310
  if supplier == "B":
    if orderSize < 400: return 370
    if orderSize < 600: return 340
    return 300
  if supplier == "C":
    if orderSize < 400: return 340
    if orderSize < 600: return 315
    return 295

def orderCost(orderSize, supplier):
  orderUnitPrice = supplierUnitPrices(supplier, orderSize)
  one = freightCost(orderSize, distanceToSupplier(supplier))
  two = carryingCost(orderSize, orderUnitPrice)
  three = processingCost()
  four = ( supplierUnitPrices(supplier, orderSize) * orderSize )
  total = one + two + three + four
  return total

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

def carryingCost(orderSize, orderUnitPrice):
  totalOrderCost = orderSize * orderUnitPrice
  averageInventoryCost = totalOrderCost / 2
  carryingCost = averageInventoryCost / 4
  return carryingCost

def yearlyCostOfOrders(sizeOfOrders, supplier):
  ordersRemaining = 6000
  totalCost = 0
  while ordersRemaining > sizeOfOrders:
    totalCost += orderCost(sizeOfOrders, supplier)
    ordersRemaining -= sizeOfOrders
  totalCost += orderCost(ordersRemaining, supplier)
  return totalCost

def finalTotals(warehouse):
  supplierA = []
  supplierB = []
  supplierC = []
  lowestA = 9999999999999999999
  lowestB = 9999999999999999999
  lowestC = 9999999999999999999
  orderA = 0
  orderB = 0
  orderC = 0
  if warehouse:
    maxOrderSize = 601
  else:
    maxOrderSize = 501
  for orderSize in range(1,maxOrderSize):
    # A
    trial = yearlyCostOfOrders(orderSize,'A')
    if trial < lowestA:
      lowestA = trial
      orderA = orderSize
    # B
    trial = yearlyCostOfOrders(orderSize,'B')
    if trial < lowestB:
      lowestB = trial
      orderB = orderSize
    # C
    trial = yearlyCostOfOrders(orderSize,'C')
    if trial < lowestC:
      lowestC = trial
      orderC = orderSize
    
  
  if warehouse:
    print "============FINAL COST (Warehouse)==========="
    print lowestA + toolingCost('A') + warehouseCost() + " " + str(orderA)
    print lowestB + toolingCost('B') + warehouseCost() + " " + str(orderB)
    print lowestC + toolingCost('C') + warehouseCost() + " " + str(orderC)
  else:
    print "============FINAL COST (No Warehouse)==========="
    print str(lowestA) + str(toolingCost('A') ) + " " + str(orderA)
    print str(lowestB) + str(toolingCost('B') ) + " " + str(orderB)
    print str(lowestC) + str(toolingCost('C') ) + " " + str(orderC)

def main():
  
  finalTotals(False)
  print
  print
  finalTotals(True)
  
  
if __name__ == '__main__':
  main()