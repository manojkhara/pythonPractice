arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

for i in range(len(arr[0])):
    col = len(arr[0])
    print( arr[(i)][col%(i+1)])



