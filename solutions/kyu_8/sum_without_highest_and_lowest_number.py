"""Sum without highest and lowest number
https://www.codewars.com/kata/sum-without-highest-and-lowest-number

Sum all the numbers of the array (in F# and Haskell you get a list) except the highest and the lowest element (the value, not the index!).<br>
(The highest/lowest element is respectively only one element at each edge, even if there are more than one with the same value!)<br><br>
Example:
```
{ 6, 2, 1, 8, 10 } => 16
{ 1, 1, 11, 2, 3 } => 6
```
<br>

If array is empty, null or None, or if only 1 Element exists, return 0.<br>
<strong>Note:</strong>In C++ instead null an empty vector is used. In C there is no null. ;-)
<br><br>


```haskell
-- There's no null in Haskell, therefore Maybe [Int] is used. Nothing represents null.
```



Have fun coding it and please don't forget to vote and rank this kata! :-) 

I have created other katas. Have a look if you like coding and challenges.

"""


def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)
