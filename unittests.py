#!/usr/bin/env python

import unittest
import ship
from math import *

class costTests(unittest.TestCase):
  def test_cost_of_supplier_A(self):
    self.assertEqual( ship.supplierCost('A'), 15000)
  
  def test_cost_of_supplier_B(self):
    self.assertEqual( ship.supplierCost('B'), 10000)
  
  def test_cost_of_supplier_C(self):
    self.assertEqual( ship.supplierCost('C'), 20000)
  
class distanceTests(unittest.TestCase):
  def test_distance_to_supplier_A(self):
    self.assertEqual( ship.distanceToSupplier('A'), 200)
  
  def test_distance_to_supplier_B(self):
    self.assertEqual( ship.distanceToSupplier('B'), 50)
  
  def test_distance_to_supplier_C(self):
    self.assertEqual( ship.distanceToSupplier('C'), 3520)

class sdvTests(unittest.TestCase):

  def test_five_hundred_units_of_freight(self):
    self.assertAlmostEqual( ship.tons(500), 25)
  
  def test_ten_units_of_frieght(self):
    self.assertAlmostEqual( ship.tons(10), 0.5)
  
  def test_freight_miles_to_move_five_hundred_units_from_A(self):
    self.assertAlmostEqual( ship.tonMiles('A', 500), 5000)
  
  def test_freight_miles_to_move_ten_units_from_C(self):
    self.assertAlmostEqual( ship.tonMiles('C', 10), 1760)
  
  
  
if __name__ == '__main__':
	unittest.main()