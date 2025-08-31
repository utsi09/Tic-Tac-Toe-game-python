import numpy as np
from datetime import datetime
from player import player 
from bot import bot
from board import board
import config

class game:
    def __init__(self,human,ai,board):
        self.human = human
        self.ai = ai
        self.board = board
        self.current_player = human

    def switch_player(self):
        self.current_player = self.ai if self.current_player == self.human else self.human

    def check_winner(self):
        b = self.board.board
        # 행 검사
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
        if (p := self.check_winner()) == 1: # 위너가 1이면
            self.show_board()
            return 1
        elif p == 2:
            self.show_board()   
            return 2
        elif p == 0:
            #self.show_board()
            config.coin=0
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
                        config.coin=0
                        return
                    else: # 지금 함수 내부에서 초기화하는데 빠져나가서 루프로 도는거로 바꾸기
                        return
                elif self.game_manager()==0:
                    print("무승부입니다")
                    config.coin=0
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
                        config.coin=0
                        break
                elif self.game_manager()==0:
                    print("무승부입니다")
                    config.coin=0
                    return
                self.switch_player()

def init():
    game_board = board()
    human = player(game_board)
    ai = bot(game_board)
    game_instance = game(human,ai, game_board)
    game_instance.run()




