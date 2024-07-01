def myreverse(l):
  if l == []:
    return l
  else:
    return myreverse(l[1:]) + [l[0]]
l = [1, 2, 3, 4, 5]
reversed_list = myreverse(l)
print(f"Reversed list: {reversed_list}")
