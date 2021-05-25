# Analysis the space and time complexities of the following algorithms


## Countdown

Given an integer `n` as input `countdown(n)` prints the numbers n to 1 in descending
order then prints "Blast off!"

```python
def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("Blast off!")
```

## Countdown recursive

This solves the same problem as the previous algorithm, but uses recursion instead of a loop.
This might not be obvious if you're not familiar with function call stacks. Bonus points
if you can explain why the space complexity here is not the same as the space complexity
of the loop-based implementation. Feel free to research on the Internet.

```python
def countdown_recursive(n):
    if n == 0:
        print("Blast off")
    else:
        print(n)
        countdown_recursive(n - 1)
```

## Palindrome

Given a string `s` as input, the `is_palindrome(s)` function returns true if `s` is a palindrome
and returns false otherwise. A palindrom in this case is a word that reads the same forward and
backwards, e.g. `madam`

```python
def is_palindrome(s):
    if len(s) == 0:
        return True   # an empty string is a palindrome

    size = len(s)
    midpoint = size // 2
    
    for i in range(midpoint + 1):
        if s[i] != s[size - i - 1]:
            return False
    return True
```

## Palindrome using reversed string

This solves the palindrome problem stated above by comparing the original
string with the reversed version of the string:

```python
def is_palindrome_rev(s):
    reversed_s = s[::-1] # This is a neat trick to reverse a string in python
    return s == reversed_s
```

The above method uses the fancy slicing feature in Python `[::-1]` which reverses
a sequence. The following implementation

```python
def is_palindrome_rev2(s):
    reversed_seq = reversed(s) # creates a sequence with the characters in the string in reverse
    reversed_s = ''.join(reversed_seq) # transformed the reversed sequence into a string
    return s == reversed_s
```

## Palindrome using recursion

This implementation is similar to the loop-based version in that it compares a pair of letters
at equal distances from the middle of the string in each iteration. But it does so using
recursion instead of a loop:

```python
def is_palindrome_recur(s):
    if len(s) == 0:
        return True
    if len(s) == 1:
        return True
    
    # in python s[-1] is the last element of the sequence s, i.e. "madam"[-1] -> "m"
    # and s[1: -1] will create a slice starting from the second element to the second last element
    # "madam"[1: -1] -> "ada"
    return s[0] == s[-1] and is_palindrome_recur(s[1:-1])
```
**Bonus questions**:

- Between `is_palindrome`, `is_palindrome_rev` and `is_palindrome_recur` which do you think is more efficient, and why?
- Which of the two implementations would you prefer for your own code, and why?

If you want to go the extra mile, you can try to implement these functions in an Python REPL and compare their runtimes
against a single input string. You can use the `timeit` module to measure their run times.

e.g:

```python
import timeit

s = "m" * 500 + "u" + "m" * 500 # this creates a string with 1001 characters, 500 'm' followed by a 'u' followed by 500 'm'.

# This will execute is_palindrome(s) 1000 times and return the average execution time in seconds
result = timeit.timeit(lambda: is_palindrome(s), number=1000) 
print("is_palindrome time:", result)
result = timeit.timeit(lambda: is_palindrome_rev(s), number=1000) 
print("is_palindrome_rev time:", result)
result = timeit.timeit(lambda: is_palindrome_rev2(s), number=1000) 
print("is_palindrome_rev2 time:", result)
result = timeit.timeit(lambda: is_palindrome_recur(s), number=1000) 
print("is_palindrome_recur time:", result)
```

Did the result of the timer match your expectations? Did the algorithm you expected to be fastest end up being
fastest? If the result of the above benchmarks did not match what you predicted, are you able to provide reasons
that could explain the "unexpected" results?

## Concatenating arrays

Given 2 arrays A and B of size m and n respectively, return a new array that contains the elements of the first array followed
by the elements of the second array.

This might not be immediately obvious. Bare in mind that in this example we have to inputs we care about so we have to consider
how an increase in either `m` or `n` affects the size of the `result` or the total number of iterations performed by the function.

For this example, let's assume that `result.append()` is a constant-time operation.

```python

def concatenate_arrays(A, B):
    result = []
    for x in A:
        result.append(x)
    for y in B:
        result.append(y)
    return result
```

## Rotate an array to the left by a certain amount

Given an array A and a distance `d`, the `rotate_left` function moves every element in `A` `d` steps to the left.
Items will be cycled back to the end if they pass beginning.

For example, let A = [3, 2, 1, 10, 15, 3] and d = 3, then `rotate_left(A, d)` will result in the following array:
`[10, 15, 3, 3, 2, 1]`

```python
def rotate_left(A, d):
    for _ in range(d):
        first_item = A[0]
        for i in range(len(A)):
            A[i] = A[i + 1]
        A[-1] = first_item

```

**Bonus question**: Can you think of ways to improve the efficiency function, or come up with a "better" implementation. "Better"
either in terms of time or space or both.

## How many times can a number be divide by 2 until we get to 1

The `count_div_2(n)` functions counts the number of times the input number
`n` can be divided by 2 before it reaches one or less.

The time complexity may not be immediately obvious to all, but here's a hint:
Count the number of iterations that this functions makes when then input is 4, 5, 6, 7, 8.
At which values of `n` does the number of iterations increase compared to when `n = 4`?
Now keep trying for values > 8, at which point does the number of iterations increase by 1 compared
to when `n=8`? Do you see a pattern or trend between the growth in `n` and how that affects
the increase in iterations? In general, how much should `n` grow before count increases by 1? Do you
see a mathematical releationship `n` and the total number of iterations?

```python
def count_div_2(n):
    count = 0
    while n > 1:
        n = n // 2
        count += 1
    return count
```

## Integer square root

Given a positive integer number `x` which has an integer square root, the `int_sqrt(x)` returns
the square root of x. If `x` does not have a square root, the function returns `-1`.

E.g. `int_sqrt(16)` -> `4`, `int_sqrt(10)` -> -1

```python
def int_sqrt(x):
    for i in range(x):
        if i * i == x:
            return i
    
    return -1
```

## Integer square root bisection method

This solves the same problem as `int_sqrt` using a different approach:
instead of trying out all numbers from 0-x, it tries out the number in the middle
of the range, then eliminates half of the range where it's sure the answer cannot be found
then keep repeating that process until the answer is found.


```python
def int_sqrt_bisect(x):
    low = 0
    high = x
    guess = x // 2
    while True:
        diff = guess * guess - x
        if diff == 0:
            return guess
        if diff < 0: # our guess was lower than the true square root
            low = guess # so we should continue searching in the range [guess - high]
        else: # our diff was higher than the true square root
            high = guess # we continue searching in the range [low - guess]
        
        if high - low <= 1: # at this point we can't an integer square root for x
            break

        guess = (low + high) // 2 # pick a guess in the middle of the new range
    return -1
```
