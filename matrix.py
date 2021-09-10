class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [row.split() for row in matrix_string.splitlines()]

    def row(self, index):
        return [int(n) for n in self.matrix[index -1]]

    def column(self, index):
        return [int(row[index - 1]) for row in self.matrix]


def main():
    string = "9 8 5\n6 5 4\n0 1 9"
    m = Matrix(string)
if __name__=="__main__":
    main()