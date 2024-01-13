dificulty = input("enter a number from 1 to 10 for the dificulty: ")
columns_rows = input("how many columns and rows do yuo want: ")

dic = [i for i in range(1,10)]
if dificulty in dic:
    dificulty = input("numver must be in 1 to 9, select an other one: ") 
