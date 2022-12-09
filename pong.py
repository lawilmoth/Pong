import pygame
pygame.init()
pygame.display.set_caption('Pong')

WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


FPS = 60
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100

class Paddle:
    COLOR = "White"
    VEL = 4
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL


def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and left_paddle.y -left_paddle.VEL >= 0:
        left_paddle.move(up = True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height <= HEIGHT:
        left_paddle.move(up = False)

    if keys[pygame.K_UP]:
        right_paddle.move(up = True)
    if keys[pygame.K_DOWN]:
        right_paddle.move(up = False)

def draw(win, paddles):  #1
    win.fill('Black')  #1


    for paddle in paddles:
        paddle.draw(win)
    pygame.display.update()


def main(): #1
    run = True #1


    clock = pygame.time.Clock()
    left_paddle = Paddle(10, HEIGHT//2 -PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT )
    right_paddle = Paddle(WIDTH-10 -PADDLE_WIDTH, HEIGHT//2 -PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT )
    
    
    while run: #1
        clock.tick(FPS)
        draw(WIN, [left_paddle, right_paddle])
        
        
        for event in pygame.event.get(): #1
            if event.type == pygame.QUIT: #1
                run = False #1
                break #1
        
        
        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)

    pygame.quit() #1



if __name__ == '__main__': #1
    main()

