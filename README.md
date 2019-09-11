stats
===========


### Running the Program

Clone the [statistics repo](https://github.com/gbova/stats)

Create a Python virtualenv

Open the python shell
  -  run *python* in your terminal

Import the necessary models
  -  *from models import DataCapture* in the Python shell



### About the Program

DataCapture.add(int elem) -> no return value
  -  Adds the given value to the DataCapture instance
  -  Raises NegativeInputException if the given element is negative
  -  O(1) because Python's list is un-sorted and allows constant appending

DataCapture.build_stats() -> Stats
  -  Returns a Stats object, built out of the existing data values in the DataCapture instance
  -  O(n logn) because I used Python's sort algorithm, which is O(n logn), to sort the values (of which there will
     be a max of n)

Stats.less(int value) -> int
  -  Returns the number of elements that are less than the given value
  -  O(1) because Python's dictionaries are wrapped hash maps and have constant time access

Stats.greater(int value) -> int
  -  Returns the number of elements that are greater than the given value
  -  O(1) because Python's dictionaries are wrapped hash maps and have constant time access

Stats.between(int lower_boundary, int upper_boundary) -> int
  -  Returns the number of elements that are between the two given values (inclusive)
  -  Raises MinLargerThanMaxException if the given lower_boundary is larger than the given upper_boundary
  -  O(1) because Python's dictionaries are wrapped hash maps and have constant time access
