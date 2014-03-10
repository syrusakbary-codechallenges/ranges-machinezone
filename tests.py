import unittest
from ranges import Range

class TestAddRange(unittest.TestCase):
    def setUp(self):
        self.ranges = Range()
    def assertEqualRange(self, range):
    	self.assertEquals(self.ranges.ranges, range)
    def test_add_none_intersect(self):
        self.ranges.addRange(10, 15)
        self.ranges.addRange(20, 25)
        self.assertEqualRange([(10, 15), (20, 25)])
    def test_add_intersect_simple_left(self):
        self.ranges.addRange(10, 15)
        self.ranges.addRange(9, 12)
        self.assertEqualRange([(9, 15)])
    def test_add_intersect_simple_right(self):
        self.ranges.addRange(10, 15)
        self.ranges.addRange(11, 16)
        self.assertEqualRange([(10, 16)])
    def test_add_intersect_simple_inner(self):
        self.ranges.addRange(10, 15)
        self.ranges.addRange(11, 12)
        self.assertEqualRange([(10, 15)])
    def test_add_intersect_simple_outer(self):
        self.ranges.addRange(10, 15)
        self.ranges.addRange(9, 16)
        self.assertEqualRange([(9, 16)])
    def test_add_intersect_complex_1(self):
        self.ranges.addRange(10, 15)
        self.ranges.addRange(20, 25)
        self.ranges.addRange(30, 35)
        self.ranges.addRange(10, 20)
        self.assertEqualRange([(10, 25),(30, 35)])
    def test_add_intersect_complex_2(self):
        self.ranges.addRange(10, 15)
        self.ranges.addRange(20, 25)
        self.ranges.addRange(30, 35)
        self.ranges.addRange(16, 19)
        self.assertEqualRange([(10, 25),(30, 35)])
    def test_add_intersect_complex_3(self):
        self.ranges.addRange(10, 15)
        self.ranges.addRange(20, 25)
        self.ranges.addRange(30, 35)
        self.ranges.addRange(17, 18)
        self.assertEqualRange([(10, 15),(17,18),(20, 25),(30, 35)])
    def test_add_intersect_complex_4(self):
        self.ranges.addRange(10, 15)
        self.ranges.addRange(20, 25)
        self.ranges.addRange(30, 35)
        self.ranges.addRange(17, 19)
        self.assertEqualRange([(10, 15),(17, 25),(30, 35)])
    def test_add_intersect_complex_5(self):
        self.ranges.addRange(10, 15)
        self.ranges.addRange(20, 25)
        self.ranges.addRange(30, 35)
        self.ranges.addRange(17, 29)
        self.assertEqualRange([(10, 15),(17, 35)])
    def test_add_intersect_complex_6(self):
        self.ranges.addRange(10, 15)
        self.ranges.addRange(20, 25)
        self.ranges.addRange(30, 35)
        self.ranges.addRange(0, 50)
        self.assertEqualRange([(0, 50)])
    def test_add_intersect_complex_7(self):
        self.ranges.addRange(10, 15)
        self.ranges.addRange(20, 25)
        self.ranges.addRange(30, 35)
        self.ranges.addRange(20, 50)
    def test_query_1(self):
        self.ranges.addRange(10, 15)
        self.ranges.addRange(20, 25)
        self.assertTrue(self.ranges.queryRange(10, 15))
    def test_query_2(self):
        self.ranges.addRange(10, 15)
        self.ranges.addRange(20, 25)
        self.assertTrue(self.ranges.queryRange(11, 14))
    def test_query_3(self):
        self.ranges.addRange(10, 15)
        self.ranges.addRange(20, 25)
        self.assertFalse(self.ranges.queryRange(9, 14))
    def test_query_4(self):
        self.ranges.addRange(10, 15)
        self.ranges.addRange(20, 25)
        self.assertFalse(self.ranges.queryRange(13, 16))


if __name__ == '__main__':
    unittest.main()
