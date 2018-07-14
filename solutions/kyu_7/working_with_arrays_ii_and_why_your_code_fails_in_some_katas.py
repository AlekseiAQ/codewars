"""Working with arrays II (and why your code fails in some katas)
https://www.codewars.com/kata/working-with-arrays-ii-and-why-your-code-fails-in-some-katas

In this kata the function returns an array/list like the one passed to it but with its nth element removed (with `0 <= n <= array/list.length - 1`). The function is already written for you and the basic tests pass, but random tests fail. Your task is to figure out why and fix it.

Good luck!

~~~if:javascript
Some good reading: [MDN Docs about arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
~~~
~~~if:python
Some good reading: [Python Docs about lists](https://docs.python.org/3/tutorial/datastructures.html)
~~~
~~~if:coffeescript
Some good reading: [CoffeeScript docs](http://coffeescript.org/)
~~~


"""


from copy import deepcopy


def remove_nth_element(lst: list, n: int) -> list:
    lst_copy = deepcopy(lst)
    del lst_copy[n]
    return lst_copy
