class player:
    def __init__(self, board, symbol = "A", is_human = True):
        self.marker = [] #지금까지 둔 마커 위치들 (3x3)
        self.symbol = symbol # A, B
        self.is_human = is_human 
        self.board = board
        self.select_num = 0

    def select_num_to_marker(self,num):
        self.select_num = num
        col = int(num / 3) # 행
        row = (num % 3)
        self.marker.append((col, row))
        self.board.board[col, row] = 1 if self.is_human else 2

    def inspect_place(self, num):
        if num < 0 or num >= self.board.size**2:
            print("보드 범위를 벗어났습니다.")
            return False

        col = int(num / 3) # 행
        row = (num % 3)
        if (col, row) in self.marker or self.board.board[col, row] != 0:
            print("이미 선택된 위치입니다.")
            return False
        return True

    def show_selectable(self):
        cnt = 1
        for i in range(0,3):
            for j in range(0,3):
                    cnt += 1
