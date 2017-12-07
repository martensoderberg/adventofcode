import unittest
import checksum

givenMatrix = [
 [5, 1, 9, 5],
 [7, 5, 3],
 [2, 4, 6, 8]
]

class TestCalculateChecksum(unittest.TestCase):
  def testCalculateRowDiff(self):
    val0 = checksum.calculateRowDiff(givenMatrix[0])
    val1 = checksum.calculateRowDiff(givenMatrix[1])
    val2 = checksum.calculateRowDiff(givenMatrix[2])
    self.assertEquals(val0, 8)
    self.assertEquals(val1, 4)
    self.assertEquals(val2, 6)

  def testCalculateChecksum(self):
    val = checksum.calculateChecksum(givenMatrix)
    self.assertEquals(val, 18)

if __name__ == "__main__":
  unittest.main()
