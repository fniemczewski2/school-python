# Franciszek Niemczewski 3C
def findleaders(arr): # definition of the function for finding leaders
	
    # last element of an array is always leader 
    arrlen = len(arr); # asigning lenght of the array to the variable arrlen
    leader = arr[arrlen-1]; # asigning last element (leader) to the variable leader
    print("Leaders: ") # printing "Leaders: "
    print(leader) # printing current leader (the last element of the array)

    for i in range(arrlen-2, -1, -1): # for loop is finding leaders in other elements of the array; iteration by range (start_value, end_value, step)
        if (arr[i] > leader): # checking if the curent number is greater than the previous leader (is the current number a leader)
            leader = arr[i]; # asigning current element (detected as leader) to the variable leader
            print(leader) # print the leader 
			
arr1 = [ 12, 9, 7, 14, 8, 6, 3] # the first array
print("First array", arr1) # printing "First array" and all the elements of the array
findleaders(arr1) # calling the function

arr2 = [ 8, 23, 19, 21, 15, 6, 11] # the second array
print("Second array", arr2) # printing "Second array" and all the elements of the array
findleaders(arr2) # calling the function

arr3 = [ 55, 67, 71, 57, 51, 63, 38] # the third array
print("Third array", arr3) # printing "Third array" and all the elements of the array
findleaders(arr3) # calling the function

arr4 = [ 21, 58, 44, 14, 51, 36, 23] # the fourth array
print("Fourth array", arr4) # printing "Fourth array" and all the elements of the array
findleaders(arr4) # calling the function
