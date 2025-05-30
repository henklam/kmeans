import math, random
def euclidean_distance(coord1, coord2):
        return math.sqrt((coord2[0] - coord1[0])**2 + (coord2[1] - coord1[1])**2)
def closest_stationary_point(coord,list):
        lowest = euclidean_distance(coord, list[0])
        count = 0
        index = 0
        for c in list:
            dist = euclidean_distance(coord,c)
            if(dist < lowest):
                lowest = dist
                index = count
            count += 1
        return index
def readFile(inputFile):
    with open(inputFile, 'r') as file:
        clusterMap = []
        coordinates = file.read().split()
        clusters = input("Enter number of clusters: ")
        clustersList = []
        numClusters = []
        num = 0
        for i in range(int(clusters)):
            index = random.randint(0, len(coordinates)-1)
            c = coordinates[index].strip().split(',')
            c1 = [float(c[0]), float(c[1])]
            clustersList.append(c1)
            numClusters.append(num)
            num += 1
        print("The random cluster centers are")
        for coord in clustersList:
            print("(" + str(coord[0]) + "," + str(coord[1]) + ")")
        print()
    times = -1
    clusterMapList = []
    while True:
        with open(inputFile, 'r') as file:
            clusterMap = []
            coordinates = file.read().split()
            for coord in coordinates:
                    coordList = coord.strip().split(',')
                    coordinate = [float(coordList[0]), float(coordList[1])]
                    clusterMap.append(numClusters[closest_stationary_point(coordinate,clustersList)])
                    print("(" + str(coordinate[0]) + "," + str(coordinate[1]) + ") belongs in cluster " + str(numClusters[closest_stationary_point(coordinate, clustersList)]) + " with a centroid of (" + str(clustersList[closest_stationary_point(coordinate, clustersList)][0]) + "," + str(clustersList[closest_stationary_point(coordinate, clustersList)][1]) + ")")
            clusterMapList.append(clusterMap)
            times += 1
            if(times > 0):
                if(clusterMapList[times-1] == clusterMapList[times]):
                    break
            nothing = input("Hit enter to continue")
            for i in range(len(numClusters)):
                count = 0
                xValue = 0
                yValue = 0
                for n in range(len(clusterMap)):
                    if(clusterMap[n] == numClusters[i]):
                        coordinates2 = []
                        for coord in coordinates:
                            coordList = coord.strip().split(',')
                            coordinate = [float(coordList[0]), float(coordList[1])]
                            coordinates2.append(coordinate)
                        xValue += float(coordinates2[n][0])
                        yValue += float(coordinates2[n][1])
                        count += 1
                if(count > 0):
                    clustersList[i][0] = xValue/count
                    clustersList[i][1] = yValue/count
            print("Your new centroids are: " + str(clustersList))
fileInput = "FiveCoordinates.csv"
readFile(fileInput)