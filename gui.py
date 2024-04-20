import pygame
from snake import SnakeGame


def main():
    pygame.init()
    cell_size = 20
    game = SnakeGame(20, 20)
    screen = pygame.display.set_mode((game.width * cell_size, game.height * cell_size))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.change_direction(0, -1)
                elif event.key == pygame.K_DOWN:
                    game.change_direction(0, 1)
                elif event.key == pygame.K_LEFT:
                    game.change_direction(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    game.change_direction(1, 0)
                if not game.move_snake():
                    print("Game Over!")
                    running = False
        
        screen.fill((0, 0, 0))
        for y in range(game.height):
            for x in range(game.width):
                rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
                if game.board[y, x] == game.snake_block:
                    pygame.draw.rect(screen, (0, 150, 0), rect)  # 蛇身体的绿色
                    inner_rect = pygame.Rect(x * cell_size + 3, y * cell_size + 3, cell_size - 6, cell_size - 6)
                    pygame.draw.rect(screen, (0, 220, 0), inner_rect)  # 蛇身体的深绿色轮廓
                elif game.board[y, x] == game.food_block:
                    pygame.draw.rect(screen, (150, 0, 0), rect)  # 果子的红色
                    inner_rect = pygame.Rect(x * cell_size + 3, y * cell_size + 3, cell_size - 6, cell_size - 6)
                    pygame.draw.rect(screen, (220, 0, 0), inner_rect)  # 果子的浅红色轮廓
                    
        pygame.display.flip()
        clock.tick(5)  # 控制游戏速度

    pygame.quit()


if __name__ == "__main__":
    main()
