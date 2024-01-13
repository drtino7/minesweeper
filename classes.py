import time as t
import pygame as pg
class mine:
    reveled=False
    def explote():
        print("you lose")
        pg.init()
        pg.mixer.music.load('assets/lose_sound.wav')
        pg.mixer.music.play()
        t.sleep(5)
        quit()

class NonMine():
    reveled=False
