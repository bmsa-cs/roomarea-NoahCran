"""
RoomArea
Author: Noah Crandall

Original assignment by: Edhesive Intro to CS

Find the area of an irregularly shaped room with the shape as shown in room.png.

Ask the user to enter the values for sides A, B, C, D, and E and print out the total room area.

"""
import os
import importlib.util

def run_tests():
  """
  This function will check for the pytest module
  before calling it to run the included tests.py
  """
  if importlib.util.find_spec('pytest') is None: # Check if pytest is installed
    os.system('python3 -m pip install -q pytest')

  command = "python3 -m pytest --tb=line tests.py"
  print(command)
  os.system(command)

def right_triangle_area(base, height):
  """
  Defines the area of any given right triangle

  Parameters: base, height

  Returns: 0.5 * base * height
  """
  r_triangle_area = 0.5 * base * height
  return r_triangle_area


def rectangle_area(length, width):
  """
  Defines the area of any given rectangle

  Parameters: length, width

  Returns: length * width
  """
  rect_area = length * width
  return rect_area


def room_area(a, b, c, d, e):
  """
  Given five measurements, this function calculates and returns the area of the room using the previous functions. From left to right,the room is divided into a rectangle with a length of a, another rectangle with the length of d minus b and e, and a triangle with a base of e

  Parameters: a, b, c, d, e

  Returns: ((a * b) + ((a - c) * (d - (b + e))) + (0.5 * (a - c) * e))
  """

  area_of_leftmost_shape = rectangle_area(a, b)

  a_sub_c = a - c
  d_sub_b_with_e = d - (b + e)
  area_of_middle_shape = rectangle_area(a_sub_c, d_sub_b_with_e)

  area_of_rightmost_shape = right_triangle_area(a_sub_c, e)

  final_area = area_of_leftmost_shape + area_of_middle_shape + area_of_rightmost_shape

  return final_area


if __name__ == "__main__":
  os.system("clear") # clears the console each time you run
  
  a = float(input("A: "))
  b = float(input("B: "))
  c = float(input("C: "))
  d = float(input("D: "))
  e = float(input("E: "))

  final_area = room_area(a, b, c, d, e)
  print("Room area: " + str(final_area))

  tests = input("Run tests? (y/n) ")
  if tests.lower() == 'y':
    run_tests()