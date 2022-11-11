import pygame as pg
import sys
from settings import * 
from map import *
from player import * 
from raycasting import *
from object_renderer import * 
from sprite_object import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import * 


class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)

        self.new_game()

    def new_game(self):
            self.map = Map(self)
            self.player = Player(self)
            self.object_renderer = ObjectRenderer(self)
            self.raycasting = RayCasting(self)
            self.object_handler = ObjectHandler(self)
            self.weapon = Weapon(self, 'resources/sprites/weapon/shotgun/0.png', 2.5, 90)
            self.sound = Sound(self)
            self.pathfinding = PathFinding(self)
            


    def update(self):
        #updates modules
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        ################
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        #2D render
        #self.screen.fill('black')
        #self.map.draw()
        #self.player.draw()
        #################

        #3D render
        self.object_renderer.draw()
        self.weapon.draw()
        #crosshair
        pg.draw.circle(self.screen, 'white', (HALF_WIDTH, HALF_HEIGHT), 1)

    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
            self.player.single_fire_event(event)

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
                

if __name__ == '__main__':
    game = Game()
    game.run()
    