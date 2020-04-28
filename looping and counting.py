#looping and counting on strings
def count(text, aChar):#parameters text ,achar
    lettercount = 0
    for j in text:
        if j == aChar:#check if the character found in the string ..it is equal to given character
            lettercount = lettercount + 1
    return lettercount

print(count("banana","n"))#arguments banana,n

#
#he function count takes a string as its parameter. The for statement iterates through each character in the string and
#checks to see if the character is equal to the value of aChar. If so, the counting variable, lettercount, is incremented by one.
#When all characters have been processed, the lettercount is returned.
a = [1, 2, 3, 4, 5] 

# printing the list using loop 
for x in range(0,3): 
	print(a[1])
