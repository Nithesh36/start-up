str="Apple"
#first thing uppercase or can always have first priority
if(str>"dood"):
    print("the {}comes after the dood")#here the conditon fals..because the given str is upper case
    #so  we use the >operator to check the value is upper or lower ..based on this we decide the str can came before or after
elif(str<"dood"):
     print(f"the {str}comes before the dood")#lessthan mean str came before the next string
else:
    print("all are same")
