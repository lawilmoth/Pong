import pygame

pygame.init()
pygame.display.set_caption("Pong")


############# CONSTATNSTS ################### 
WIDTH, HEIGHT = 700, 500 
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100 

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 60

##############CLASSES#########################
class Paddle:
    COLOR = "White"
    VEL = 4

    def __init__(self, x, y , width, height):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
    
    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up: 
            self.y -= self.VEL
        else:
            self.y += self.VEL


class Ball:
    COLOR = "White"
    MAX_VEL = 5
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel




###########################MAIN LOOP##########################
def main(): #Main loop of the game
    run = True

    clock = pygame.time.Clock()

    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT) 
    right_paddle = Paddle(WIDTH -10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT) 

    ball = Ball(WIDTH//2, HEIGHT//2, 7)

    while run:
        clock.tick(FPS)
        draw(WIN, [left_paddle, right_paddle], ball)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    
        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)
        ball.move()

        
    pygame.quit()
##################################################################   
##############FUNCTIONS########################

def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >= 0: 
        left_paddle.move(up = True)
    if keys[pygame.K_s] and left_paddle.y +left_paddle.VEL <= HEIGHT - left_paddle.height:
        left_paddle.move(up = False)


def draw(win, paddles, ball):
    win.fill("Black")

    for paddle in paddles:
        paddle.draw(win)

    for i in range(10, HEIGHT, HEIGHT//20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(win, "White",(WIDTH//2-5, i, 10, HEIGHT//20))

    ball.draw(win)
    #Update should always be last when we draw.
    pygame.display.update()

 
 
if __name__ == '__main__':
    main()