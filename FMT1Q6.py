'''Improve Q5. Insert each new number so the sublist stays sorted. Do not
sort after insertion. Hint, find the insertion index using binary search.'''


def hash_table():
    hashtable=[[] for i in range(10)]
    n=int(input("Enter number of integers: "))
    for j in range(n):
        num=int(input("Enter number"+str(j+1)+":"))
        index=num%10
        sublist=hashtable[index]
        default=len(sublist)

        low=0
        high=len(sublist)-1
        while(low<=high):
            mid=(low+high)//2
            if sublist[mid]>=num:
                high=mid-1
                default=mid
            elif sublist[mid]<=num:
                low=mid+1
        sublist.insert(default,num)

    print("The hash table is :")
    for k in range(10):
        print("Sublist"+str(k)+":",hashtable[k])

hash_table()