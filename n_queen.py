import numpy as np #use numpy
import pandas as pd #use pandas

n= int(input()) # n is a number of n x n matrix

num = 0 #number of queens
row = [0]*n #initialize matrix

def check(x): #check the queen's position
    for i in range(x):
        if row[x]==row[i] or abs(row[x] - row[i]) == abs(x-i):
            return False
    return True

def Result(x): #function about print result

    Matrix = [["0"]*x for _ in range(x)] #basically all of the matrix's values are '0'
    Matrix = pd.DataFrame(Matrix) #Matrix's architecture
    Matrix = np.array(Matrix.values) #array's values

    for i in range(x):
        for j in range(x):
            if i == row[j]:
                Matrix[i][j] = "1" #'1' is meaning there is a queen
    print(Matrix) #show matrix
    print("\n")

def queen(x): #Total possible arrangements of queens
    global num
    if x==n:
        if (num < 10): #to print the first few arrangements (not more than 10)
            Result(x)
        num += 1 #from 0 to 'n'
        return
    for i in range(n):
        row[x] = i
        if check(x):
            queen(x+1)



print("The first few (not more than 10) arrangements are:\n")
queen(0) #from 0 to 'n'
print("Total possible arrangements : ", num)
