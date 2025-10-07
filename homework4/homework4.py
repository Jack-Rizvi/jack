# 3.1 List Operations
fav_foods = ["pizza", "burger", "chicken", "milkshake", "milkshake_2"]
print(fav_foods[1])
fav_foods.append("milkshake_4")
fav_foods.insert(0, "apple")
# Got an error in the following function as I treated the remove() function as the del function, I corrected it by using the del function 
del fav_foods[2]
print(fav_foods)
for food in fav_foods:
    print(food.upper())
new_fav_foods = fav_foods[0::len(fav_foods)]
if new_fav_foods.count("potato") > 0:
    print("A potato!")
else:
    print("No potato!")

# 3.2 Slicing and Striding
# This function wasn't printing at first but I realized that I never passed the arguements through the final print statement, so I added the full arguement list and it worked
numbers = list(range(0,21))
def get_first_15(numbers):
    return numbers[0:15]
print((get_first_15(numbers)))
def get_every_5th(get_first_15):
    return get_first_15[::5]
print(get_every_5th(get_first_15(numbers)))
def reverse_and_stride(get_every_5th):
    temp_list = get_every_5th[::-1]
    return temp_list[::3]
print(reverse_and_stride(get_every_5th(get_first_15(numbers))))

# 3.3 Nested Lists
numbers = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for thing in numbers:
    print(thing[2])
print(numbers[1][1])
numbers.append([10, 11, 12])
# There is probably a more efficient way to do this, but a nested for loop works too
def sum_nested(numbers):
    total = 0
    for list in numbers:
        for thing in list:
            total += thing
    return total

# 3.4 Create a 5x5 List
# This wouldn't store the list correctly for a while and would return an empty list, turns out I was just printing the list without calling the function
loops_5x5 = []
def nested_loops():
    count = 0
    for num1 in range(5):
        sublist1 = []
        for num2 in range(5):
            sublist1.append(count + 1)
            count += 1
        loops_5x5.append(sublist1)
nested_loops()
new_array = loops_5x5
def multiples_of_3(new_array):
    for var in new_array:
        for var2 in var:
            if var2 % 3 == 0:
                var2 = "?"
multiples_of_3(new_array)
def add_not_equal():
    total = 0
    for var in new_array:
        for var2 in var:
            if var2 != "?":
                total += var2
    return total
result = add_not_equal()

# 4.1 Dictionary Operations
ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}
print(ages["Katie"])
ages["Mira"] = 100
ages["Milana"] = 52
del ages["Mariam"]
for entry in ages.items():
    print(entry)