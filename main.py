import time as t

class mine:
    reveled=False
    def explote():
        print("you lose")
        t.sleep(1000)
        quit()


class NonMine():
    reveled=False

x=[[1,0,0,0,1],[0,1,0,0,1],[0,0,0,1,0],[1,0,1,0,0],[0,0,1,0,1]]

for i in range(0,5):
    for j in range(0,5):
        if(x[i][j]==1):
            x[i][j]=mine()
        elif(x[i][j]==0):
            x[i][j]=NonMine()

x[3][1].reveled = True

for i in range(0,len(x)):
    for j in range(0,len(x[0])):
        if(isinstance(x[i][j],mine) and x[i][j].reveled == False):
            print("x")
            
        if(isinstance(x[i][j],NonMine) and x[i][j].reveled == False):
            print("x")
            
        if(isinstance(x[i][j],NonMine) and x[i][j].reveled == True):
            count = 0
            if(isinstance(x[i-1][j-1],mine)):
                count = count + 1
            if(isinstance(x[i-1][j],mine)):
                count = count + 1            
            if(j < len(x[0]) and isinstance(x[i-1][j+1],mine)):
                count = count + 1            
            if(isinstance(x[i][j-1],mine)):
                count = count + 1
            if(j < len(x[0]) and isinstance(x[i][j+1],mine)):
                count = count + 1
            if(i < len(x) and isinstance(x[i+1][j-1],mine)):
                count = count + 1
            if(i < len(x) and isinstance(x[i+1][j],mine)):
                count = count + 1
            if(j < len(x[0]) and i < len(x) and isinstance(x[i+1][j+1],mine)):
                count = count + 1

            print(count)


