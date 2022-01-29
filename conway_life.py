"""
Conway's Game of Life
"""
import random

def game_of_life(board):
    """
    Returns a new board with the next generation of Conway's Game of Life.
    """
    new_board = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            neighbors = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x == 0 and y == 0:
                        continue
                    if i + x < 0 or i + x >= len(board):
                        continue
                    if j + y < 0 or j + y >= len(board[0]):
                        continue
                    neighbors += board[i + x][j + y]
            if board[i][j] == 1:
                if neighbors < 2:
                    new_board[i][j] = 0
                elif neighbors > 3:
                    new_board[i][j] = 0
                else:
                    new_board[i][j] = 1
            else:
                if neighbors == 3:
                    new_board[i][j] = 1
                else:
                    new_board[i][j] = 0
    return new_board


if __name__ == '__main__':
    # random board of 0s and 1s size 50x50
    board = [[random.randint(0, 1) for _ in range(50)] for _ in range(50)]
    print(game_of_life(board))

    # visualize the board with pygame
    import pygame
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Conway\'s Game of Life')
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 1:
                    pygame.draw.rect(screen, (255, 255, 255), (i * 10, j * 10, 10, 10))
        pygame.display.flip()
        board = game_of_life(board)
        clock.tick(60)
    pygame.quit()
    quit()


