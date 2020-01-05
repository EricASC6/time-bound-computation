# time-bound-computation

Comparing the input vs. time graph of performing matrix multiplication with python (without numpy) and with numpy

## Why Numpy Destroys Python in speed

```python
   import numpy

   lst = [1, 2, 3] # slow
   numpy_arr = np.array([1, 2, 3]) # super fast

```

### Dynamically Typed vs. Fixed Typed

A python list can contain multiple data types within it such as ints, strings and
booleans. It is flexible, dynamic and its type is not fixed.

On the other hand, numpy multidimensional arrays are fixed, meaning that it can
strictly contain one data type within. You would never find an int type and a string type together numpy arrays. What does this mean?

SPEED!!!

Because of the fixed nature of numpy arrays, performing operations on them is a lot faster than on a list. Take for instance looping. Everytime you loop through a python list, python has to check the data type of the iteration variable even if all of them are of the same type. This process is not necessary when looping through numpy arrays because of fixed type.

### Continuous Memory

![](https://www.stechies.com/userfiles/images/numpyint-4.jpg)

A python list contains the pointers to the items within it, which may be scattered throughout the computer's memory. A numpy array has something called continuous memory which means that all of the item's memory location is right next to each other, making it compact and thus faster to work with.
