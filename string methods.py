#casefold
str="ß'"
res= str.casefold()
print(res)#it will  return the given str to lowercase but the main reason for using
#this it looks like a translator if we give a input in any other language it can convert
#to english  and return a value




#$str.center(width[, fillchar])

#Return centered in a string of length width.
#Padding is done using the specified fillchar (default is an ASCII space). The original string is returned if width is less than or equal to len(s).
#(CENTER)
str="welcome"
length1=len(str)
sa=str.center(24,'*')#here the first parameter is length of a padding string and second parameters is fillchar it represent  ..what the data can be add to the pading string before and after
if(sa!=length1):
    print("the res is"+sa)
else:
    print("wrong")

#........string.center(length[, fillchar])
#Parameters:
#length: length of the string after padding with the characters.
#fillchar:(optional) characters which needs to be padded. 
#If it's not provided, space is taken as default argument.
#Returns:
#returns a string padded with specified fillchar and it doesn't modify# 
#the original string........>>>>>?//
#ENDSWITH
str="wlcome all"
print(str.endswith('e',0,1))#here the function act as boolean value ..if the given string end with ..given parameter or character  ,,it returns true
#otherwise false   ..it take two parameters suffix value and positions
#here the char(e) present in the given position ...so it will return false


