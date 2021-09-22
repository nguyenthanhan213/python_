print("0~100 までの 得点(整数値) を２ つ入力してください")
x = int(input("1つ目の得点:"))
y = int(input("2つ目の得点:"))
if x==y:
  print("どちらも{}点です".format(x))
else:
  x,y = sorted([x,y], reverse=True)
  print("{}点、{}点です。".format(x,y))