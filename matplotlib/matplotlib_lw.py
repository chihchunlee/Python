import matplotlib.pyplot as plt

w = [1,3,4,5,9,11]
x = [1,2,3,4,5,6,]
y = [20,30,43,22,34,20]
z = [12,33,43,22,34,20]

plt.plot(x,y,lw=5,label='Mary')
plt.plot(w,z,lw=2,label='Tom')
plt.xlabel('month')
plt.ylabel('dollars (million)')
plt.legend()
plt.title('test fire')
plt.show()