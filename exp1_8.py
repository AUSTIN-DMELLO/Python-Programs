L=[1,2,'apple',[12,'orange']]
print(L)
L[-1][-1]="pineapple"
print(L)
if 'apple' in L:
    print("Apple is present in list.")
else:
    print("Apple is not present in list.")