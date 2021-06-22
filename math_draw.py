import numpy as np
import matplotlib.pyplot as plt

x, y = np.loadtxt('output_bfs.txt', delimiter=' ', unpack=True)
x=x/10
plt.plot(x, y, label='bfs') 

x, y = np.loadtxt('output_final.txt', delimiter=' ', unpack=True) 
x=x/10
plt.plot(x, y, label='final')

x, y = np.loadtxt('output_github.txt', delimiter=' ', unpack=True)
x=x/10
plt.plot(x, y, label='github')

x, y = np.loadtxt('output_ideal.txt', delimiter=' ', unpack=True)
x=x/10
plt.plot(x, y, label='ideal')

x, y = np.loadtxt('output_s.txt', delimiter=' ', unpack=True)
x=x/10
plt.plot(x, y, label='s')



plt.xlabel('sec') 
plt.ylabel('score') 
plt.title('FIND THE SNAKE KING') 
plt.legend() 
plt.show() 