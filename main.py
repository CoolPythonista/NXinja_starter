import sys
import pygame
from entities import PhysicsEntity
from utils import load_image, load_images
from tilemap import Tilemap


pygame.init()


class Game:
    def __init__(self, game_caption):
        self.game_caption = game_caption
        self.SCENE_WIDTH = 640
        self.SCENE_HEIGHT = 480
        self.FPS = 60
        

        self.SCENE = pygame.display.set_mode(
            [self.SCENE_WIDTH, self.SCENE_HEIGHT]
        )

        self.DISPLAY = pygame.Surface([320, 240])
        
        self.clock = pygame.time.Clock()

        self.assets = {
            'decor': load_images('/tiles/decor'),
            'grass': load_images('/tiles/grass'),
            'large_decor': load_images('/tiles/large_decor'),
            'stone': load_images('/tiles/stone'),
            'player': load_image('/entities/player.png')
        }


        #self.assets[]
        

        self.movement = [False, False]
        
        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))

        self.tilemap = Tilemap(self, tile_size=16)
        
    def run(self):
        running = True
        while running:
            
            self.clock.tick(self.FPS)
            current_fps = self.clock.get_fps()
            pygame.display.set_caption(f'{self.game_caption} [FPS: {current_fps:.2f}]')

            self.DISPLAY.fill([14, 219, 248])

            self.tilemap.render(self.DISPLAY)

            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.DISPLAY)


            print(self.tilemap.physics_rects_around(self.player.pos))

            # x2 screen size
            scaled_DISPLAY = pygame.transform.scale_by(self.DISPLAY, 2)
            self.SCENE.blit(scaled_DISPLAY, [0, 0])

            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pygame.K_UP:
                        self.player.velocity[1] = -3                 
                        
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False

            pygame.display.update()

        pygame.quit()
        sys.exit()




if __name__ == '__main__':
    game = Game('NXinja')
    game.run()
