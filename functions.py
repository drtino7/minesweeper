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




def check(x):
    for i in range(0,len(x)):
        for j in range(0,len(x[0])):
            if(isinstance(x[i][j],cl.mine) and x[i][j].reveled == False):
                print("x")
                
            if(isinstance(x[i][j],cl.NonMine) and x[i][j].reveled == False):
                print("x")
                
            if(isinstance(x[i][j],cl.NonMine) and x[i][j].reveled == True):
                count = 0
                if(isinstance(x[i-1][j-1],cl.mine)):
                    count = count + 1
                if(isinstance(x[i-1][j],cl.mine)):
                    count = count + 1            
                if(j < len(x[0]) and isinstance(x[i-1][j+1],cl.mine)):
                    count = count + 1            
                if(isinstance(x[i][j-1],cl.mine)):
                    count = count + 1
                if(j < len(x[0]) and isinstance(x[i][j+1],cl.mine)):
                    count = count + 1
                if(i < len(x) and isinstance(x[i+1][j-1],cl.mine)):
                    count = count + 1
                if(i < len(x) and isinstance(x[i+1][j],cl.mine)):
                    count = count + 1
                if(j < len(x[0]) and i < len(x) and isinstance(x[i+1][j+1],cl.mine)):
                    count = count + 1

                print(count)

