#Week 4
#Task 9


#Generates our list
def generateList(size):
    just_list = []
    for i in range(size):
        just_list.append(i)

    return just_list


def binarySearch(data, a, b):
    '''
        Binary Search Algorithm

        Binary Search gets a sorted list and searches
        for a specific value or in a set of values
        in our case.

        As arguments it take a sorted array and the two values
        we want to search for.

        Afterwards, it starts by taking the middle value of a list
        and checks whether it has found the value and if not it sees
        whether it is less or higher than the middle value.
        This keeps looping until the middle value equals
        the value we are checking for .
    '''

    another_list = [] #Stores our range of numbers
    for i in range(a, b):
        another_list.append(i)

    first_value = 0
    last_value = len(data) - 1

    found = False
    while first_value <= last_value and not found:
        mid_value = (first_value + last_value) // 2 #Return the middle value in the list
        if data[mid_value] in another_list:
            found = True
        else:
            if max(another_list) < data[mid_value]:
                last_value = mid_value - 1
            else:
                first_value = mid_value + 1
    return found

data=[1,2,3,4,5,6,7,8,9,10,15,23,111]
print(binarySearch(data, 111, 222))
def main():
    '''
    Initiates the main task and asks for
    two numbers and the list size.
    And it calls the binary search.

    '''

    vO = input("Enter a number ") #Input first value
    value_one = int(vO)
    vT = input("Enter a number ") #Input second value
    value_two = int(vT)
    ls = input("Enter the list size ") #Input the size of the list
    list_size = int(ls)


    list_two = generateList(list_size) #Generates a list

    #Here we call the binary search function
    search = binarySearch(list_two, value_one, value_two)



    return search


