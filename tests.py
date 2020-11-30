from unittest import TestCase
from unittest.mock import patch
from random import random, randint

import main


class RoomAreaTest(TestCase):
    """
    This class contain tests for the RoomArea program.
    """
    def test_sample(self):
        """This test verifies that the output matches the sample run."""
        answer = main.room_area(11.0,2.0,4.0,7.0,1.0)
        self.assertEqual(answer, 53.5, "Incorrect value returned for float inputs.")

    def test_integers(self):
        """This test verifies that even when integers are inputted, the final result is a float."""
        answer = main.room_area(11,2,4,7,1)
        self.assertEqual(answer, 53.5, "Incorrect value returned for integer inputs. Make sure your final result is a float.")      
    
    def test_zero(self):
        """This test verifies the case of all 0 measurements."""
        answer = main.room_area(0,0,0,0,0)
        self.assertEqual(answer, 0.0, "Does not return 0 for measurements of 0")
    
    def test_random(self):
        """This test tests a random set of values."""
        a,b,c,d,e = [round(random()*randint(1,50),2) for x in range(5)]
        answer = main.room_area(a,b,c,d,e)
        self.assertAlmostEqual(answer, a*(d-0.5*e)+c*(b-d+0.5*e),2,"Random values failed the test: {}".format([a,b,c,d,e]))

    def test_square(self):
        """This test tests a square room (a=b=c=d, e=0)"""
        length = randint(1,50)
        answer = main.room_area(length,length,length,length,0)
        self.assertEqual(answer, length**2, "If a,b,c,d are all equal and e is 0, the area should just be one large square.")

    def test_right_triangle_area(self):
        """This directly tests the right triangle function."""
        b = randint(1,50)
        h = randint(1,50)
        answer = main.right_triangle_area(b,h)
        self.assertEqual(answer, 0.5*b*h, "Your right_triangle_area function does not return the correct area.")
    
    def test_rectangle_area(self):
        """This directly tests the square_area function."""
        w = randint(1,50)
        h = randint(1,50)
        answer = main.rectangle_area(w,h)
        self.assertEqual(answer, w*h, "Your rectangle_area function does not return the correct area.")