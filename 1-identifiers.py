import sys

MAX_PURCHASE = int(sys.argv[1])

i = 0
total = 0
purchase = [1500, 100, 10, 50]
for each in purchase:
  total = total+purchase[i]
  i = i+1
if total <= MAX_PURCHASE:
  print(total)
