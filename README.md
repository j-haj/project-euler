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
C/C++ | 3/516
JavaScript | 3/516

##Solutions
###Solution Index
[PE1](https://github.com/j-haj/project-euler#pe1)

[PE2](https://github.com/j-haj/project-euler#pe2)

[PE3](https://github.com/j-haj/project-euler#pe3)

###PE1
There is not much need for explanation on this one. We simply need to check if each number less than 1,000 is a multiple of 3, 5, or both, and if so, add it to a running total. The *trick* with this problem is if your program logic uses two if-statements to check divisble by 3 and divisible by 5. In this case, a number such as 30 (divisible by both 3 and 5) would get counted twice.

###PE2
Generating Fibonacci numbers is easy:

```
F(n) = F(n-1) + F(n-2)
```

For this problem we simply generate a sequence of Fibonacci numbers starting at 1 and moving up to 4,000,000. After a number is generated, check if it is even and, if so, add it to a running total.

###PE3
The naive approach to this problem is to count up from 2 to just above the square root of the given number, consider whether the current number is prime and, if it is, see if it is a factor of the number in question. While this will certainly solve the problem, it can be a non-trivial task, especially since at each step we need to test whether a number is prime or not.

A simpler approach is to find the smallest factor (greater than 1!) of the number in question and divide that factor out completely. For example, the smallest factor for the number 8 is 2 (2^3 = 8). If we divide 8 by 2 we are left with 4. Dividing 4 by 2 we are left with 2, etc. until we hit one. In this case we have found the prime decomposition of 8. If we look at 26 on the other hand we find that we can divide 26 by 2 once and are left with 13. Working our way up the chain we realize 13 must be prime because it has no other factors (aside from itself and one, of course). In general, if we extend this approach to any number, we will keep hitting successive primes as we move up our "factor" sequence. As long as we completely divide out the lower factors (starting at 2), we will move along the sequence of the given number's prime decomposition until we hit the end point, which is the given number's largest prime factor.

This approach can be implemented using tail-recursion.
