num=int(input("Enter a number: "))
while True:
  numstr=str(num)
  reversed_num = "".join(reversed(numstr))
  if reversed_num==numstr:
    break
  rev_str=int(reversed_num)
  num+=rev_str
  print(num)
  