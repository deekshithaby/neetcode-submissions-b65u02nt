class Solution:
    def isValidSudoku(self, board):
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                elem = board[i][j]

                if elem == ".":
                    continue
                
                box_index=(i//3)*3 + (j//3)

                if (elem in rows[i] or elem in cols[j] or elem in boxes[box_index]):
                   return False

                rows[i].add(elem)
                cols[j].add(elem)
                boxes[box_index].add(elem)


        return True

