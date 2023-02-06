num=int(input("Enter a number: "))
for x in range(4):
  numstr=str(num)
  reversed_num = "".join(reversed(numstr))
  rev_str=int(reversed_num)
  num+=rev_str
  print(num)