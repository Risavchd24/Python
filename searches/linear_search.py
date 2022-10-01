def linear_search(arr,x): #linear search function #
    temp = 0              # in case the number is not in the sequence it will help #
    index = []            # in case the number occurs more than once than it will store those indices #
    for i,val in enumerate(arr):   # iterating the array #
        if val == x:                # checking if the iterated value is equal to the number to be searched #
           index.append(i)          # if found the position will be store in this array #
           temp = 1       
    
    return index,temp                # returning the index array #

print("ENTER THE ELEMENTS OF THE SEQUENCE SEPARATED BY SPACE:")  # asking the user to get the sequence #
arr = [int(x) for x in input().split()]                           # storing the elements in the array #
y = int(input("ENTER THE NUMBER TO BE SEARCHED :"))             # asking the user the value to be searched #
i,t = linear_search(arr,y)                                        # calling the linear search function #
if t == 1:                                                 # if the element occurs then we print the index or indices depending upon the frequency #
    if len(i) == 1:                                        # checking the frequency of occurence #
       print("NUMER FOUND AT INDEX {}" .format(i))         # printing the indices at which the number occur #
    else :                                                            
       print("NUMBER FOUND AT {} INDICES :".format(len(i)))  # if number found at one index then this print statement works #
       for k in list(range(len(i))):                       
           print(i[k])
           
elif t != 1:
    print("NUMBER NOT FOUND IN THE GIVEN SEQUENCE")                  # if number not found then this statement will work #



