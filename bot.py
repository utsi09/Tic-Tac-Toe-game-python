from player import player

class bot(player):
    def __init__(self, board, symbol="B", is_human=False):
        super().__init__(board,symbol, is_human)

    def move_bot(self):
        n = self.board.size  # 보드 크기 (3)
        
        # 플레이어(1)의 두 개 연속 방어
        for i in range(n):
            for j in range(n):
                if self.board.board[i,j] == 1:
                    # 세로 확인
                    if i+2 < n and self.board.board[i+1,j] == 1 and self.board.board[i+2,j] == 0:
                        self.board.board[i+2,j] = 2
                        self.marker.append((i+2,j))
                        return
                    # 가로 확인
                    if j+2 < n and self.board.board[i,j+1] == 1 and self.board.board[i,j+2] == 0:
                        self.board.board[i,j+2] = 2
                        self.marker.append((i,j+2))
                        return

        # 봇(2)의 두 개 연속 승리 시도
        for i in range(n):
            for j in range(n):
                if self.board.board[i,j] == 2:
                    if i+2 < n and self.board.board[i+1,j] == 2 and self.board.board[i+2,j] == 0:
                        self.board.board[i+2,j] = 2
                        self.marker.append((i+2,j))
                        return
                    if j+2 < n and self.board.board[i,j+1] == 2 and self.board.board[i,j+2] == 0:
                        self.board.board[i,j+2] = 2
                        self.marker.append((i,j+2))
                        return

        # 중앙 자리 선호
        if self.board.board[1,1] == 0:
            self.board.board[1,1] = 2
            self.marker.append((1,1))
            return

        # 그 외 빈자리 아무 데나 두기
        for i in range(n):
            for j in range(n):
                if self.board.board[i,j] == 0:
                    self.board.board[i,j] = 2
                    self.marker.append((i,j))
                    return