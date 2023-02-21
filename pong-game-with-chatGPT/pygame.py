import pygame

# Set up game window
pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pong")

# Define game objects
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
BALL_RADIUS = 10
paddle1 = pygame.Rect(50, 250, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(740, 250, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(395, 295, BALL_RADIUS, BALL_RADIUS)
ball_speed_x = 5
ball_speed_y = 5

# Set up score display
font = pygame.font.Font(None, 50)
score1 = 0
score2 = 0
score_text1 = font.render(str(score1), True, (255, 255, 255))
score_text2 = font.render(str(score2), True, (255, 255, 255))
score_pos1 = score_text1.get_rect(center=(50, 50))
score_pos2 = score_text2.get_rect(center=(750, 50))

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                paddle1.y -= 20
            elif event.key == pygame.K_s:
                paddle1.y += 20
            elif event.key == pygame.K_UP:
                paddle2.y -= 20
            elif event.key == pygame.K_DOWN:
                paddle2.y += 20
    
    # Move ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    # Handle collisions with walls
    if ball.top <= 0 or ball.bottom >= WINDOW_HEIGHT:
        ball_speed_y = -ball_speed_y
    if ball.left <= 0:
        score2 += 1
        score_text2 = font.render(str(score2), True, (255, 255, 255))
        ball_speed_x = -ball_speed_x
    if ball.right >= WINDOW_WIDTH:
        score1 += 1
        score_text1 = font.render(str(score1), True, (255, 255, 255))
        ball_speed_x = -ball_speed_x
    
    # Handle collisions with paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x = -ball_speed_x
    
