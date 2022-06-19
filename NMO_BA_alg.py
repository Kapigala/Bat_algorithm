import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

#Obliczanie wartości funkcji Ackleya
def f(array):
    return -20*np.exp((-0.2*np.sqrt(0.5*(array[0]**2+array[1]**2))))-np.exp(0.5*(np.cos(2*np.pi*array[0])+np.cos(2*array[1]*np.pi)))+np.e+20

#PARAMS
iterations=301
pop_size=30

f_min=0
f_max=1
dim=2
min_value=-100
max_value=100

#stałe
alfa=0.85
gamma=0.3

#Inicjacja wartości dla nietoperzy
fs=np.random.random(pop_size)*(f_max-f_min)+f_min
pos_matrix=np.random.uniform(min_value,max_value,(pop_size,dim))
v_matrix=2*np.random.random((pop_size,dim))
r0_matrix=np.random.uniform(0.75,1,pop_size)
A_matrix=np.random.uniform(30,20+max_value*1/2,pop_size)
r_matrix=r0_matrix*(1-np.exp(-gamma*1))

def find_best(pop_size,nietoperze):
    best=10**6
    coor=[]
    for n in range(pop_size):
        if f(nietoperze[n]) < best:
            coor=nietoperze[n]
            best=f(nietoperze[n])
    return coor

optimal_sol=[100,100]

for i in range(1,iterations+1):
    best=find_best(pop_size,pos_matrix)

    for bat in range(pop_size):
        fs[bat]=np.random.uniform(0,1)
        v_matrix[bat]=v_matrix[bat]+0.85*(pos_matrix[bat]-best)*fs[bat]
        #Utworzenie pozycji kandydata
        candidate_pos= pos_matrix[bat] + v_matrix[bat]
        #Decyzja czy porzucamy kandydata na korzyść innego z sąsiedztwa najlepszego nietoperza
        if np.random.random() > r_matrix[bat]:
            candidate_pos = best + A_matrix.mean() * np.random.uniform(-1,1,2)
        #Decyzja czy akcjeptujemy kandydata
        if (A_matrix[bat] > np.random.random()) & (f(candidate_pos)<f(pos_matrix[bat])):
            pos_matrix[bat]=candidate_pos

        #Kontrola uciekania 'poza ściane'
        if pos_matrix[bat][0]<min_value:
            pos_matrix[bat][0]=min_value
            v_matrix[bat][0]=30
            v_matrix[bat][1]=30 * np.random.choice([-1, 1])
        if pos_matrix[bat][1]<min_value:
            pos_matrix[bat][1]=min_value
            v_matrix[bat][0]=30 * np.random.choice([-1, 1])
            v_matrix[bat][1]=30
        if pos_matrix[bat][0]>max_value:
            pos_matrix[bat][0]=max_value
            v_matrix[bat][0]=-30
            v_matrix[bat][1]=30 * np.random.choice([-1, 1])
        if pos_matrix[bat][1]>max_value:
            pos_matrix[bat][1]=max_value
            v_matrix[bat][0]=30 * np.random.choice([-1, 1])
            v_matrix[bat][1]=-30

    if f(best)<f(optimal_sol):
        optimal_sol=best

print('Rozwiązanie:',optimal_sol,'Wartość',f(optimal_sol))
