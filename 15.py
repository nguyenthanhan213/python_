print("0~100 までの 値(整数値) を２ つ入力してください")
x = int(input("1つ目の値:"))
y = int(input("2つ目の値:"))
if x==y:
  print("同じ値です")
else:
  print("値が大きいのは{}です。".format(max([x,y])))