import math

centroid =[[-4.89680383e-02, -4.00953648e-01,  1.86463646e-01,
         2.06965251e-01,  6.51875111e-02,  9.42557737e-02,
        -3.59637263e-01,  8.48317906e-02,  2.06399176e-01,
        -1.71955416e-01,  1.27147373e-01,  6.30196850e-01,
        -1.41807314e+00],
       [-8.71894477e-02, -2.46491090e-01, -8.58221316e-01,
        -1.03856687e+00, -7.93366154e-01, -1.08456994e+00,
        -2.16222284e-01, -2.96121324e-01, -2.77069689e-01,
        -1.76833657e-01, -2.42400938e-01, -2.70458640e-01,
         1.58022549e-02],
       [ 1.19102407e-01,  3.95793581e-01, -1.20097027e-04,
         1.43449239e-01,  2.32262211e-01,  2.55774285e-01,
         5.89398974e-01, -6.97550448e-01, -7.02825720e-01,
        -3.49746796e-02, -5.21185284e-01, -5.10907779e-01,
         5.61256568e-01],
       [-2.75364349e-01, -5.79934297e-01,  3.17663621e-01,
         3.05153463e-01,  6.49546984e-02,  1.08904813e-01,
        -2.24972290e-01,  5.62741877e-01,  6.40006832e-01,
        -2.88568693e-01,  4.39033526e-01,  6.35336081e-01,
         6.98467334e-01],
       [-1.96847122e-01, -6.78599071e-01, -4.31199096e-01,
        -6.97529667e-01,  2.95361109e-02, -8.66282300e-02,
        -1.22013805e+00, -1.18149030e+00, -1.03074404e+00,
         2.01787871e+00, -6.00871622e-01, -7.84700794e-02,
         6.62509670e-02],
       [ 3.23267492e-01,  1.07958656e+00,  2.70179259e-01,
         3.25550642e-01,  8.80005139e-02,  2.39317273e-01,
         6.95723089e-01,  1.08165121e+00,  7.60911957e-01,
        -3.41819476e-01,  5.76397481e-01, -5.54325659e-01,
         5.44543232e-01]]
Test = [0]*13
Test2 = [1]*13


def pythlist (list1, list2):
    summ = 0
    for i in range(len(list1)):
        summ += ((list1[i]-list2[i])**2)
    return (summ)**0.5

def findCluster (centroids, testList):
    vals = [0,0,0,0,0,0]
    for i in range(6):
        vals[i] = pythlist(centroids[i],testList)
    minval = min(vals)
    cluster = vals.index(minval) + 1
    print vals
    return cluster

print findCluster(centroid, Test)
print findCluster(centroid, Test2)
