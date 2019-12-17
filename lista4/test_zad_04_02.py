

import unittest
# import gauss
import lista_04.zad_04_02 as zad_02

class Test_lista_04(unittest.TestCase):
    
    def test_zad_02(self):
        
        self.assertAlmostEqual(zad_02.niuton(2, 100), 2.5118864, 6)
        self.assertAlmostEqual(zad_02.niuton(2, 32), 2, 6)
        self.assertAlmostEqual(zad_02.niuton(8, 32768), 8, 6)
        self.assertAlmostEqual(zad_02.niuton(3, 652), 3.6546813, 6)
        self.assertAlmostEqual(zad_02.niuton(1, 1), 1, 6)
        self.assertAlmostEqual(zad_02.niuton(.5, .2), 0.72477966367, 6)