import pygame
import random

pygame.init()


class cube(object):
    res = 20
    w = 500
    def __init__(self, pos, dir_x=1, dir_y = 0, color=(255,0,0)) -> None:
        self.pos = pos
        self.dir_x = 1
        self.dir_y = 0
        self.color = color
        super().__init__()
    
    def move(self, dir_x, dir_y):
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.pos = (self.pos[0] + self.dir_x, self.pos[1] + self.dir_y)

    def draw(self, surface, eyes=False):
        d = self.w // self.res
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i*d+1, j*d+1, d-2, d-2))
        if eyes:
            mid = d//2
            rad = 4
            circle_1 = (i*d+mid, j*d+mid)
            pygame.draw.circle(surface, (255,255,255), circle_1, rad*2)
            pygame.draw.circle(surface, (0,0,0), circle_1, rad)


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
            sim = random.randrange(4)
            print('slumpar ett tal')
            
            #print(keys)

            for key in keys:
                if keys[pygame.K_LEFT] or sim == 1:
                    self.dir_x = -1
                    self.dir_y = 0
                    self.turns[self.head.pos[:]] = [self.dir_x, self.dir_y]

                elif keys[pygame.K_RIGHT] or sim == 2:
                    self.dir_x = 1
                    self.dir_y = 0
                    self.turns[self.head.pos[:]] = [self.dir_x, self.dir_y]

                elif keys[pygame.K_UP] or sim == 3:
                    self.dir_x = 0
                    self.dir_y = -1
                    self.turns[self.head.pos[:]] = [self.dir_x, self.dir_y]

                elif keys[pygame.K_DOWN] or sim == 4:
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
                if c.dir_x == -1 and c.pos[0] <= 0:
                    #c.pos = (c.res-1, c.pos[1])
                    print('Score: ', len(s.body))
                    s.reset((10,10))
                elif c.dir_x == 1 and c.pos[0] >= c.res-1:
                    #c.pos = (0, c.pos[1])
                    print('Score: ', len(s.body))
                    s.reset((10,10))
                elif c.dir_y == 1 and c.pos[1] >= c.res-1:
                    #c.pos = (c.pos[0], 0)
                    print('Score: ', len(s.body))
                    s.reset((10,10))
                elif c.dir_y == -1 and c.pos[1] <= 0:
                    #c.pos = (c.pos[0], c.res-1)
                    print('Score: ', len(s.body))
                    s.reset((10,10))
                else: c.move(c.dir_x, c.dir_y)

    
    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)

    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dir_x = 0
        self.dir_y = 1

    def addCube(self):
        tail = self.body[-1] # Last element
        dx, dy = tail.dir_x, tail.dir_y

        if dx == 1 and dy == 0: # Right
            self.body.append(cube((tail.pos[0]-1, tail.pos[1])))
        elif dx == -1 and dy == 0: # Left
            self.body.append(cube((tail.pos[0]+1, tail.pos[1])))
        elif dx == 0 and dy == -1: # Up
            self.body.append(cube((tail.pos[0], tail.pos[1]+1)))
        elif dx == 0 and dy == 1: # Down
            self.body.append(cube((tail.pos[0], tail.pos[1]-1)))

        self.body[-1].dir_x = dx
        self.body[-1].dir_y = dy


def start_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    keys = pygame.key.get_pressed()

    for key in keys:  
        if keys[pygame.K_SPACE]:
            print("enter-press")
            return True
        else:
            return False


def draw_start_screen(surface):
    surface.fill((0,0,0))
    font = pygame.font.SysFont('didot.ttc', 72)
    text = font.render('Press space to start', True, (255,255,255))
    surface.blit(text, (150, 200))
    pygame.display.update()
                    
def draw_grid(w, res, surface):
    size_between = w // res
    
    x = 0
    y = 0
    for l in range(res):
        x = x + size_between
        y = y + size_between
        pygame.draw.line(surface, (255, 255, 255), (x,0), (x,w))
        pygame.draw.line(surface, (255, 255, 255), (0,y), (w,y))

def draw_stats(w, res, surface, s):
    font = pygame.font.SysFont('didot.ttc', 72)
    score_text = font.render('Score:', True, (255,255,255))
    score = font.render(str(len(s.body)), True, (255,255,255))
    surface.blit(score_text, (w+30, 200))
    surface.blit(score, (w+100, 250))

def apple_pos(res, snake):
    position = snake.body
    while True:
        x = random.randrange(res)
        y = random.randrange(res)
        if len(list(filter(lambda z:z.pos == (x,y), position))) > 0:
            continue
        else:
            break
    return(x,y)

def redraw(surface):
    surface.fill((0,0,0))
    s.draw(surface)
    apple.draw(surface)
    draw_grid(height, res, surface)
    draw_stats(height, res, surface, s)
    pygame.display.update()


def main():
    global width, height, res, s, apple, game
    width = 700
    height = 500
    res = 20
    window = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    # Variable to know whether the game has started or not
    game = False # Set to True to skip this step
    while game == False:
        pygame.time.delay(50)
        clock.tick(40)
        if start_game():
            game = True
        draw_start_screen(window)
        

    s = snek(color=(0,0,0), pos=(10,10))
    apple = cube(apple_pos(res, s), color=(0,255,0))
    
    while game:
        pygame.time.delay(50)
        clock.tick(40)
        s.move()
        # Checking if snake has eaten the apple
        if s.body[0].pos == apple.pos:
            s.addCube()
            apple = cube(apple_pos(res, s), color=(0,255,0))

        # Checking of snake has failed
        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos, s.body[x+1:])):
                print('Score: ', len(s.body))
                s.reset((10,10))
                game = False
                break

        redraw(window)
        
    

main()
# rows -> res
# randomSnack -> apple_pos
# top left is (0,0)
