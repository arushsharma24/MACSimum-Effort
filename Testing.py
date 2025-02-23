import Config
from Player import Player
import pygame as pg

width = Config.WindowWidth
height = Config.WindowHeight

win = pg.display.set_mode((width,height))
pg.display.set_caption("Client")

pos=[
    Player(Config.PlayerOffSet,(Config.WindowHeight-Config.PlayerLength)/2,Config.PlayerWidth,Config.PlayerLength,(255,0,0)),
    Player(Config.WindowWidth-Config.PlayerWidth-Config.PlayerOffSet,(Config.WindowHeight-Config.PlayerLength)/2,Config.PlayerWidth,Config.PlayerLength,(0,255,0)),
    Player((Config.WindowWidth-Config.PlayerLength)/2,Config.PlayerOffSet,Config.PlayerLength,Config.PlayerWidth,(0,0,255)),
    Player((Config.WindowWidth-Config.PlayerLength)/2,Config.WindowHeight-Config.PlayerWidth-Config.PlayerOffSet,Config.PlayerLength,Config.PlayerWidth,(128,128,0))
    ]


def render(win):
    win.fill((255,255,255))
    for p in pos:
        p.draw(win)
    pg.display.update()

def main():
    run=True
    clock=pg.time.Clock()
    while run:
        clock.tick(Config.FPS)
        for event in pg.event.get():
            if event.type ==pg.QUIT:
                run =False
                pg.quit()
        
        pos[2].move()
        render(win)

main()