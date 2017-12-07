def calculateRowDiff(row):
  return max(row) - min(row)

def calculateChecksum(matrix):
  return sum([calculateRowDiff(row) for row in matrix if row])

if __name__ == "__main__":
  inputFile = open("input.txt", "r")
  matrix = []
  for line in inputFile:
    row = []
    for elem in line.split():
      row.append(int(elem))
    matrix.append(row)
  print(calculateChecksum(matrix))

