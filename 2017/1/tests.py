import unittest
import captcha

givenExamples = [
  ("1122", 3),
  ("1111", 4),
  ("1234", 0),
  ("91212129", 9)
]

class TestCalculateDuplicatesSum(unittest.TestCase):
  def testGivenExamples(self):
    for ex in givenExamples:
      line = ex[0]
      calc = captcha.calculateDuplicatesSum(line)
      self.assertEqual(calc, ex[1])

if __name__ == "__main__":
  unittest.main()
