import random as rs
import GameConfig as gco

def create_X():
    x = [[0 for j in range(int(gco.columns_rows))] for i in range(int(gco.columns_rows))]


    for i in range(0,int(gco.columns_rows)):
        for j in range(0,int(gco.columns_rows)):
            if(rs.random() < int(gco.dificulty)/10):
                x[i][j] = 1

    return x
