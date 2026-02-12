from checkmate import checkmate

def main():
    board = """\
R...
.K..
....
....\
"""
    checkmate(board)

    board2 = """\
Q...
.K..
....
....
\
"""
    checkmate(board2)

if __name__ == "__main__":
    main()