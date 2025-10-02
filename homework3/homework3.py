# 3.1 Say Goodbye
def say_goodbye(name):
    print("Goodbye, " + name)

# 3.2 Area of a Circle
def circle_area(rad):
    print((rad**2)*3.14)

# 4.1 Subtract, Multiply, and Divide
def subtract(a, b):
    return(a - b)
def multiply(a, b):
    return(a * b)
def divide(a, b):
    return(a / b)

# 5.1 What Should I Wear?
def what_to_wear(temps):
    minmax = (min(temps), max(temps))
    return(minmax)

# 5.2 Check if it's the Weekend
def is_weekend(daynum):
    return (daynum > 5)

# 5.3 Fuel Efficiency Calculator
def fuel_calc(dist, fuel):
    return(dist/fuel)

# 5.4 Secret Code
def encryption(num):
    last_value = num % 10
    other_values = num // 10
    return (str(last_value) + str(other_values))

# 6.1 Oski Stole Your Power
def power_without_operators(x, y):
    total = x
    for i in range(y-1):
        total *= x
    return total

# 6.2 Min & Max with Loops!
# 6.2.1 For Loops
def for_min(numlist):
    lowest = numlist[0]
    for num in numlist:
        if lowest > num:
            lowest = num
    return lowest
def for_max(numlist):
    lowest = numlist[0]
    for num in numlist:
        if lowest < num:
            lowest = num
    return lowest
# 6.2.2 While Loops
def while_max(numlist):
    lowest = numlist[0]
    counter = len(numlist)-1
    while (counter > 0):
        if lowest < numlist[counter]:
            lowest = numlist[counter]
        counter -= 1
    return lowest
def while_min(numlist):
    lowest = numlist[0]
    counter = len(numlist)-1
    while (counter > 0):
        if lowest > numlist[counter]:
            lowest = numlist[counter]
        counter -= 1
    return lowest

# 6.3 Calculate the Sum
def sum_of_digits(num):
    sum = 0
    new_num = num
    while (new_num > 0):
        last_value = new_num % 10
        sum += last_value
        new_num = new_num // 10
    return sum
