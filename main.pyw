import sys
import pygame




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
        self.clock = pygame.time.Clock()
        

    def run(self):
        running = True
        while running:
            
            self.clock.tick(self.FPS)
            current_fps = self.clock.get_fps()
            pygame.display.set_caption(f'{self.game_caption} [FPS: {current_fps:.2f}]')

            self.SCENE.fill([225, 220, 235])


            ...
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            pygame.display.update()

        pygame.quit()
        sys.exit()




if __name__ == '__main__':
    game = Game('NXinja')
    game.run()
