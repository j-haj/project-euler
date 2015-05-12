// PE1: Find the sum of all multiples of 3 or 5 below 1000

/**
 * @function isMultipleOf3Or5
 * @abstract Returns true if given number is a multipel of 3 or 5
 * @param n
 *  Number to determine multiple of 3 or 5
 * @returns True or false depending on input
 */
function isMultipleOf3Or5(n) {
  if ((n % 3 === 0) || (n % 5 === 0)) {
    return true
  }
  return false
}

/**
 * @function sumMultiplesLessThanN
 * @abstract Sums multiples of 3 and 5, less than n
 * @param n
 *    The limit on the summation
 * @returns The sum of all multiples
 */
function sumMultiplesLessThanN(n) {
  var total = 0
  for (i = 1; i < 1000; i++) {
    if (isMultipleOf3Or5(i)) {
      total += i
    }
  }
  return total
}

debug(sumMultiplesLessThanN(1000))
