"""
RoomArea
Author:

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

  """

  return 0


def rectangle_area(length, width):
  """

  """

  return 0


def room_area(a, b, c, d, e):
  """
  Given five measurements, this function calculates and returns the area of the room.

  """

  return 0


if __name__ == "__main__":
  os.system("clear") # clears the console each time you run
  
  a = input("A: ")
  b = input("B: ")
  c = input("C: ")
  d = input("D: ")
  e = input("E: ")

  final_area = room_area(a, b, c, d, e)
  print("Room area: " + str(final_area))

  tests = input("Run tests? (y/n)")
  if tests.lower() == 'y':
    run_tests()