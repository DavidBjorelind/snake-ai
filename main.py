import pygame
pygame.init()


class cube(object):
    res = 20
    w = 500
    def __init__(self, start) -> None:
        self.pos = start
        super().__init__()

class snek(object):
    body = []
    turns = {}

    def __init__(self, color, pos) -> None:
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dir_x = 0
        self.dir_y = 1
        super().__init__()
    
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dir_x = -1
                    self.dir_y = 0
                    self.turns[self.head.pos[:]] = [self.dir_x, self.dir_y]

                elif keys[pygame.K_RIGHT]:
                    self.dir_x = 1
                    self.dir_y = 0
                    self.turns[self.head.pos[:]] = [self.dir_x, self.dir_y]

                elif keys[pygame.K_UP]:
                    self.dir_x = 0
                    self.dir_y = -1
                    self.turns[self.head.pos[:]] = [self.dir_x, self.dir_y]

                elif keys[pygame.K_DOWN]:
                    self.dir_x = 0
                    self.dir_y = 1
                    self.turns[self.head.pos[:]] = [self.dir_x, self.dir_y]

        for i,c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                if c.dir_x == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1]) 
                elif c.dir_x == 1 and c.pos[0] <= c.rows-1: c.pos = (0, c.pos[1])
                elif c.dir_y == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0) 
                elif c.dir_y == -1 and c.pos[1] <= 0: c.pos = (c.pos[0], c.rows-1)
                else: c.move(c.dir_x, c.dir_y)


                    
def draw_grid(w, res, surface):
    size_between = w // res
    
    x = 0
    y = 0
    for l in range(res):
        x = x + size_between
        y = y + size_between
        pygame.draw.line(surface, (255, 255, 255), (x,0), (x,w))
        pygame.draw.line(surface, (255, 255, 255), (0,y), (w,y))

    

def redraw(surface):
    global res, width
    surface.fill((0,0,0))
    draw_grid(width, res, surface)
    pygame.display.update()
    print('updates window')

def main():
    global width, res
    width = 500
    res = 25
    window = pygame.display.set_mode((width, width))

    s = snek(color=(0,0,0), pos=(0,0))

    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(500)
        clock.tick(10)
        redraw(window)
    

main()
# rows -> res
# top left is (0,0)
