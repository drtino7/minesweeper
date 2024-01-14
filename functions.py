import classes as cl
import GameCreator as gc
import GameConfig as gco



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'






def converter(x):
    for i in range(0,int(gco.columns_rows)):
        for j in range(0,int(gco.columns_rows)):
            if(x[i][j]==1):
                x[i][j]=cl.mine()
            elif(x[i][j]==0):
                x[i][j]=cl.NonMine()




def show(x):
    print('',end='       ')
    for i in range(0,len(x)):
        if (i > 9):
            print(i, end= '  ')
        else:
            print(i,end='   ')
    print()
    print()
        
    for i in range(0,len(x)):
        

        if (i > 9): 
            print(i, end= ' ')
        else:
            print(i,end='  ')

        print('  ',end='')



        for j in range(0,len(x[0])):
            if(isinstance(x[i][j],cl.mine) and x[i][j].reveled == False and x[i][j].flag == False):
                print(bcolors.OKCYAN + '|' + bcolors.ENDC ,"x", end=' ')
                
            if(isinstance(x[i][j],cl.NonMine) and x[i][j].reveled == False and x[i][j].flag == False):
                print(bcolors.OKCYAN +'|' + bcolors.ENDC,"x", end=' ')
                
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


                if count == 0:
                    print(bcolors.OKCYAN +'| ' + bcolors.ENDC , end='')
                    print(bcolors.HEADER + str(count) + bcolors.ENDC + ' ', end='')
                elif count > 0:
                    print(bcolors.OKCYAN +'| ' + bcolors.ENDC ,  end='')
                    print(bcolors.WARNING + str(count) + bcolors.ENDC + ' ', end='')

               

            if(isinstance(x[i][j],cl.mine) and x[i][j].reveled == False and x[i][j].flag == True):
                print(bcolors.OKCYAN + '|'+ bcolors.ENDC, bcolors.FAIL +"✓" + bcolors.ENDC, end=' ')

            if(isinstance(x[i][j],cl.NonMine) and x[i][j].reveled == False and x[i][j].flag == True):

                print(bcolors.OKCYAN +'|' + bcolors.ENDC ,bcolors.FAIL + "✓" + bcolors.ENDC, end=' ')


        print(bcolors.OKCYAN +'|' + bcolors.ENDC,end='')

        print()
        print('     ',end='')
        for h in range(0,len(x)):
            print(bcolors.OKCYAN +'  - ' + bcolors.ENDC ,end='')
        print()




def play(x):
    playi = 0
    playj = 0
    show(x)
    print('\n')
    option = input('''
excavate[1]
flag[2]
select an option: ''')
    if option == '1':
        playi = int(input("tpye the column you want to reveal: "))
        playj= int(input("tpye the row you want to reveal: "))

        if x[playi][playj].flag == True:
            option=input('''
are you sure you want to excavate?
yes[y]
no[n]
select an option: ''')
            if(option == 'yes'):
                if(isinstance(x[playi][playj],cl.mine)):
                    cl.mine.explote()
                elif(isinstance(x[playi][playj],cl.NonMine) and x[playi][playj].reveled == False):  
                    x[playi][playj].reveled = True
                    won=False
            if option == 'y':
                if(isinstance(x[playi][playj],cl.mine)):
                    cl.mine.explote()
                elif(isinstance(x[playi][playj],cl.NonMine) and x[playi][playj].reveled == False):
                    x[playi][playj].reveled = True

        elif(isinstance(x[int(playi)][int(playj)],cl.mine)):
            cl.mine.explote()

        elif(isinstance(x[playi][playj],cl.NonMine) and x[playi][playj].reveled == False ):
            x[playi][playj].reveled = True
            won=False

    if option == '2':
        playi = input('type the column you want to flag: ')
        playj = input('type the row you want tp flag: ')
        playi = int(playi)
        playj = int(playj)

        x[playi][playj].flag = True
        

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

