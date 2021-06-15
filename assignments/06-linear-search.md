

# Assignment One
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Example 1:

Input: ```nums = [2,7,11,15], target = 9```
Output: ```[0,1]```
Output: Because ```nums[0] + nums[1] == 9```, we ```return [0, 1]```.

## Example 2:

Input: ```nums = [3,2,4], target = 6```
Output: ```[1,2]```

## Example 3:

Input: nums = ```[3,3], target = 6```
Output: ```[0,1]```


# Assignment Two
 
 
Given:
- A class representing a subject Grade as below:
```
class Grade:
  def __init__(self, start, to, gradeName):
    self.start = start
    self.to = to
    self.gradeName = gradeName
```
- A List of available grades below:
```
grades = [
  Grade(90, 100, "A"),
  Grade(80, 89, "B"),
  Grade(70, 79, "C"),
  Grade(60, 69, "D"),
  Grade(0, 59, "E")
]
```
- A class representing student marks as below:
```
class Student:
  def __init__(self, name, marks):
    self.name = name
    self.marks = marks
```
  
- A list of students marks a below:
```
students = [
  Student("Dennis", 44),
  Student("Ken", 90),
  Student("Derick", 32),
  Student("James", 67),
  Student("Joyce", 76),
  Student("Linet", 29),
  Student("Ben", 96),
  Student("Jane", 82)
]
```

Implement a function named `super_students` that returns names of students who scored grades "A" and "B" i.e
```
def super_students(grades, students):
  return "names of students who score grades A and B"

```
