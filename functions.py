import classes as cl
import GameCreator as gc
import GameConfig as gco


def converter(x):
    for i in range(0,int(gco.columns_rows)):
        for j in range(0,int(gco.columns_rows)):
            if(x[i][j]==1):
                x[i][j]=cl.mine()
            elif(x[i][j]==0):
                x[i][j]=cl.NonMine()




def show(x):
    for i in range(0,len(x)):
        print('\n',end='')
        for j in range(0,len(x[0])):
            if(isinstance(x[i][j],cl.mine) and x[i][j].reveled == False):
                print("x", end=' ')
                
            if(isinstance(x[i][j],cl.NonMine) and x[i][j].reveled == False):
                print("x", end=' ')
                
            if(isinstance(x[i][j],cl.NonMine) and x[i][j].reveled == True):
                count = 0
                if(i > 0 and j > 0 and isinstance(x[i-1][j-1],cl.mine)):
                    count = count + 1
                if(i > 0 and isinstance(x[i-1][j],cl.mine)):
                    count = count + 1            
                if(j < len(x[0])-1 and i > 0 and isinstance(x[i-1][j+1],cl.mine)):
                    count = count + 1            
                if(j > 0 and isinstance(x[i][j-1],cl.mine)):
                    count = count + 1
                if(j < len(x[0])-1 and isinstance(x[i][j+1],cl.mine)):
                    count = count + 1
                if(j + 0 and i < len(x)-1 and isinstance(x[i+1][j-1],cl.mine)):
                    count = count + 1
                if(i < len(x)-1 and isinstance(x[i+1][j],cl.mine)):
                    count = count + 1
                if(j < len(x[0])-1 and i < len(x)-1 and isinstance(x[i+1][j+1],cl.mine)):
                    count = count + 1

                print(count,end=' ')
            

def play(x):
    print('\n')
    playi = int(input("tpye the column you want to reveal: "))
    playj= int(input("tpye the row you want to reveal: "))


    if(isinstance(x[int(playi)][int(playj)],cl.mine)):
        cl.mine.explote()

    elif(isinstance(x[playi][playj],cl.NonMine) and x[playi][playj].reveled == False):
        x[playi][playj].reveled = True
        won=False
        

def check(x):
    check=0
    for i in range(0,len(x)):
        for j in range(0,len(x[0])):
            if(isinstance(x[i][j],cl.NonMine) and x[i][j].reveled == False):
                check = check + 1

    return check
            

def win():
    import pygame as pg
    import time as t
    print("YOU WON!!!")
    pg.init()
    pg.mixer.music.load('assets/win_sound.wav')
    pg.mixer.music.play()
    t.sleep(5)

