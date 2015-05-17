// Solution to PE2 - find the sum of the even-valued Fibonacci numbers less than
// 4,000,000
// Solution: 4,613,732

object PE2 {
  def main(args: Array[String]) = {
    println("Answer: " + evenFibSum(4000000, 1, 1))
  }

  def evenFibSum(limit: Int, a: Int, b: Int): Int = {
    val next = a + b
    val prev = b
    if (next > limit) { 0 }
    else {
      if (next % 2 == 0) {
        next + evenFibSum(limit, prev, next)
      } else {
        evenFibSum(limit, prev, next)
      }
    }
  }
}
