"""
source: http://www.sciencedirect.com/science/article/pii/S1750583611000880
"""
# Digitized Gasphase Data from [Liu et al. (2011)] Fig 1.
T_low = [400.0, 964.87, 1163.90, 1218.04, 1230.48, 
         1235.60, 1236.34, 1234.87, 1232.68, 1226.82, 
         1222.43, 1216.58, 1210.73, 1204.87, 1196.82, 
         1190.24, 1182.92, 1172.68, 1164.63, 1159.51]

T_high = [400.0, 964.146341463, 1264.14, 1315.36, 
          1324.14, 1325.60, 1324.87, 1324.87, 1321.21,
          1315.36, 1310.24, 1303.65, 1295.60, 1289.02, 
          1278.78, 1270.00, 1259.75, 1250.24, 1239.26, 
          1226.09]

# Sample location distance is 0.025m from that we can compute the 
# corresponding times assuming a constant particle velocitiy of 2.5 m/s
pos = [0.025 * x for x,_ in enumerate(T_low)]
time = [0.025/2.5 * x for x,_ in enumerate(T_low)]
