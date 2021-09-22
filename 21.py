kokugo = int(input("国語の点数"))
sugaku = int(input("数学の点数"))
eigo = int(input("英語の点数"))
sum = kokugo + sugaku + eigo
if sum >=230:
  print("合格です")
elif sum >=210 and (kokugo>=85 or sugaku>=85 or eigo>=85  ):
  print("補講対象")
else:
  print("不合格です")
