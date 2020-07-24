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
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        if self.count > 2:
            self.index += 1
            self.count = 0

    def group_sprites(self):
        return pygame.sprite.Group(self)


def group():
    dici = {}
    actions = "idle walk run jump dead"
    actions = actions.split()
    for action in actions:
        dici[action] = MySprite(action).group_sprites()
    return dici

def main():
    global font, clock

    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Game v.5")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 60)
    keyactions = (
        (pygame.K_LEFT, "walk"),
        (pygame.K_UP, "jump"),
        (pygame.K_SPACE, "idle"),
        (pygame.K_RIGHT, "run"),
        (pygame.K_DOWN, "dead"))
    action = group()
    my_group = action["idle"]

    ln = 509
    ln2 = 511
    run = False
    loop = 1
    line = 599
    bgd = pygame.Surface((400, 509))
    bgd.fill((0,0,0))
    pygame.draw.line(screen, (255, 0, 0), (0, ln), (ln + 100, ln), 2)
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
            if event.type == pygame.KEYDOWN:
                for k, v in keyactions:
                    if event.key == k:
                        my_group = action[v]
                        run = True
        my_group.update()
        # screen.fill((0, 0, 0))
        my_group.clear(screen, bgd)
        my_group.draw(screen)
        pygame.draw.line(screen, (0, 0, 0), (line + 6, ln2), (line + 6, ln2 + 100), 2)
        pygame.draw.line(screen, (255, 0, 0), (line, ln2), (line, ln2 + 100), 2)
        if run:
            line -= 3
            if line < - 7:
                line = 599
        screen.blit(fps(), (10, 0))
        clock.tick(60)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()