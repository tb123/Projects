import unittest


def calculate_pi(N):
    """ Uses the Bailey-Borwein-Plouffe formula to calculate Pi to a given number of digits.
    """
    assert(N >= 0 and N <= 11)
    pi = 0.0
    for n in xrange(0, N+1):
        pi += (1/float(16) ** n) * float((4/float(8*n + 1)) - (2/float(8*n + 4)) - (1/float(8*n + 5)) - 1/float(8*n + 6))
    if N > 0:
        return str(pi)[:N+2]
    return str(int(pi))

class CalculatePiTests(unittest.TestCase):
    """ Some tests to check that the basic requirements for this
    problem are satisfied.
    """
    def test_calculate_pi_11N(self):
        """ A basic test to check the correctness of our solution. Correct
        value of Pi is "3.14159265359" according to a highly reliable source
        - a.k.a Google's calculator :-).
        """
        self.assertEquals(calculate_pi(11), "3.14159265359")

    def test_calculate_pi_0N(self):
        """ Tests the 0 case, where we expect an integer result only.
        """
        self.assertEquals(calculate_pi(0), "3")

    def test_negative_N_value(self):
        """ Tests that negative N values are not calculated as they can lead
        to zero division errors.
        """
        self.assertRaises(AssertionError, calculate_pi, -1)

if __name__ == "__main__":
    print "Hello! This program calculates Pi to N digits."
    help_text =  "Help: Enter an integer or 'test' to test the program."
    print help_text

    while True:
      inp = raw_input('?> ')
      # Check if the 'test' command was requested
      if inp == 'test':
          unittest.main()
      # Otherwise attempt to convert input to an integer so we can calculate Pi!
      try:
          num_digits = int(inp)
      except ValueError:
          print help_text
          continue

      if num_digits > 11:
          print "We can only calculate up to 11 digits. Please try again!"
          continue
      pi = calculate_pi(num_digits)
      print "The value of pi (rounded to %d digits): %s" % (num_digits, pi)
