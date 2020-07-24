import pygame
import glob


def fps():
    fr = "V.3 Fps: " + str(int(clock.get_fps()))
    frt = font.render(fr, 1, pygame.Color("coral"))
    return frt


class MySprite(pygame.sprite.Sprite):
    def __init__(self, action):
        super(MySprite, self).__init__()
        self.action = action
        # This is to slow down animation # takes the frame now and...
        self.elapsed = 0
        self.images = []
        self.temp_imgs = []
        self.load_images()
        self.count = 0

    def load_images(self):
        l_imgs = glob.glob(f"png\\{self.action}*.png")
        for img in l_imgs:
            if len(img) == len(l_imgs[0]):
                self.images.append(pygame.image.load(img))
            else:
                self.temp_imgs.append(pygame.image.load(img))
        self.images.extend(self.temp_imgs)
        self.index = 0
        self.rect = pygame.Rect(5, 5, 150, 198)

    def update(self):
        self.count += 1
        if self.index == len(self.images):
                self.index = 0
        self.image = self.images[self.index]
        if self.count > 2:
                #self.image = self.images[self.index]
                self.index += 1
                self.count = 0

    def group_sprites(self):
        return pygame.sprite.Group(self)


def group():
    "Dictionary of group of sprites"
    dici = {}
    actions = "idle walk run jump dead"
    actions = actions.split()
    for action in actions:
        dici[action] = MySprite(action).group_sprites()
    return dici


def main():
    global clock
    global font

    SIZE = 600, 600
    FPS = 60
    pygame.init()
    action = group()
    my_group = action["idle"]
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Game v.3")
    font = pygame.font.SysFont("Arial", 60)
    clock = pygame.time.Clock()
    keyactions = (
        (pygame.K_LEFT, "walk"),
        (pygame.K_UP, "jump"),
        (pygame.K_SPACE, "idle"),
        (pygame.K_RIGHT, "run"),
        (pygame.K_DOWN, "dead"))

    loop = 1
    while loop:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
            if event.type == pygame.KEYDOWN:
                for k, a in keyactions:
                    if event.key == k:
                        my_group = action[a]

        my_group.update()
        screen.fill((0, 0, 0))
        my_group.draw(screen)
        screen.blit(fps(), (10, 0))
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()