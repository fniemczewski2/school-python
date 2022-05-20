# Franciszek Niemczewski 3C
def findmajorityhashmap(arr): # definition of the function for finding leaders
	#hashmap

    arrlen = len(arr); # asigning lenght of the array to the variable arrlen
    test = {} # new empty dictionary
    for i in range(arrlen): # iteration through the array
        if arr[i] in test: # checking is there the current element from the array already in the dictionary
            test[arr[i]] += 1 # if there is the current element in the dictionary algoritm icreases the value
        else: # otherwise
            test[arr[i]] = 1 # the algoritm sets the value to 1
    lock = 0 # realy helpful variable, protection against printing "No majority element" 
    for key in test: # iteration through the dictionary
        if test[key] > arrlen / 2: # tlesting if the number of appearances is greater than half of the array
            print("Majority element: ",key) # printing the information about found majority element
            lock = 1 # majority element has been already found
            break # break the loop
    if (lock  == 0): # when the majority element is found, the algorithm sets the value of the variable to 1
        print("No majority element") # printing "No majority element"
			
def findmajorityvoting(arr): # definition of the function for finding leaders
    # Boyer-Moore algoritm

    lenarr = len(arr) # assingning the lenght of the array to the variable lenarr
    maj = 0 # index of the mojority element
    count = 1 # the number of votes for the majority element
    for i in range(lenarr): # iteration through the array
        if arr[maj] == arr[i]: # checking if the current element is equal to majority candidate
            count += 1 # increasing votes by one
        else: # otherwise
            count -= 1 # decreasing votes by one
        if count == 0: # if the are no votes for current candidate
            maj = i # the majority candidate changes
            count = 1 # and there is a one vote for the new majority candidate
    
    final_candidate = arr[maj] # assigning the current candidate as the final candidate to the variable final_candidate
 
    count = 0 # setting the number of occurrences to 0
    for i in range(lenarr): # iteration through the array
        if arr[i] == final_candidate: # if the current element of the array is equal to final_candidate
            count += 1 # increase the number of occurrences to 0
    if count > lenarr /2: # if the number of occurrences is greater than half of the array
        print("Majority element: ", final_candidate) # printing the information about found majority element
    else: # otherwise
        print("No Majority Element") # printing "No majority element"

arr1 = [ 1,2,3,4,5,5,5,5,5,5,6] # the first array
print("First array", arr1) # printing "First array" and all the elements of the array
findmajorityhashmap(arr1) # calling the function
findmajorityvoting(arr1) # calling the function


arr2 = [ 1,2,3,4,3,3,2,4,5,6,1,2,3,4,6,1,2,3,4,6,6] # the second array
print("Second array", arr2) # printing "Second array" and all the elements of the array
findmajorityhashmap(arr2) # calling the function
findmajorityvoting(arr2) # calling the function