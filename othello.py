import numpy as np
class Board:
    black = 1
    white = -1
    board_size = 8  
  
    def __init__(self):
        self.cell = np.zeros((board_size,board_size)) # 値が全て0の8行8列の二次元配列を生成
        self.cell[3][3] = self[4][4] = black
        self.cell[3][4] = self[4][3] = white
        
        print(self.cell)

    def turn(self):

# 初期配置設定
# ターン開始
#     if 石を置ける場所が存在する
#         石を置く
#     elif ターン交代後 石を置ける場所が存在する 
#         ターンを交代する
#     else 
#         終了処理

# def 石を置く
#     石を置く場所を選択する
#     if 指定した場所に石が存在する
#         もう一度選択する
#     elif 指定した場所に置いても石をひっくり返せない
#         もう一度選択する
#     else
#         石を置きひっくり返す

# def 石をひっくり返す
#     処理
#     ターンを交代する

# def ターンを交代する
#     処理
#     ターン開始に戻る

# def 終了処理
#     黒と白の数の合計を数え大小を比較する
#     数が多い方を勝者として表示する