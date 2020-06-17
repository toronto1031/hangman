# -*- coding: utf-8 -*-

import random

def hangman():
  word_list = ["Python", "Java", "computer", "hacker", "painter"]
  random_number = random.randint(0,4)
  word = word_list[random_number]
  wrong = 0
  stages = ["",
            "___________      ",
            "|        |       ",
            "|        |       ",
            "|        O       ",
            "|      / | \     ",
            "|       / \      ",
            "|                "
              ]
  rletters = list(word)
  board = ["__"] * len(word)
  win = False
  print("ハングマンへようこそ！")
  while wrong < len(stages) -1:
    print("\n")
    msg = "1文字を予想してね"
    char = input(msg)
    if char in rletters:
      cind = rletters.index(char)  #入力された文字が何番目にあるか取得
      board[cind] = char   #boardの"__"を置き換える
      rletters[cind] = '$'  #indexは最初に見つけた要素のインデックス値を返す。同じ文字が二つあると不具合が起きるため置き換えて防ぐ
    else:
      wrong += 1
    print(" ".join(board))  #空白追加
    e = wrong + 1
    print("\n".join(stages[0:e]))  #スライスで取り出したものに改行を加えて表示。なのでステージの最初は空白にしている。0を表示するから
    if "__" not in board:
      print("あなたの勝ち")
      print(" ".join(board))
      win = True
      break
  if not win:
    print("\n".join(stages[0:wrong+1]))
    print("あなたの負け。正解は{}.".format(word))

hangman()
