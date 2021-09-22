print("0~100 までの 得点(整数値) を２ つ入力してください")
x = int(input("1つ目の得点:"))
y = int(input("2つ目の得点:"))
if x >= 80 and y >= 80:
  print("合格です")
elif x >= 80 or y >= 80:
  print("補欠合格です")
else:
  print("不合格です")