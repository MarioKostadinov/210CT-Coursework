from random import randint
#Task 10
#1. Given a sequence of n integer numbers, extract the sub-sequence of
# maximum length which is in ascending order.
array = [10,12,13,14,15,16,1,2,20,23,24,1,2,3,4,5,6,7,8,1,10,11,12,13,14,15,16,17,18,222]

longest_list = []
def output_highest_order():

    temp_array_one = []
    temp_array_two = []
    print(temp_array_one, temp_array_two)
    n = 0
    index_one = 0
    index_two = 1
    global longest_list
    while True:
        print(array)
        print("Run number : {}".format(n))
        n += 1

        try:
            if array[index_one] < array[index_two]:
                print("First Condition is True")
                print("{} < {}".format(array[index_one],array[index_two]))

                value = array.pop(index_one)
                print("Popping {}".format(value))

                print("Appending {} to temp_array_one".format(value))
                temp_array_one.append(value)

                print("temp_array_one:",temp_array_one)

            elif array[index_one] > array[index_two]:
                print("Second Condition is True")
                print("{} > {}".format(array[index_one],array[index_two]))

                value = array.pop(index_one)
                print("Popping {}".format(value))

                print("Appending {} to temp_array_one".format(value))
                temp_array_one.append(value)

                print("temp_array_one:",temp_array_one)
                while True:
                    print(array)
                    print("Loop number Two")
                    print("Run number : {}".format(n))
                    n += 1
                    try:
                        if array[index_one] < array[index_two]:
                            print("First(Second IF statement) Condition is True")
                            print("{} < {}".format(array[index_one], array[index_two]))

                            value = array.pop(index_one)
                            print("Popping {}".format(value))

                            print("Appending {} to temp_array_two".format(value))
                            temp_array_two.append(value)

                            print("temp_array_two:", temp_array_two)
                        elif array[index_one] > array[index_two]:
                            print("Second(Second ELIF statement Condition is True")
                            print("{} > {}".format(array[index_one], array[index_two]))

                            value = array.pop(index_one)
                            print("Popping {}".format(value))

                            print("Appending {} to temp_array_two".format(value))
                            temp_array_two.append(value)

                            print("temp_array_two:", temp_array_two)
                            print("temp_array_one", temp_array_one)

                            if len(temp_array_one) > len(temp_array_two):
                                print("The longest list is", temp_array_one)

                                if len(temp_array_one) > len(longest_list):

                                    longest_list = temp_array_one
                                    output_highest_order()

                            else:
                                print("The longest list is", temp_array_two)
                                if len(temp_array_two) > len(longest_list):


                                    longest_list = temp_array_two
                                    print("The Longest List is {}".format(longest_list))
                                    output_highest_order()


                    except IndexError:
                        print("Second Exeception")
                        print(array)
                        print(temp_array_one, temp_array_two)
                        """"""
                        value = array.pop(0)
                        print("Popping {}".format(value))

                        print("Appending {} to temp_array_one".format(value))
                        temp_array_two.append(value)

                        print("temp_array_two:", temp_array_two)
                        if len(temp_array_one) > len(temp_array_two):
                            print("The longest list is", temp_array_one)
                            global longest_list
                            if len(temp_array_one) > len(longest_list):
                                longest_list = temp_array_one
                                output_highest_order()

                        else:
                            print("The longest list is", temp_array_two)
                            if len(temp_array_two) > len(longest_list):
                                longest_list = temp_array_two
                                print("The Longest List is {}".format(longest_list))
                                output_highest_order()


            if len(array) == 1:
                print("First Exceptionnnn iffff")
                print(array)
                value = array.pop(0)
                print("Popping {}".format(value))

                print("Appending {} to temp_array_one".format(value))
                temp_array_one.append(value)
                print(temp_array_one)
                print("The longest list as of now is", longest_list)
                if len(temp_array_one) > len(longest_list):
                    longest_list = temp_array_one
                    print("The final longest list is:", longest_list)
                else:
                    print("The final longest list is:", longest_list)
                    exit()

        except IndexError:
            print("First Exceptionnnn")
            print(array)
            value = array.pop(0)
            print("Popping {}".format(value))

            print("Appending {} to temp_array_one".format(value))
            temp_array_one.append(value)
            print(temp_array_one)
            print("The longest list as of now is", longest_list)
            if len(temp_array_one) > len(longest_list):
                longest_list = temp_array_one
                print("The final longest list is:", longest_list)
            else:
                print("The final longest list is:", longest_list)
                exit()


def output_highest_order_two():

    temp_array_one = []
    temp_array_two = []
    print(temp_array_one, temp_array_two)
    n = 0
    index_one = 0
    index_two = 1
    global longest_list
    while True:
        print(array)
        n += 1
        try:
            if array[index_one] < array[index_two]:
                value = array.pop(index_one)
                temp_array_one.append(value)
            elif array[index_one] > array[index_two]:
                value = array.pop(index_one)
                temp_array_one.append(value)
                while True:
                    n += 1
                    try:
                        if array[index_one] < array[index_two]:
                            value = array.pop(index_one)
                            temp_array_two.append(value)
                        elif array[index_one] > array[index_two]:
                            value = array.pop(index_one)
                            temp_ar]]ray_two.append(value)
                            if len(temp_array_one) > len(temp_array_two):
                                if len(temp_array_one) > len(longest_list):
                                    longest_list = temp_array_one
                                    output_highest_order_two()
                            else:
                                if len(temp_array_two) > len(longest_list):
                                    longest_list = temp_array_two
                                    output_highest_order_two()
                    except IndexError:
                        value = array.pop(0)
                        temp_array_two.append(value)
                        if len(temp_array_one) > len(temp_array_two):
                            global longest_list
                            if len(temp_array_one) > len(longest_list):
                                longest_list = temp_array_one
                                output_highes]t_order_two()
                        else:
                            if len(temp_array_two) > len(longest_list):
                                longest_list = temp_array_two
                                output_highest_order_two()
            if len(array) == 1:
                value = array.pop(0)
                temp_array_one.append(value)
                if len(temp_array_one) > len(longest_list):
                    longest_list = temp_array_one
                else:
                    exit()

        except IndexError:
            value = array.pop(0)
            temp_array_one.append(value)
            print(temp_array_one)
            if len(temp_array_one) > len(longest_list):
                longest_list = temp_array_one
                print(longest_list)
            else:
                exit()


#task 11

class Node(object):
    def __init__(self, Value):
        self.value = Value
        self.next = None
        self.prev = None


class List(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, n, x):
        if n != None:
            x.next = n.next
            n.next = x
            x.prev = n
            if x.next != None:
                x.next.prev = x
        if self.head == None:
            self.head = self.tail = x
            x.prev = x.next = None
        elif self.tail == n:
            self.tail = x


    def display(self):
        num = self.head
        for i in range(10):
            if num == None:
                return None
            else:
                print(num.value)
                num = num.next

    def delete(self, n):
        num = self.head
        while num != None:
            if n.value == num.value:
                if num.prev != None:
                    num.prev.next = num.next
                else:
                    l.head = num.next
                if num.next != None:
                    num.next.prev = num.prev
                else:
                    l.tail = num.prev
                return True
            try:
                num = num.next
                print("Number is", num.value)
            except AttributeError:
                print("Exeception Caught")
                break
        return False


l = List()
l.insert(None, Node(1))
l.insert(l.head, Node(13))
l.insert(l.head, Node(132))
l.insert(l.head, Node(8))
l.insert(l.head, Node(55))
l.pri()
l.display()




















