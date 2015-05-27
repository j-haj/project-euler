// PE3 - find the largest prime factor of 600851475143
// Solution: 6857

import scala.math.BigInt._

object PE3 {
  def main(args: Array[String]) = {
    println("Answer: " + largestPrimeFactor(600851475143L,2))
  }

  def largestPrimeFactor(n: BigInt, x: BigInt): BigInt = {
    if (n == x) n
    else {
      if (n % x == 0) largestPrimeFactor(n/x, x)
      else largestPrimeFactor(n, x+1)
    }
  }

}
