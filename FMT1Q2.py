class sort:
    def selectionsort(self):    
        l=[]
        n=int(input("Enter the number of elements in the list"))
        for k in range(n):
             l.append(input("Enter list elements"))             
        n=len(l)
        for i in range(0,n):
            min=i
            for j in range(i,n):
                if l[j]<l[min]:
                    min=j
            l[i],l[min]=l[min],l[i] 
        return l              
sorter = sort()
print(sorter.selectionsort())

    
'''Create a class with a function that does selection sort on a list of
strings. Input a list like Q1, call the function, print the output.'''


