'''Learn open hashing. Implement a hash table using 2D lists. Input n
integers. Every number where 
num % 10 == 0 goes in sublist 0, 
== 1 goes in sublist 1, and so on. Print the hash table.
num % 10'''

def hash_table():
    hashtable=[[] for i in range(10)]
    n=int(input("Enter number of integers: "))
    for i in range(n):
        num=int(input("Enter number"+str(i+1)+": "))
        index=num%10
        hashtable[index].append(num)
    print("The hash table is: ")
    for k in range(10):
        print("sublist"+str(k)+":",hashtable[k])
hash_table()