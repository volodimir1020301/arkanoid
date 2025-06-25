import pygame
pygame.init()
class Ball:
    def __init__(self, x, y, radius, speed, color):
        self.color = color
        self.rect = pygame.Rect(x, y, 2*radius, 2*radius)
        self.dx = speed
        self.dy = speed
        self.radius = radius

    def draw(self, window):
        pygame.draw.circle(window, self.color, [self.rect.x, self.rect.y], self.radius)
class Brick:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)


window = pygame.display.set_mode([1000, 600])
clock = pygame.time.Clock()
ball = Ball(400, 300, 10, 8, [255, 0, 0])
bricks = []
with open("lvl1", "r", encoding="utf-8") as file:
    lines = [line for line in file.readlines()]
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "#":
                bricks.append(Brick(x*75+10, y*75+10,75, 75, [255, 0, 0]))


while 1==1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    window.fill([0, 0, 0])
    ball.draw(window)
    for brick in bricks:
        brick.draw(window)
    pygame.display.flip()

    clock.tick(60)