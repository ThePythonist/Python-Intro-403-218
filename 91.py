def main():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def table():
        print('''
         {} | {} | {}
        -----------
         {} | {} | {}
        -----------
         {} | {} | {}
        '''.format(
            board[0],
            board[1],
            board[2],
            board[3],
            board[4],
            board[5],
            board[6],
            board[7],
            board[8],
        ))

    def choice1():
        while True:
            n = input("Player 1 choose : ")
            try:
                n = int(n)
                n -= 1
                # if 0 <= n <= 8:
                if n in range(0, 9):
                    return n
                else:
                    print("Thats not on the board. Try again")
            except ValueError:
                print("That's not a number. Try again")

    def choice2():
        while True:
            n = input("Player 2 choose : ")
            try:
                n = int(n)
                n -= 1
                # if 0 <= n <= 8:
                if n in range(0, 9):
                    return n
                else:
                    print("Thats not on the board. Try again")
            except ValueError:
                print("That's not a number. Try again")

    def move1():
        pass

    def move2():
        pass

    def check_board():
        pass
