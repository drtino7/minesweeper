import functions as fc
import GameConfig as gco
import GameCreator as gc
import classes as cl

x = gc.create_X()
fc.converter(x)
while(fc.check(x)!= 0):
    fc.show(x)
    fc.play(x)

print("you won")
