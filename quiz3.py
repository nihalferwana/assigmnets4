x = input("First number : ")
y = input("Second number : ")
z = input("Third number : ")
if x < y and x < z:
 min = x
elif y < x and y< z:
 min = y
else:
 min = z
print ("The smallest is ", min)
