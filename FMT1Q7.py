'''Let (x,y) be a point in 2D space. Given a list of coordinates, write a sort
function that sorts them by proximity to a reference point given by the user
that is not in the list. Eg list 
[(0,1),(0,3),(1,2)] , reference 
(0,0) ,
output 
[(0,1),(1,2),(0,3)]'''

import math
def distance():
    return math.dist(Coordinates,reference)
Coordinates=[]
n=int(input("How many coordinates do you want to enter"))
for i in range(n):
    x=int(input("Enter x coordinate: "))
    y=int(input("Enter y coordinate: "))
    Coordinates.append((x,y))
print(Coordinates)

a=int(input("Enter reference point x coordinate: "))
b=int(input("Enter reference point y coordinate: "))
reference=(a,b)
Coordinates.sort(key=distance)
print(Coordinates)
