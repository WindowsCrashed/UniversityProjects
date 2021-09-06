import numpy as np


def multNumMat(num, mat):
    matResult = []

    for i in range(len(mat)):
        matResCurrentLine = []

        for j in range(len(mat[i])):
            matResCurrentLine.append(num * mat[i][j])

        matResult.append(matResCurrentLine)

    return np.array(matResult)


def printMat(mat):
    for i in range(len(mat)):
        print(mat[i])


def createMat(name):
    matData = []
    while True:
        try:
            # Ex: 2 3; 1 2; 3 1..
            ordMat = input(f'\nOrder of Matrix {name.upper()}: ').split()

            if len(ordMat) != 2:
                raise Exception

            break
        except Exception:
            print('\nInvalid order\nTry again\n')

    for i in range(int(ordMat[0])):
        while True:
            try:
                # Ex: 2 3; 1 2 1; 12 3 22 3211..
                matCurrentLine = input(
                    f'Matrix {name.upper()} Line {i+1}: ').split()

                if len(matCurrentLine) != int(ordMat[1]):
                    raise Exception

                matData.append([int(j) for j in matCurrentLine])

                break
            except Exception:
                print('\nInvalid number of columns\nTry again\n')

    return np.array(matData)


# Mat A
a = createMat('a')

# Mat B
b = createMat('b')

# K
while True:
    try:
        # Ex: 3; 2; 12..
        k = float(input('\nValue of K: '))

        if k == 0:
            raise Exception

        break
    except Exception:
        print('\nInvalid value for K\nTry again\n')


# Equations

# a)
try:
    eqA = multNumMat(k, (a + b))

    print('\na) K * (A + B) =')
    printMat(eqA)
except ValueError:
    print('\nA has different order than B')

# b)
try:
    eqB = multNumMat((k/4), a) + multNumMat((k/5), b)

    print('\nb) ((K/4) * A) + ((K/5) * B) =')
    printMat(eqB)
except ValueError:
    print('\nA has different order than B')

# c)
try:
    eqC = a.dot(b)

    print('\nc) A * B =')
    printMat(eqC)
except ValueError:
    print('\nOrder A incompatible with order B')
