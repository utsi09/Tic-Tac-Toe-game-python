import numpy as np

class board:
    def __init__(self,size=3):
        self.size = size
        self.board = np.zeros((size,size),dtype=int) # 보드 초기화