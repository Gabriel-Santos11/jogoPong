import pygame
import random

# Constantes
WIDTH, HEIGHT = 800, 640
FPS = 60

# Cores
SKY_BLUE = (138, 43, 226)
PRUSSIAN_BLUE = (2, 48, 71)
SELECTIVE_YELLOW = (255, 140, 000)
WHITE = (255, 255, 255)

# Propriedades das barras
RECT_WIDTH, RECT_HEIGHT = 50, 100
RECT1_X, RECT1_Y = 10, HEIGHT // 2 - RECT_HEIGHT // 2
RECT2_X, RECT2_Y = WIDTH - RECT_WIDTH - 10, HEIGHT // 2 - RECT_HEIGHT // 2

# Propriedades da bola
BALL_RADIUS = 10
BALL_X, BALL_Y = WIDTH // 2, HEIGHT // 2
BALL_DX, BALL_DY = random.choice([-4, 4]), random.choice([-4, 4])

# Velocidade da barra
SPEED = 5

# Fonte para exibir a pontuação
FONT_NAME = pygame.font.match_font('arial')
FONT_SIZE = 36

def draw_text(screen, text, font, color, position):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=position)
    screen.blit(text_surface, text_rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong")
    clock = pygame.time.Clock()

    # Inicializar pontuação
    score1 = 0
    score2 = 0

    # Carregar fonte
    font = pygame.font.Font(FONT_NAME, FONT_SIZE)

    rect1_y = RECT1_Y
    rect2_y = RECT2_Y
    ball_x, ball_y = BALL_X, BALL_Y
    ball_dx, ball_dy = BALL_DX, BALL_DY

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and rect1_y > 0:
            rect1_y -= SPEED
        if keys[pygame.K_s] and rect1_y < HEIGHT - RECT_HEIGHT:
            rect1_y += SPEED
        if keys[pygame.K_UP] and rect2_y > 0:
            rect2_y -= SPEED
        if keys[pygame.K_DOWN] and rect2_y < HEIGHT - RECT_HEIGHT:
            rect2_y += SPEED

        # Movimento da bola
        ball_x += ball_dx
        ball_y += ball_dy

        # Colisão com as bordas da tela
        if ball_y - BALL_RADIUS <= 0 or ball_y + BALL_RADIUS >= HEIGHT:
            ball_dy *= -1

        # Colisão com as barras
        # Barra amarela
        if (RECT1_X < ball_x + BALL_RADIUS and
            ball_x - BALL_RADIUS < RECT1_X + RECT_WIDTH and
            rect1_y < ball_y + BALL_RADIUS and
            ball_y - BALL_RADIUS < rect1_y + RECT_HEIGHT):
            ball_dx *= -1
            ball_x = RECT1_X + RECT_WIDTH + BALL_RADIUS

        # Barra azul
        if (RECT2_X < ball_x + BALL_RADIUS and
            ball_x - BALL_RADIUS < RECT2_X + RECT_WIDTH and
            rect2_y < ball_y + BALL_RADIUS and
            ball_y - BALL_RADIUS < rect2_y + RECT_HEIGHT):
            ball_dx *= -1
            ball_x = RECT2_X - BALL_RADIUS

        # Colisão com as bordas laterais da tela (marcador de ponto)
        if ball_x - BALL_RADIUS <= 0:
            score2 += 1
            ball_x, ball_y = WIDTH // 2, HEIGHT // 2
            ball_dx, ball_dy = random.choice([-4, 4]), random.choice([-4, 4])
        if ball_x + BALL_RADIUS >= WIDTH:
            score1 += 1
            ball_x, ball_y = WIDTH // 2, HEIGHT // 2
            ball_dx, ball_dy = random.choice([-4, 4]), random.choice([-4, 4])

        screen.fill(PRUSSIAN_BLUE)

        # Desenhar barras
        pygame.draw.rect(screen, SELECTIVE_YELLOW, (RECT1_X, rect1_y, RECT_WIDTH, RECT_HEIGHT))
        pygame.draw.rect(screen, SKY_BLUE, (RECT2_X, rect2_y, RECT_WIDTH, RECT_HEIGHT))

        # Desenhar bola
        pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_RADIUS)

        # Desenhar pontuação
        draw_text(screen, f'{score1}', font, WHITE, (WIDTH // 4, 50))
        draw_text(screen, f'{score2}', font, WHITE, (3 * WIDTH // 4, 50))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
