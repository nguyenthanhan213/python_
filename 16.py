print("整数値を３つ入力してください")
x = int(input("1つ目の値:"))
y = int(input("2つ目の値:"))
z = int(input("3つ目の値:"))
if x==y==z:
  print("同じ値です")
else:
  print("最大の値は{}です。".format(max([x,y,z])))