def calculateRowDiff(row):
  return max(row) - min(row)

def calculateChecksum(matrix):
  return sum([calculateRowDiff(row) for row in matrix if row])

if __name__ == "__main__":
  inputFile = open("input.txt", "r")
  matrix = [map(int, line.split()) for line in inputFile]
  inputFile.close()
  print(calculateChecksum(matrix))

