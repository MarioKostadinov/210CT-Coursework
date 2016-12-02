from random import randint
#Task 1

array = [3, 2, 1, 5, 7, 13, 25, 4]
def random_shuffle_function(array):
    """
    This function takes an array
    and shuffles it randomly to another
    list
    """

    new_array = []


    while len(array) != 0:

        variable = randint(0, (len(array)-1))
        variable_two = array.pop(variable)
        print("Popping", variable_two)
        new_array.append(variable_two)
        print("The New Array is",new_array)

    return new_array

#Task 2



def trailing_zeroes(number):
    """
    This function returns the number of
    trailiing zeroes in a factorial
    number
    """

    total_trailing_zeroes = 0
    fives = 5
    num = 2
    while True:


        var = number / fives
        print("The number is", var)
        if var > 1:
            total_trailing_zeroes += int(var)
            print(fives)
        else:
            print("Final result is {} trailizing zeroes".format(total_trailing_zeroes))
            return total_trailing_zeroes
        fives = 5**num
        num = num+1

#Task 3

"""
Does the algorithms have defined inputs and outputs?

-   The algorithms do not have defined inputs or outputs.
    They calculate the output based on the input

Can you guarantee that it terminates?

-   Yes, They have clear and easy conditions that terminate
    the loops

Is it specified in a clear and concise manner?

-   Yes, with proper variable and function names,
    everything should be clear and concise.

Does your algorithm produce the correct result for all instances?

- Only if wrong data type is enter, then it will result into an error

"""
