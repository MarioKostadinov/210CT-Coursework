#6. Write the pseudocode and code for a function that reverses the words in a sentence.
# Input: "This is awesome" Output: "awesome is This". Give the Big O notation.

#Task 6
def sentenceReverse():

    user_input = input("Enter a sentence" )

    splitted_list = user_input.split()

    reversed_list = []

    input_lenght = len(splitted_list)

    while input_lenght > 0:

        the_index = len(splitted_list) - 1
        try:
            popped_word = splitted_list.pop(the_index)

            reversed_list.append(popped_word)
        except IndexError:
            return reversed_list

    return reversed_list

#Write pseudocode about task 6

#Task 7
#It could require some more work, but it works as it is

def checkPrime(number):

    stack = []

    for i in range(1, number):
        num = number % i
        print("The number is", i)
        stack.append(num)
        print("Appending {} to list".format(num))
    print("The Entire stack is", stack)
    print("The number of Zeroes in the stack are", stack.count(0)+1)
    if stack.count(0) > 1:
        return False
    else:
        return True


stack = []

def recursivePrime(value_one, value_two):

    print("Value one is",value_one)
    value = value_two % value_one
    stack.append(value)
    print("Appending {} to list".format(value))
    print(stack)
    print("The stack count is", stack.count(0))
    the_stack = stack.count(0)
    if the_stack > 1:
        print("It is not a Prime Number")
        return False
    elif the_stack < 2 and value_one != 2:
        print("Executing Second Condition")
        recursivePrime(value_one - 1, value_two)
    else:
        print("It is a Prime Number")
        return True


#Write psuedocode for task 7



#Task 8
def split_word(the_word):
    stack = []
    for i in the_word:
        stack.append(i)

    return stack


def is_vowel_left(splitted_word):
    vowels = ["a", "e", "o", "u", "y", "i"]
    count = 0
    for v in vowels:
        if v in splitted_word:
            return True
        elif count == 5:
            return False
        count += 1


def vowel_removal_function(word, number_of_starts):

    print("Number of Starts {}, and the word is {}".format(number_of_starts, word))

    vowels = ["a", "e", "o", "u", "y", "i"]

    splitted_word = split_word(word)  # Splits the string into a list

    is_there_a_vowel_left = is_vowel_left(word) #Checks if any Vowels remain in the word

    if is_there_a_vowel_left == True:
        new_word = "".join(splitted_word)
        print("Executing first Condition")
        count = 0
        for v in vowels:
            count += 1
            print("The new word is", new_word)
            values = v in splitted_word
            if values == True:
                print("We found a vowel")
                print("Removing {}...".format(v))
                var = splitted_word.index(v)
                del splitted_word[var]
                print(splitted_word)
                new_word = "".join(splitted_word)
                number_of_starts += 1
                vowel_removal_function(new_word, number_of_starts)

    else:
        print("Final Execution")
        print(splitted_word)
        return splitted_word


vowel_removal_function("beautiful", 0)













