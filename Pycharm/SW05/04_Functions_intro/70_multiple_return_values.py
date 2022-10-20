# 70_multiple_return_values.py

# There are situations where it makes sense for a function to return more than one value.
# It's possible in Python! Not in Java!

def sum_and_mult_return(i):
    sum = 0
    for j in range(1,i+1):
        sum = sum + j
    mult = 1
    for y in range(1,i+1):
        mult = mult * y
    return (sum, mult)

while True:
    x = int(input("Your number: "))
    if x <=0:
        break
    (mysum, mymult) = sum_and_mult_return(x)
    print("The sum from 1 to ", x, " is ", mysum)
    print("The multiplication from 1 to ", x, " is ", mymult)

