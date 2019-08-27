class Queens (object):
  # initialize the board
  def __init__ (self, n = 8, numOfBoards = 0):
    self.board = []
    self.n = n
    self.numOfBoards = numOfBoards
    for i in range (self.n):
      row = []
      for j in range (self.n):
        row.append ('*')
      self.board.append (row)

  # print the board
  def print_board (self):
    for i in range (self.n):
      for j in range (self.n):
        print (self.board[i][j], end = ' ')
      print ()

  # check if no queen captures another
  def is_valid (self, row, col):
    for i in range (self.n):
      if (self.board[row][i] == 'Q' or self.board[i][col] == 'Q'):
        return False
    for i in range (self.n):
      for j in range (self.n):
        row_diff = abs (row - i)
        col_diff = abs (col - j)
        if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
          return False
    return True

  # do a recursive backtracking solution
  def recursive_solve (self, col):
    if (col == self.n):
        self.numOfBoards += 1
    else:
      for i in range (self.n):
        if (self.is_valid(i, col)):
          self.board[i][col] = 'Q'
          self.recursive_solve(col + 1)
          self.board[i][col] = '*'
      return False

  # if the problem has a solution print the board
  def solve (self):
    memo = [0]
    self.recursive_solve(0)
    print()
    print("Number of solutions: ", self.numOfBoards)

class Memo(Queens):

    def __init__(self, Q):
        self.Q = Queens
        self.memo = {}
    def __call__(self, args):
        if not args in self.Q(args):
            self.memo[args] = self.Q(args)
        return self.memo[args]
          

def main():

    n = int(input("Enter the size of the board: "))
    while n < 1 or n > 16:
        n = int(input("Enter the size of the board: "))
    
    game = Queens(n)
    game2 = Memo(n)
    game2.solve()

main()
    

    
