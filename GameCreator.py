import random as rs
import GameConfig as gco
rs.random()

x=[]

for h in range(0,int(gco.columns_rows)) :
    x.append([])

print(x)

for i in range(0,):
    for j in range(0,int(gco.columns_rows)):
        if(rs.random() > int(gco.dificulty/10)):
            x[i][j] = 1
        else:
            x[i][j] = 0

print(x.split())