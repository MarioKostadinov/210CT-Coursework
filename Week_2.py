#Task 3
# Write the pseudocode for a function which returns the
# highest perfect square which is less or equal to its
# parameter (a positive integer). Implement this in a programming
# language of your choice.

def perfectSqr(num):

    for i in range(num):

        squire = i*i

        if squire == num:
            print(i*i)
            return i*i
        if squire > num:
            print((i-1)*(i-1))
            return i*i

print(perfectSqr(99))

def perfectSquire(number)

    stack <- [1,2...,number]

    for i to lenght[stack]

        sqr = i*i
        if sqr = number
            return i
        if sqr > number
            return i-1




#Task 4

#Task 5

def multiply_matrices(matrice_one, matrice_two)


    # we need to check the size of the matrices first
    # if matrice_one more columns than matrice_two rows
    # then we canno multiply them
    check_size(matrice_one, matrice_two)
    if matrice_one.rows = matrice_two.colums
    return True

else return False

matrice_three < - []

# this creates the next size of the matrix
for i < -1 to length(size.of.matrice_one)
matrice_three.add[0]
for i < -1 to length(size.of.matrice_one)
for c < -1 to length(size.of.matrice_two)
matrice_three.add[0]

for i < -1 to length(size.of.matrice_one)
for c < -1 to length(size.of.matrice_two+1)
matrice_three[I][c] = matrice_one[i][c] * matrice_two[i][c]

return matrice_three


def addition_matrices(matrice_one, matrice_two)
    matrice_three < - []

    for i < -1 to length(matrice_one)
    for k < -1 to length(matrice_two)
    a = matrice_one[i]
    b = matrice_two[i]
    matrice_three = a[k] + b[k]


return matrice_three


def subtract_matrices(matrice_one, matrice_two)
    matrice_three < - []

    for i < -1 to length(matrice_one)
    for k < -1 to length(matrice_two)
    a = matrice_one[i]
    b = matrice_two[i]
    matrice_three = a[k] - b[k]


return matrice_three
A = B * C –2 * (B + C)
R1 < - multiply_matrices(B, C)
R2 < - addition_matrices(B, C)
R3 < -multiply_matrices(2, R2)
R < -R1 + R3

