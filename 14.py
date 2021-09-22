x = int(input("0~100 までの 得点(整数値)を入力してください"))
if x >100 and x<0:
  print("入力値は不正です")
if x == 100:
  print('満点合格です')
elif x>=60 and x<100:
  print('合格です')
elif x<60: 
  print("不合格です。")
