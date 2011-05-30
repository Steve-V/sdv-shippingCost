#!/usr/bin/env python

import unittest
import ship
from math import *

class sdvTests(unittest.TestCase):
  
  # KMKG - 43.1676717 / -86.2354387
  
	#def test_distance_KBTL_to_KDET(self):
		#self.assertAlmostEqual ( bearing.haversineDistance( 42.309777, -85.252314, 42.4091944, -83.0098611), 184, 0)

  def test_five_hundred_units_of_freight(self):
    self.assertAlmostEqual( ship.tons(500), 25)
  
  
if __name__ == '__main__':
	unittest.main()