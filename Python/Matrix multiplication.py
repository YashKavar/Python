import numpy as np

m1=np.array([
            [1,2,3,4,5],
            [4,5,6,7,8]

        ])
m2=np.array([[4,5,],[6,8],[5,7],[2,4],[3,8]])
# m2=matrix['1 4 7; 2 5 8']

m3=m1.dot(m2)
print(m3)
# m3=m1*m2
# print(m3)

