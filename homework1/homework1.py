# --- Variables and Data Types ---

a = 10
print(a)
print(type(a)) # a is an integer, so whole number

b = 1.5
print(b)
print(type(a)) # b is a float, so a number with fractional value

c = 3j
print(c)
print(type(c)) # c is a complex, so it represents a complex number

d = "hello"
print(d)
print(type(d)) # d is a string, so it is text

e = [1, 2, 3]
print(e)
print(type(e)) # e is a list, so it stores a series of different/multiple data types (in this case integers)

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary, so it stores data in key-value pairs like a dictionary with words and their definitions

g = (1,2)
print(g)
print(type(g)) # g is a tuple, so a list that cannot be changed

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # e is a list, so it stores a series of different/multiple data types (in this case strings)

i = True
print(i)
print(type(i)) # i is a boolean, so it stores true/false data

j = None
print(j)
print(type(j)) # j is a NoneType, so it is an object with no value

k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list, so it stores a series of different/multiple data types (in this case a boolean, string, and integer)

l = str(14)
print(l)
print(type(l)) # l is an string, in this case a number was put into the function str(), which turned it into a string

m = 1e4
print(m)
print(type(m)) # m is a float, so it is a number with a decimal point, except it was defined with scientific notation

"""
1. I found 9 data types
2. integer, float, string, list, dictionary, Nonetype, tuple, boolean, and complex
3. float b&m, list - e&h&k, string - d&l
4. L was a string because we turned the number 1 into a string with the str() function
5. Bytes
"""

n = b'Hello'
print(n)
print(type(n)) # n is part of the bytes type, which encodes the string given into ASCII.

# --- Booleans ---

print(10 > 9) # The result was True, because 10 is greater than 9
print(10 == 9) # The result was False, because 10 isn't equal to 9
print(10 <= 9) # The result was False, because 10 isn't less than or equal to 9
print(bool("abc")) # The result was True, because there is data in the string
print(bool(123)) # The result was True, because these numbers have a value that isn't zero
print(bool(["apple", "cherry", "banana"])) # The result was True, because there is data in the list.
print(bool(True)) # The result was True, because it is true
print(bool(False)) # The result was False, because it is false
print(bool(0)) # The result was False, because the value is 0
print(bool("")) # The result was False, because the string is empty
print(bool(" ")) # The result was True, because there string isn't empty
print(bool(())) # The result was False, because the paranthesis are empty
print(bool([])) # The result was False, because the brackets are empty
print(bool({})) # The result was False, because the braces are empty
print(bool(True and False)) # The result was False, because both must be true in order to be true
print(bool(True and True)) # The result was True, because both are true
print(bool(False and False)) # The result was False, because both are false
print(bool(True or False)) # The result was True, because at least one is true
print(bool(True or True)) # The result was True, because at least one is true
print(bool(False or False)) # The result was False, because neither are true
print(bool(not(False))) # The result was True, because true is not false
print(bool(not(True))) # The result was False, because false is not true

"""
1. Except for ones which deal with the literal data types of true or false, if something has data stored in it, it is true. Whereas empty things such as lists are false.
2. That the string "abc" was true, don't really think of strings as true or false 
"""
#3
print(bool(False or True and True)) # This is true because it satisfies the conditions of one or the other being true and both of the 'and' adjacent ones being true

#4
print(bool(True and True and True and True and True and True and True and False)) # They all have to be true, but one isn't

# --- Operators ---

print(10 + 5) # The result was 15, because 10 + 5 = 15
print(10 - 5) # The result was 5, because 10 - 5 = 5
print(2 * 4) # The result was 8, because 2 * 4 = 8
print(6 / 3) # The result was 2.0, because 6 / 3 = 2, and the normal division symbol creates a float 2.0
print(5 % 2) # The result was 1, because the remainder of 5/2 is 1
print(3 ** 2) # The result was 9, because 3 to the power of 2 is 9
print(15 // 2) # The result was 7, because 15 / 2 = 7 with rounding

print(5 == 2) # The result was False, because 5 isn't equal to 2
print(10 != 10) # The result was False, because 10 doesn't not equal 10
print(2 < 5) # The result was True, because 2 is less than 5
print(12 > 5) # The result was True, because 12 is greater than 5
print(5 <= 6) # The result was True, because 5 is less than 6
print(1 >= 10) # The result was False, because 1 isn't greater than 10

x = 5
print(x) # The result was 5, because x = 5
x += 5
print(x) # The result was 10, because 5+5=10
x -= 4
print(x) # The result was 6, because 10-4 is 6
x *= 3
print(x) # The result was 18, because 6*3 is 18

"""
1. and returns true only if both arguements are true.
- (True and True) = True
- (False and True) = False
2. or returns true if either arguements are true.
- (True or False) = True
- (False or False) = False
3. not() returns the opposite of its arguement
- not(False) = True
- not(True) = False

1. / returns float division results, // returns rounded integer results
2. % returns the remainder of division, // returns the quotient
3. You would use the modulus (%) operator to do this. So 5 % 4 = 1
4. Assignment operators assign a variable with a value.
"""

# --- Strings ---
my_string = "hello"
print(my_string) # This prints hello
print(my_string[0]) # This prints H
print(my_string[1]) # This prints e
print(my_string[2]) # This prints l
print(my_string[3]) # This prints l
print(my_string[4]) # This prints o
print(my_string[-1]) # This prints o
print(my_string[1:3]) # This prints el
print(my_string[0:5:2]) # This prints hlo
print(len(my_string)) # This prints 5
print(my_string + "goodbye") # This prints hellogoodbye
print(7*my_string) # This prints hellohellohellohellohellohellohello

#1. Slicing means only using certain parts of the string given by a certain step length, so when I did [1:3] and [0:5:2] I was slicing [start:stop:step]
#2
name = "Oski"
print("Hello, my name is", name) # It printed Hello, my name is Oski
#3
name + "Oski"
print(f"Hello, my name is {name}") # It printed Hello, my name is Oski
#4 The difference was f-strings allow expression to be embedded in Strings with braces, whereas normally they can only be added on with a space automatically applied.

# --- Terminal Commands ---
"""
cd
- Changes directories. Use it to move from one folder to another
- Example: cd Desktop
ls
- Lists directories. Shows all non-hidden directories
- Example: ls
ls -a
- Lists directories. Shows all directories
- Example: ls -a
mkdir
- Makes a directory. Creates a new directory where you are, or you can specify path
- Example: mkdir homework1
cat
- Concatenate. Combines files into one, also shows content of file
- Example: cat file1.txt file2.txt > file3.txt
- Example: cat file1.txt (shows file)
pwd
- Prints the working directory
- Example: pwd
cd ..
- Changes directory to the parent directory
- Example: cd ..
cd .
- Changes directory to the current working directory, so really doesn't do much
- Example: cd .
cd ~
- Changes directory to your home directory
- Example: cd ~
cp
- Copies file/directory to another file/directory
- Example: cp file1.txt file2.txt
mv
- Moves files from one location to another
- Example: mv oldfilename.txt newfilename.txt
rm
- Removes a file
- Example rm file1.txt
clear
- Clears terminal of visible content
- Example: clear
grep
- Searches files for a specific string
- Example: grep "a string" file1.txt

1. The 3 other commands not present:
- open: Opens a file
- touch: Creates a blank file
- exit: Closes the terminal session
2. The difference between ls and ls -a is that ls -a shows hidden files while ls doesn't
3. A hidden file is a configuration file, system files, and the special entries representing the current and parent directory
4. The 3 other flags:
- -L for pwd, displays the logical working directory
- -P for pws, displayes the physical working directory
- -R for rm, removes a directory and all its contents, including nested subdirectories
"""