import matplotlib.pyplot as plt
import numpy as np

with open('city.txt','r',encoding="utf-8") as fp:
    populations = fp.readlines()

city = list()
popu = list()

for p in populations:
    pp = p.split(',')

    city.append(pp[0])
    popu.append((int(pp[1].rstrip('\n'))))
# print(city)
ind = np.arange(len(city))
# print(popu)
plt.bar(ind, popu)
plt.xticks(ind+0.5,city)
plt.title('Program test')
plt.show()