print('Welcome to the Grade Sorter App.') 
a=int(input('What is your first grade (0-100): ')) 
b=int(input('What is your second grade (0-100): ')) 
c=int(input('What is your third grade (0-100): ')) 
d=int(input('What is your fourth grade (0-100): ')) 
L=[a,b,c,d] 
print('Your grades are:',L) 
L.sort(reverse=False) 
print("Your grades from highest to lowest are:",L)
print("Your lowest two grades will now be dropped.") 
DL=L[2:] 
for dropped_grade in L[2:]: 
    print("Removed grade:",dropped_grade)
print("Your remaining grades are:",DL)
HL=max(DL)
print("Nice work! Your highest grade is a",HL)