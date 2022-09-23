count_p = 0
count_n = 0
total = 0
while True:
   number = int(input("Enter an integer, the input ends if it is 0: "))
   if number == 0:  break
   else:
       total += number
       if number > 0:
           count_p+= 1
       elif number < 0:
           count_n+= 1

print("The number of positives is: " + str(count_p))
print("The number of negatives is: " + str(count_n))
print("The total is: " + str(total))
print("The average is: " + str(total / (count_p + count_n)))
