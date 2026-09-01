'''Write a function for matrix multiplication. It should support any
dimensions and print errors where multiplication is impossible.'''


rows1=int(input("Enter number of rows of matrix 1: "))
cols1=int(input("Enter number of columns of matrix 1: "))
matrix1=[]
matrix2=[]
for i in range(rows1):
    rows=[]
    for j in range(cols1):
        x=int(input("Enter elements of matrix 1: "))
        rows.append(x)
    matrix1.append(rows)   
print("Matrix 1 is : ",matrix1)


rows2=int(input("Enter number of rows of matrix 2: "))
cols2=int(input("Enter number of columns of matrix 2: "))
for i in range(rows2):
    rowss=[]
    for j in range(cols2):
        x=int(input("Enter elements of matrix 2: "))
        rowss.append(x)
    matrix2.append(rows)   
print("Matrix 2 is : ",matrix2)


if cols1==rows2:
    product=[]
    for i in range(len(matrix1)):
        rowsss=[]
        for j in range(len(matrix2[0])):
            result=0
            for k in range(len(matrix2)):
                result=result+matrix1[i][k]*matrix2[k][j]
            rowsss.append(result)
    product.append(rowsss)  
    print("The matrix multiplication product is: ",product) 
else:
    print("Cannot to matrix multiplication")         



