#!/usr/bin/env python3


"""
Return list of 'hello world' string

Single string word with zero iteration

>>> helloworld_pythonic_func(0)
[]
"""


def helloworld_pythonic_func(num_times=1):
    """
    Single string word with negative one parameter for the iteration
    >>> helloworld_pythonic_func(-1)
    []

    Single string word with negative parameter for the iteration
    >>> helloworld_pythonic_func(-2)
    []

    Single string word with no argument passed so that default will
    be used for  iteration
    >>> helloworld_pythonic_func()
    ['hello world']

    Single string word with single iteration
    >>> helloworld_pythonic_func(1)
    ['hello world']

    Single string word with two iterations
    >>> helloworld_pythonic_func(2)
    ['hello world', 'hello world']
    """
    return ["hello world" for _ in range(num_times)]


"""
Return list of single world string

List of words using default argument

>>> helloworld_derived_cfunc("hello", "world")
['hello', 'world']
"""


def helloworld_derived_cfunc(*iter_text_args):
    """
    List of words with single empty string argument

    >>> helloworld_derived_cfunc("")
    ['']

    List of words with single word argument

    >>> helloworld_derived_cfunc("hello")
    ['hello']

    List of words with space in between two words argument

    >>> helloworld_derived_cfunc("hello", " ", "world")
    ['hello', ' ', 'world']

    List of words where each argument word trailing with single space

    >>> helloworld_derived_cfunc("hello ", "world ")
    ['hello ', 'world ']
    """
    return list(map(lambda wor: wor, iter_text_args))


print("hello world text header caption ", end="")


if __name__ == "__main__":
    print()
    import doctest

    doctest.testmod()
