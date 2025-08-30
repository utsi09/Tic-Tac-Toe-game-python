import numpy as np
from datetime import datetime

coin = 1

class game:
    def __init__(self,human,ai,board):
        self.human = human
        self.ai = ai
        self.board = board
        self.current_player = human

    def switch_player(self):
        self.current_player = self.ai if self.current_player == self.human else self.human

    def check_winner(self):
        global coin
        b = self.board.board        # 행 검사
        for row in b:
            if np.all(row == 1):
                print("Player A wins!")
                return 1
            elif np.all(row == 2):
                print("Player B wins!")
                return 2

        # 열 검사
        for col in b.T:
            if np.all(col == 1):
                print("Player A wins!")
                return 1
            elif np.all(col == 2):
                print("Player B wins!")
                return 2
        # 대각선 검사
        if np.all(np.diag(b) == 1) or np.all(np.diag(np.fliplr(b)) == 1):
            print("Player A wins!")
            return 1
        elif np.all(np.diag(b) == 2) or np.all(np.diag(np.fliplr(b)) == 2):
            print("Player B wins!")
            return 2
        
        #무승부 검사
        if np.all( b!=0):
            return 0



    def show_board(self):
        for i in range(self.board.size):
            for j in range(self.board.size):
                if (i, j) in self.human.marker:
                    print("1", end=" ")
                elif (i, j) in self.ai.marker:
                    print("2", end=" ")
                else:
                    print(".", end=" ")
            print()
        #self.human.marker

    def game_manager(self):
        global coin
        if (p := self.check_winner()) == 1: # 위너가 1이면
            self.show_board()
            return 1
        elif p == 2:
            self.show_board()   
            return 2
        elif p == 0:
            #self.show_board()
            coin=0
            return 0

    def save_result(self,winner):
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        with open("result.txt","a") as f: 
            f.write(f"{current_time} - {winner} wins \n")


    def run(self):
        global coin
        while True:
            if self.current_player.is_human:
                # 인간 플레이어의 차례
                self.show_board()
                #self.current_player.show_selectable()
                tmp = int(input("선택할 위치를 입력하세요 (1-9): "))-1
                if not self.current_player.inspect_place(tmp):
                    continue
                self.current_player.select_num_to_marker(tmp)
                self.current_player.marker.append(self.current_player.select_num)
                if self.game_manager(): #1이나 2 반환되면 트루
                    print("다시 시작하겠습니까? (y/n)")
                    if input().lower() != 'y':
                        self.save_result(self.current_player.symbol)
                        print("게임을 종료합니다.")
                        coin=0
                        return
                    else: # 지금 함수 내부에서 초기화하는데 빠져나가서 루프로 도는거로 바꾸기
                        return
                elif self.game_manager()==0:
                    print("무승부입니다")
                    coin=0
                    return
                #self.current_player.move_player()
                self.switch_player()
            else:
                # AI 플레이어의 차례
                self.current_player.move_bot()
                if self.game_manager():
                    print("다시 시작하겠습니까? (y/n)")
                    if input().lower() != 'y':
                        self.save_result(self.current_player.symbol)
                        print("게임을 종료합니다.")
                        coin = 0
                        break
                elif self.game_manager()==0:
                    print("무승부입니다")
                    coin=0
                    return
                self.switch_player()

class board:
    def __init__(self,size=3):
        self.size = size
        self.board = np.zeros((size,size),dtype=int) # 보드 초기화

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
        #print(f"선택한 위치: {col}, {row}")
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
                    #print(f"{cnt} ",end="")
                    cnt += 1
            #print("")

    def move_player(self):
        # 인간 플레이어의 움직임 로직을 구현
        pass

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

def init():
    game_board = board()
    human = player(game_board)
    ai = bot(game_board)
    game_instance = game(human,ai, game_board)
    game_instance.run()

def main():
    global coin
    while(coin == 1):
        init()



if __name__ == "__main__":
    main()
