
def my_func(strlist):
   p = len(strlist)
    #range following ordered 
   for i in range(p):   # sequence/Iterate each element in the list
        for j in range(i + 1, p): # Compare each element with the all
                if strlist[i] > strlist[j]:   # If the current element is greater than the next one, swap for 1st itteration.
                 strlist[j], strlist[i]= strlist[i], strlist[j] 
 
str_list = ["cello", "sorld", "uearn", "dddas", "nhuij", "djkks","jhhh","f8ujww"]
my_func(str_list)
 
print("Sorted List:", str_list)