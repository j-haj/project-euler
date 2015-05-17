// PE1: Find sum of all mutiples of 3 or 5 less than 1,000
// Solution: 233168

object PE1 {

  // Main function
  def main(args: Array[String]) = {
    println("Answer:" + sumLessThanN(1000))
  }

  /**
  Sums multiples of the three, five, or both that are less than the passed arguemnt
  */
  def sumLessThanN(n: Int): Int = {
    
    def multipleOf3Or5(n: Int): Boolean = {
      if ((n % 3 == 0) || (n % 5 == 0)) { true }
      else { false }
    }

    if (n == 0) {
      0
    } else {
      if (multipleOf3Or5(n-1)) {
        n-1 + sumLessThanN(n-1)
      } else {
        sumLessThanN(n-1)
      }
    }
  }

}
