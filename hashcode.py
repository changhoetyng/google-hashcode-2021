starts = []
end = []
name = []
seconds = []
startPoint = []
endPoint = []
thisdict={}

def printOneIntersect(end,name):
  f = open("outputE.txt", "a")
  f.write(end + "\n")
  f.write("1\n")
  f.write(name + " 1\n")
  f.close()

with open('e.txt', 'r') as f:
    content = f.readlines()
    totalRunTime, intersections, streets, cars, points = [int(x) for x in content[0].split()]

    car = []

    for x in range(0, intersections):
        new = []
        new2 = []
        startPoint.append(new)
        endPoint.append(new2)

    for x in range(1,streets + 1):
        startsIn, endIn, nameIn, secondsIn = content[x].split()
        starts.append(startsIn)
        end.append(endIn)
        name.append(nameIn)
        seconds.append(secondsIn)
        startPoint[int(startsIn)].append(x-1)
        endPoint[int(endIn)].append(x-1)

    lines = [x for x in range(0, streets)]

    

    for x in range(streets + 1, len(content)):
        car = content[x]
        temp = car.split()
        del temp[0]
        for y in temp:
            if y in thisdict:
                thisdict[y] += 1
            else:
                thisdict[y] = 1
    print(thisdict)

    f = open("outputE.txt", "w")
    f.write(str(len(endPoint)) + "\n")
    f.close()

for x in range(0,intersections):
    if(len(endPoint[x]) == 1):
        point = endPoint[x]
        line = point[0]
        idx = lines.index(line)
        printOneIntersect(end[idx],name[idx])
        del lines[idx]
        del starts[idx]
        del end[idx]
        del name[idx]
        del seconds[idx]

for x in range(0,intersections):
    if(len(endPoint[x]) == 1):
        continue

    point = endPoint[x]
    z = point[0]
    idx = lines.index(z)
    # print(idx)
    f = open("outputE.txt", "a")
    f.write(end[idx]+"\n")
    f.write(str(len(point)) + "\n")
    for x in range (0,len(point)):
        try:
            if((thisdict[name[idx]] / cars) * 100 > 50):
                z = point[x]
                idx = lines.index(z)
                f.write(name[idx] +" 3\n")
            else:
                z = point[x]
                idx = lines.index(z)
                f.write(name[idx] +" 1\n")
        except:
            z = point[x]
            idx = lines.index(z)
            f.write(name[idx] +" 1\n")
    f.close()

# print(lines)
# print(startPoint)
# print(endPoint)