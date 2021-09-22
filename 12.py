nen = int(input("西暦年を入力してください。"))
if nen%4==0:
  if nen%100==0 and nen%400==0:
    print("閏年です。")
  else:
    print("平年です")
