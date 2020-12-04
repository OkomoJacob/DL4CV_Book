## Fibonacci Sequence
* The Fibonacci sequence is a series of numbers where the next number of the sequence is found
by summing the two integers that preceeds the integer in question. 
* For example, given the sequence 0, 1, 1, the next number
is found by adding 1 + 1 = 2. Similarly, given 0, 1, 1, 2, the next integer in the sequence is <br />
    ```1 + 2 = 3.```
Following that pattern, the first handful of numbers in the sequence are as follows: <br />
    ```0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...````
Of course, we can also define this pattern in an (extremely unoptimized) Python function using
recursion as above.

As you can see, the Fibonacci sequence is straightforward and is an example of a family of
functions that:
    ```
    1. Accepts an input, returns an output.
    2. The process is well defined.
    3. The output is easily verifiable for correctness.
    4. Lends itself well to code coverage and test suites.
    ```
## Requirements
python 3.0.0+