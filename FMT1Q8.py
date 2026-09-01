'''Consider a CSV (
cones.csv ) with cone id, x, y, colour (blue or yellow)
per row. Sort the rows by distance from the origin. Write two new CSVs, one
per colour, keeping the sorted order. Then find the midpoint between every
blue cone and its nearest yellow cone and write those midpoints to
centreline.csv .'''


import math
import csv
file=open("/Users/dhruv/cones.csv","w")
writer=csv.writer(file)
writer.writerow(["id","x","y","colour"])
writer.writerow(["1","2","1","blue"])
writer.writerow(["2","5","9","yellow"])
writer.writerow(["3","3","3","blue"])
writer.writerow(["4","7","2","yellow"])
file.close()

file=open("/Users/dhruv/cones.csv","r")
reader=csv.DictReader(file)
cones=[]
for row in reader:
    row["x"]=float(row["x"])
    row["y"]=float(row["y"])
    row["distance"]= math.sqrt(row["x"]**2+row["y"]**2)
    cones.append(row)
file.close()

def distance(x):
    return x["distance"]

cones.sort(key=distance)

blue=[]
yellow=[]
for cone in cones:
    if cone["colour"]=="blue":
        blue.append(cone)
    elif cone["colour"]=="yellow":
        yellow.append(cone)

file=open("/Users/dhruv/blue.csv","w")
writer=csv.writer(file)
writer.writerow(["id","x","y","colour"])
for cone in blue:
    writer.writerow([cone["id"],cone["x"],cone["y"],cone["colour"]])
file.close()

file=open("/Users/dhruv/yellow.csv","w")
writer=csv.writer(file)
writer.writerow(["id","x","y","colour"])
for cone in yellow:
    writer.writerow([cone["id"],cone["x"],cone["y"],cone["colour"]])
file.close()

midpt=[]
for b in blue:
    nearest_yellow=None
    smallest_distance=float("inf")
    for y in yellow:
        Distance=math.sqrt((b["x"]-y["x"])**2+(b["y"]-y["y"])**2)
        if Distance<smallest_distance:
            smallest_distance=Distance
            nearest_yellow=y
    midptx=(b["x"]+nearest_yellow["x"])/2
    midpty=(b["y"]+nearest_yellow["y"])/2
    midpt.append([b["id"],nearest_yellow["id"],midptx,midpty])

file=open("/Users/dhruv/centreline.csv","w")
writer=csv.writer(file)
writer.writerow(["Blue cone id","Yellow cone id","x coordinate","y coordinate"])
for point in midpt:
    writer.writerow(point)
file.close()






