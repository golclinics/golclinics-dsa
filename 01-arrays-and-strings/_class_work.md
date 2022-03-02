

## Warm-up challenge

Write a method/function, `reverse(A)` that takes an array of integers, `A` \
and reverses it.

**Examples:**

```python
[1, 2, 5, 6] -> [6, 5, 2, 1]
[] -> []
[1] -> [1]
```

**Instructions:**
- Fork (the clone) `https://github.com/golclinics/golclinics-dsa` and create a folder/directory called
`classwork`. In it, create another folder/dir called `01`. That is where we will put all our
stuff for the `01 Arrays and Strings` topic.
- Once you are done with the class challenges, do a PR against our base repo. It won't be merged but will be for the purpose of class review. The same will apply for your assignments.

> **Note** - if you are using languages like C# and Java, make sure, you _gitignore_ the binary folder.


```c
#include <stdio.h>

int main()
{
    int[] a = {1, 2, 6, 5};
    int* pa = a; // &a, this will be int**

    printf("%p contains -> %d\n", pa, a[0]);

    printf("%p contains -> %d\n", &a[0], a[0]);

    return 0;
}



```

