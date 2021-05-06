"""
Teddy b

"""
from SimpleFraction import SimpleFraction
import unittest


class TestSimpleFraction(unittest.TestCase):
    def test_init(self):
        # testing values 25, 50
        f = SimpleFraction(25, 50)
        self.assertEqual(f.num, 25)
        self.assertEqual(f.denom, 50)

        #testing values 0, 50
        f = SimpleFraction(0, 50)
        self.assertEqual(f.denom,1)
        #testing for type error 
        self.assertRaises(TypeError,SimpleFraction,"a")
        #testing for zero division error
        self.assertRaises(ZeroDivisionError,SimpleFraction,1,0)

        
    def test_multiply(self):
        #testing values 60,30
        x = SimpleFraction(60,30)
        #testing values 20, 80
        y = SimpleFraction(20,80)
        ans = x.multiply(y)
        self.assertEqual(ans.num,1200)
        self.assertEqual(ans.denom,2400)
        #testing values 5,15 
        y = SimpleFraction(5,15)
        # mutiples 5/15 by a integer to ensure it works when using int
        ans = y.multiply(3)
        self.assertEqual(ans.num,15)
        self.assertEqual(ans.denom,45)
        
        
    
    def test_divide(self):
        #test values 60,30
        x = SimpleFraction(60,30)
        
        y = SimpleFraction(20,80)
        ans = x.divide(y)
        self.assertEqual(ans.num,4800)
        self.assertEqual(ans.denom,600)

        x = SimpleFraction(30,5)
        y = SimpleFraction(15,3)
        ans = x.divide(y)
        self.assertEqual(ans.num,90)
        self.assertEqual(ans.denom,75)

        x = SimpleFraction(30,2)
        y = SimpleFraction(15,1)
        ans = x.divide(y)
        self.assertEqual(ans.num,30)
        self.assertEqual(ans.denom,30)
        

    def test__eq__(self):
        # testing values 60,30
        x = SimpleFraction(60,30)
        y = SimpleFraction(60,30)
        ans = x._eq_(y)
        self.assertAlmostEqual(ans,True)

        #tesing values 655 and 30
        x = SimpleFraction(655,3)
        #testing values 60 and 3030)
        y = SimpleFraction(60,303)
        ans = x._eq_(y)
        self.assertAlmostEqual(ans,False)

    def test_make_reciprocal(self):
        #testing values 60,30
        c = SimpleFraction(60,30)
        ans = c.make_reciprocal()
        #compares to orginal numerator
        self.assertEqual(ans.num,c.denom)
        #comparing to orginaly denominator)
        
        
        self.assertEqual(ans.denom,c.num)
        #testing values 1,20
        c = SimpleFraction(1,20)
        ans = c.make_reciprocal()
        self.assertEqual(ans.num,c.denom)
        self.assertEqual(ans.denom,c.num)

    def validate():
        f = SimpleFraction(25, 50)
        self.assertEqual(f.num, 25)
        self.assertEqual(f.denom, 50)
        self.assertRaises(TypeError,SimpleFraction,"l")
        self.assertEqual(f.denom,1)
        self.assertRaises(TypeError,SimpleFraction,"a")
        self.assertRaises(ZeroDivisionError,SimpleFraction,1,0)
       

def main():
    unittest.main(verbosity = 3)

main()
