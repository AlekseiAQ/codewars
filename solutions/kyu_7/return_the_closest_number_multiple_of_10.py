"""Return the closest number multiple of 10
https://www.codewars.com/kata/return-the-closest-number-multiple-of-10

Given a number return the closest number to it that is divisible by 10.

Example input:

```
22
25
37
```

Expected output:

```
20
30
40
```
"""


def closest_multiple_10(i):
    return round(i, -1)
