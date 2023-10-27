import time as t
class mine:
    reveled=False
    def explote():
        import pygame as pg
        print("you lose")
        pg.init()
        pg.mixer.music.load('assets/lose_sound.wav')
        pg.mixer.music.play()
        t.sleep(5)
        quit()

class NonMine():
    reveled=False