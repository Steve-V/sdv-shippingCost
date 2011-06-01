#!/usr/bin/env python

import unittest
import ship
from math import *

class costTests(unittest.TestCase):
  def test_cost_of_supplier_A(self):
    self.assertEqual( ship.toolingCost('A'), 15000)
  
  def test_cost_of_supplier_B(self):
    self.assertEqual( ship.toolingCost('B'), 10000)
  
  def test_cost_of_supplier_C(self):
    self.assertEqual( ship.toolingCost('C'), 20000)
  
class distanceTests(unittest.TestCase):
  def test_distance_to_supplier_A(self):
    self.assertEqual( ship.distanceToSupplier('A'), 200)
    
  def test_distance_to_supplier_B(self):
    self.assertEqual( ship.distanceToSupplier('B'), 50)
  
  def test_distance_to_supplier_C(self):
    self.assertEqual( ship.distanceToSupplier('C'), 3520)

class shippingCostTests(unittest.TestCase):
  def test_five_hundred_units_of_freight(self):
    self.assertAlmostEqual( ship.tons(500), 25)
  
  def test_ten_units_of_frieght(self):
    self.assertAlmostEqual( ship.tons(10), 0.5)
  
  def test_freight_miles_to_move_five_hundred_units_from_A(self):
    self.assertAlmostEqual( ship.tonMiles(500, 200), 5000)
  
  def test_freight_miles_to_move_ten_units_from_C(self):
    self.assertAlmostEqual( ship.tonMiles(10, 3520), 1760)
  
  def test_cost_to_move_one_full_truckload_from_A(self):
    self.assertAlmostEqual( ship.freightCost(300, 200), 3000)
  
  def test_cost_to_move_20_units_one_mile(self):
    self.assertAlmostEqual( ship.freightCost(20, 1), 1.3)
  
  def test_cost_to_move_450_units_one_mile(self):
    self.assertAlmostEqual( ship.freightCost(450, 1), 24.75)
  
  def test_cost_to_move_500_units_3000_miles(self):
    self.assertAlmostEqual( ship.freightCost(500, 3000), 84000)
  
  def test_cost_to_move_900_units_one_mile(self):
    self.assertAlmostEqual( ship.freightCost(900, 1), 45)
  
  def test_cost_to_move_1400_units_one_mile(self):
    self.assertAlmostEqual( ship.freightCost(1400, 1), 73)
  
  def test_carrying_cost_of_10_units_at_300_apiece(self):
    self.assertAlmostEqual( ship.carryingCost(10, 300), 375)
  
class fullOrderTests(unittest.TestCase):
  def test_cost_of_20_units_50_miles_300_bucks_each(self):
    #20 units = 1 ton, 50 miles at $1.30 per ton = 1.30*50
    # = $65
    
    #processing cost = $100
    
    #cost of the units themselves = 370 * 20 = 7400
    
    #carrying cost = 
    
    #7400 + 100 + 925 + 65 = 8490
    
    self.assertAlmostEqual( ship.orderCost(20,'B'), 8490)
  
  def test_total_cost_of_20_unit_orders_from_B(self):
    self.assertAlmostEqual( ship.yearlyCostOfOrders(20,'B'), 2547000)
    
if __name__ == '__main__':
	unittest.main()