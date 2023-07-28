import pygame
import os


WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Test 1st Game")
FPS = 60

CHARIMG = pygame.image.load(os.path.join('Assets','adventurer_action1.png'))

def draw_window():
        WIN.fill((200,200,200))
        WIN.blit(CHARIMG,(400,300))
        pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()


# TestComment



if __name__ == "__main__":
    main()