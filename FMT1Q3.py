'''Create a class with a function that does binary search in a list of strings.
Input a list like Q1, sort it using your Q2 function, input a string, search for it'''
from FMT1Q2 import sort
class binary:
    def binary_search(self):
        s=sort()
        a=s.selectionsort()
        e=input("Enter element: ")
        n=len(a)
        low=0
        high=n-1
        found=False
        while low<=high:
            mid=(low+high)//2
            if a[mid]==e:
                print("Element found",e)
                found=True
                break
            elif e<a[mid]:
                high=mid-1
            else:
                low=mid+1
        if found==False:             
            print("Element not found")
b=binary()           
b.binary_search()


    
