def checkmate(board):
    rows = [r for r in board.split('\n') if r]
    grid = []
    
    for row in rows:
        if (len(rows) != len(row)):
            return
        grid.append(list(row))

    if len(grid) == 0:
        return

    king_count = 0
    k_row = -1
    k_col = -1

    for i in range(len(rows)):
            for j in range(len(rows)):
                if grid[i][j] == 'K':
                    king_count += 1
                    k_row = i
                    k_col = j

    if king_count != 1:
        return

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            piece = grid[r][c]
            if piece != '.' and piece != 'K':

                # P
                if piece == 'P':
                    if (r == k_row + 1 or r == k_row - 1):
                        if c == k_col - 1 or c == k_col + 1:
                            print("Success")
                            return

                # R or Q
                if piece == 'R' or piece == 'Q':
                    if r == k_row or c == k_col:
                        is_blocked = False

                        step_r = 0
                        if k_row > r: step_r = 1
                        elif k_row < r: step_r = -1
                        step_c = 0
                        if k_col > c: step_c = 1
                        elif k_col < c: step_c = -1
                    
                        curr_r = r + step_r
                        curr_c = c + step_c
                        
                        while curr_r != k_row or curr_c != k_col:
                            if grid[curr_r][curr_c] != '.':
                                is_blocked = True
                                break
                            curr_r += step_r
                            curr_c += step_c
                        
                        if is_blocked == False:
                            print("Success")
                            return

                # B or Q
                if piece == 'B' or piece == 'Q':
                    diff_r = k_row - r
                    if diff_r < 0: diff_r = -diff_r
                    
                    diff_c = k_col - c
                    if diff_c < 0: diff_c = -diff_c
                    
                    if diff_r == diff_c:
                        is_blocked = False
                        
                        step_r = 1
                        if k_row < r: step_r = -1
                        step_c = 1
                        if k_col < c: step_c = -1
                        
                        curr_r = r + step_r
                        curr_c = c + step_c
                        
                        while curr_r != k_row or curr_c != k_col:
                            if grid[curr_r][curr_c] != '.':
                                is_blocked = True
                                break
                            curr_r += step_r
                            curr_c += step_c
                            
                        if is_blocked == False:
                            print("Success")
                            return

    print("Fail")