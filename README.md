#Project Euler Solutions

This is a small collection of my solutions, in various languages, to [Project Euler](https://projecteuler.net) problems.

##Languages

* Swift
* Scala
* Python
* C/C++
* JavaScript

##Progress

Language | Progress
-------- | --------
Swift | 2/516
Scala | 3/516
Python | 3/516
C/C++ | 2/516
JavaScript | 3/516

##Solutions
###Solution Index
[PE1](https://github.com/j-haj/project-euler#pe1)

[PE2](https://github.com/j-haj/project-euler#pe2)

PE3

###PE1
There is not much need for explanation on this one. We simply need to check if each number less than 1,000 is a multiple of 3, 5, or both, and if so, add it to a running total. The *trick* with this problem is if your program logic uses two if-statements to check divisble by 3 and divisible by 5. In this case, a number such as 30 (divisible by both 3 and 5) would get counted twice.

###PE2
Generating Fibonacci numbers is easy:

```
F(n) = F(n-1) + F(n-2)
```

For this problem we simply generate a sequence of Fibonacci numbers starting at 1 and moving up to 4,000,000. After a number is generated, check if it is even and, if so, add it to a running total.
