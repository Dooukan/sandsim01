from settings import*
from map import*

import pygame as pg
import random as rd
import sys


class Game:
    def __init__(self):
        print("loading done!")
        self.screen = pg.display.set_mode(SCREENSIZE)
        self.clock = pg.time.Clock()
        self.fps = FPS
        self.bot = SIZEY - 1
        self.mapdict = MAPDICT.copy()
        self.mapcor = MAPCORS.copy()
        self.blocks = dict()

    def new_game(self):
        key = pg.key.get_pressed()
        if key[pg.K_r] or key[pg.K_F5]:
            self.mapdict = MAPDICT.copy()
            self.block = dict()
    
    def update(self):

        self.delta_time = self.clock.tick(self.fps)
        pg.display.set_caption("snow:click,r=F5")
        pg.display.flip()
       

    def add(self):
        tx,ty = pg.mouse.get_pos()
        x = round((tx)/BLOCKSIZE)
        y = round((ty)/BLOCKSIZE)
        key = pg.mouse.get_pressed(3)
    
        if key[0] and 0<=x<=SIZEX*CHUNKX-1 and 0<=y<=SIZEY*CHUNKY-1:
            self.mapdict.update({(x,y):1})


     #very inefficient block of my code    
    def find_block(self,I,v):

        L = []
        for x in range(SIZEX):
            for y in range(SIZEY-1):
                if v == I[x,y]:
                    L.append((x,y))
        return L


    def drop(self):
    
        #maybe I need save after block contanct whit flor but I dont know but look at this if cycle not prety huh
        for I in reversed(self.find_block(self.mapdict,1)):
   
            x,y = I
            p = [-1,0,1]
            if x>SIZEX-2:
                p.remove((1))
                if self.mapdict[(x,y+1)] == 1:
                    p.remove(0)
                if self.mapdict[(x-1,y+1)] == 1:
                    p.remove(-1)

            elif x<1:
                p.remove((-1))
                if self.mapdict[(x,y+1)] == 1:
                    p.remove(0)
                if self.mapdict[(x+1,y+1)] == 1:
                    p.remove(+1)
        
            else:
                if self.mapdict[(x+1,y+1)] == 1:
                    p.remove(+1)
                if self.mapdict[(x-1,y+1)] == 1:
                    p.remove(-1)
                if self.mapdict[(x,y+1)] == 1:
                    p.remove(0)

            if p != []:
                r = rd.choice(p)
                self.mapdict.update({(x,y):0})
                self.mapdict.update({(x+r,y+1):1})
            else:
                pass


    def draw(self):
        self.screen.fill("black")
        h0 = rd.choice(range(50,150))
        h1 = rd.choice(range(50,150))
        h2 = rd.choice(range(50,150))
        for c in self.mapdict:
            h0 = rd.choice(range(50,190))
            h1 = rd.choice(range(50,190))
            h2 = rd.choice(range(50,190))
            x,y = c
            if y > SIZEY-1:
                pass
            # what I am doing here?
            #elif self.mapdict[(x,y)]== 0: 
            #    pg.draw.rect(self.screen,(20,20,20),(BLOCKSIZE+x*BLOCKSIZE,BLOCKSIZE+y*BLOCKSIZE,BLOCKSIZE,BLOCKSIZE))                
            if self.mapdict[(x,y)]== 1:
    
                pg.draw.rect(self.screen,(250,y,y),(BLOCKSIZE+x*BLOCKSIZE,BLOCKSIZE+y*BLOCKSIZE,BLOCKSIZE,BLOCKSIZE))
    def check_events(self):
         for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
    
    def run(self):
        while True:

            self.new_game()
            self.update()
            self.add()
            self.drop()
            self.draw()
            self.check_events()

if __name__ == "__main__":
    game = Game()
    game.run()