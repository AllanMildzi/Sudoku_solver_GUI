import pygame, sys
from settings import *


class Node:
    def __init__(self, number, pos, number_color=DARK_BLUE):
        self.number = number
        self.number_color = number_color
        if self.number > 0:
            self.number_color = GRAY

        self.font = pygame.font.SysFont("Arial", 30)

        self.is_selected = False

        self.image = pygame.Surface((NODE_WIDTH, NODE_HEIGHT))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect(topleft=pos)
        self.pos = pygame.math.Vector2((pos[0] // NODE_WIDTH, pos[1] // NODE_HEIGHT))

    def draw(self, surface):        
        if self.is_selected:
            self.image.fill((220, 220, 255))
        else:
            self.image.fill(GHOSTWHITE)

        if self.number > 0:
            self.number_image = self.font.render(str(self.number), False, self.number_color)
            self.image.blit(self.number_image, (NODE_WIDTH / 2, NODE_HEIGHT / 2))
        
        surface.blit(self.image, self.rect)


class Board:
    def __init__(self):
        self.rows = self.columns = 9
        self.board = [
                    [Node(7, (0 * NODE_WIDTH, 0 * NODE_HEIGHT)), Node(8, (1 * NODE_WIDTH, 0 * NODE_HEIGHT)), Node(0, (2 * NODE_WIDTH, 0 * NODE_HEIGHT)), Node(4, (3 * NODE_WIDTH, 0 * NODE_HEIGHT)), Node(0, (4 * NODE_WIDTH, 0 * NODE_HEIGHT)), Node(0, (5 * NODE_WIDTH, 0 * NODE_HEIGHT)), Node(1, (6 * NODE_WIDTH, 0 * NODE_HEIGHT)), Node(2, (7 * NODE_WIDTH, 0 * NODE_HEIGHT)), Node(0, (8 * NODE_WIDTH, 0 * NODE_HEIGHT))],
                    [Node(6, (0 * NODE_WIDTH, 1 * NODE_HEIGHT)), Node(0, (1 * NODE_WIDTH, 1 * NODE_HEIGHT)), Node(0, (2 * NODE_WIDTH, 1 * NODE_HEIGHT)), Node(0, (3 * NODE_WIDTH, 1 * NODE_HEIGHT)), Node(7, (4 * NODE_WIDTH, 1 * NODE_HEIGHT)), Node(5, (5 * NODE_WIDTH, 1 * NODE_HEIGHT)), Node(0, (6 * NODE_WIDTH, 1 * NODE_HEIGHT)), Node(0, (7 * NODE_WIDTH, 1 * NODE_HEIGHT)), Node(9, (8 * NODE_WIDTH, 1 * NODE_HEIGHT))],
                    [Node(0, (0 * NODE_WIDTH, 2 * NODE_HEIGHT)), Node(0, (1 * NODE_WIDTH, 2 * NODE_HEIGHT)), Node(0, (2 * NODE_WIDTH, 2 * NODE_HEIGHT)), Node(6, (3 * NODE_WIDTH, 2 * NODE_HEIGHT)), Node(0, (4 * NODE_WIDTH, 2 * NODE_HEIGHT)), Node(1, (5 * NODE_WIDTH, 2 * NODE_HEIGHT)), Node(0, (6 * NODE_WIDTH, 2 * NODE_HEIGHT)), Node(7, (7 * NODE_WIDTH, 2 * NODE_HEIGHT)), Node(8, (8 * NODE_WIDTH, 2 * NODE_HEIGHT))],
                    [Node(0, (0 * NODE_WIDTH, 3 * NODE_HEIGHT)), Node(0, (1 * NODE_WIDTH, 3 * NODE_HEIGHT)), Node(7, (2 * NODE_WIDTH, 3 * NODE_HEIGHT)), Node(0, (3 * NODE_WIDTH, 3 * NODE_HEIGHT)), Node(4, (4 * NODE_WIDTH, 3 * NODE_HEIGHT)), Node(0, (5 * NODE_WIDTH, 3 * NODE_HEIGHT)), Node(2, (6 * NODE_WIDTH, 3 * NODE_HEIGHT)), Node(6, (7 * NODE_WIDTH, 3 * NODE_HEIGHT)), Node(0, (8 * NODE_WIDTH, 3 * NODE_HEIGHT))],
                    [Node(0, (0 * NODE_WIDTH, 4 * NODE_HEIGHT)), Node(0, (1 * NODE_WIDTH, 4 * NODE_HEIGHT)), Node(1, (2 * NODE_WIDTH, 4 * NODE_HEIGHT)), Node(0, (3 * NODE_WIDTH, 4 * NODE_HEIGHT)), Node(5, (4 * NODE_WIDTH, 4 * NODE_HEIGHT)), Node(0, (5 * NODE_WIDTH, 4 * NODE_HEIGHT)), Node(9, (6 * NODE_WIDTH, 4 * NODE_HEIGHT)), Node(3, (7 * NODE_WIDTH, 4 * NODE_HEIGHT)), Node(0, (8 * NODE_WIDTH, 4 * NODE_HEIGHT))],
                    [Node(9, (0 * NODE_WIDTH, 5 * NODE_HEIGHT)), Node(0, (1 * NODE_WIDTH, 5 * NODE_HEIGHT)), Node(4, (2 * NODE_WIDTH, 5 * NODE_HEIGHT)), Node(0, (3 * NODE_WIDTH, 5 * NODE_HEIGHT)), Node(6, (4 * NODE_WIDTH, 5 * NODE_HEIGHT)), Node(0, (5 * NODE_WIDTH, 5 * NODE_HEIGHT)), Node(0, (6 * NODE_WIDTH, 5 * NODE_HEIGHT)), Node(0, (7 * NODE_WIDTH, 5 * NODE_HEIGHT)), Node(5, (8 * NODE_WIDTH, 5 * NODE_HEIGHT))],
                    [Node(0, (0 * NODE_WIDTH, 6 * NODE_HEIGHT)), Node(7, (1 * NODE_WIDTH, 6 * NODE_HEIGHT)), Node(0, (2 * NODE_WIDTH, 6 * NODE_HEIGHT)), Node(3, (3 * NODE_WIDTH, 6 * NODE_HEIGHT)), Node(0, (4 * NODE_WIDTH, 6 * NODE_HEIGHT)), Node(0, (5 * NODE_WIDTH, 6 * NODE_HEIGHT)), Node(0, (6 * NODE_WIDTH, 6 * NODE_HEIGHT)), Node(1, (7 * NODE_WIDTH, 6 * NODE_HEIGHT)), Node(2, (8 * NODE_WIDTH, 6 * NODE_HEIGHT))],
                    [Node(1, (0 * NODE_WIDTH, 7 * NODE_HEIGHT)), Node(2, (1 * NODE_WIDTH, 7 * NODE_HEIGHT)), Node(0, (2 * NODE_WIDTH, 7 * NODE_HEIGHT)), Node(0, (3 * NODE_WIDTH, 7 * NODE_HEIGHT)), Node(0, (4 * NODE_WIDTH, 7 * NODE_HEIGHT)), Node(7, (5 * NODE_WIDTH, 7 * NODE_HEIGHT)), Node(4, (6 * NODE_WIDTH, 7 * NODE_HEIGHT)), Node(0, (7 * NODE_WIDTH, 7 * NODE_HEIGHT)), Node(0, (8 * NODE_WIDTH, 7 * NODE_HEIGHT))],
                    [Node(0, (0 * NODE_WIDTH, 8 * NODE_HEIGHT)), Node(4, (1 * NODE_WIDTH, 8 * NODE_HEIGHT)), Node(9, (2 * NODE_WIDTH, 8 * NODE_HEIGHT)), Node(2, (3 * NODE_WIDTH, 8 * NODE_HEIGHT)), Node(0, (4 * NODE_WIDTH, 8 * NODE_HEIGHT)), Node(6, (5 * NODE_WIDTH, 8 * NODE_HEIGHT)), Node(0, (6 * NODE_WIDTH, 8 * NODE_HEIGHT)), Node(0, (7 * NODE_WIDTH, 8 * NODE_HEIGHT)), Node(7, (8 * NODE_WIDTH, 8 * NODE_HEIGHT))]
                    ]

    def user_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for nodes in self.board:
                    for node in nodes:
                        node.is_selected = False
                        if node.rect.collidepoint(event.pos):
                            if node.is_selected:
                                node.is_selected = False
                            else:
                                node.is_selected = True
            
            if event.type == pygame.KEYDOWN and event.key in INPUTS:
                for nodes in self.board:
                    for node in nodes:
                        if node.is_selected and node.number_color != GRAY:
                            node.number = int(event.unicode)
                            if (not self.check_row(int(node.pos.y), node.number) 
                                or not self.check_column(int(node.pos.x), node.number) 
                                or not self.check_mini_square(int(node.pos.y), int(node.pos.x), node.number)):
                                
                                node.number_color = RED
                            else:
                                node.number_color = DARK_BLUE
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.backtrack()

    def check_row(self, row, num):
        for col in range(self.columns):
            if self.board[row][col].number <= 0 or self.board[row][col].is_selected:
                continue
            if self.board[row][col].number == num:
                return False

        return True

    def check_column(self, col, num):
        for row in range(self.rows):
            if self.board[row][col].number <= 0 or self.board[row][col].is_selected:
                continue
            if self.board[row][col].number == num:
                return False

        return True

    def check_mini_square(self, curr_row, curr_col, num):
        for row in range(curr_row - curr_row % 3, curr_row - (curr_row % 3) + 3):
            for col in range(curr_col - curr_col % 3, curr_col - (curr_col % 3) + 3):
                if self.board[row][col].number <= 0 or self.board[row][col].is_selected:
                    continue
                if self.board[row][col].number == num:
                    return False

        return True

    def is_winner(self):
        for nodes in self.board:
            for node in nodes:
                if node.number == 0 or node.number_color == RED:
                    return False
        
        return True

    def backtrack(self):
        empty_space = None
        for row in range(self.rows):
            for col in range(self.columns):
                if self.board[row][col].number == 0:
                    empty_space = (row, col)
        
        if empty_space == None:
            return True

        row, col = empty_space
        for num in NUMBERS:                
            if (self.check_row(row, num) 
                and self.check_column(col, num)
                and self.check_mini_square(row, col, num)):

                self.board[row][col].number = num

                if self.backtrack() == True:
                    return True
                
                self.board[row][col].number = 0

        return False

    def draw_board(self, surface):
        for nodes in self.board:
            for node in nodes:
                node.draw(surface)
        
        for row in range(self.rows + 1):
            if row % 3 == 0:
                color = BLACK
                width = 3
            else:
                color = GRAY
                width = 1
            
            pygame.draw.line(surface, color, (0, row * NODE_HEIGHT), (BOARD_WIDTH, row * NODE_HEIGHT), width)
        
        for col in range(self.columns + 1):
            if col % 3 == 0:
                color = BLACK
                width = 3
            else:
                color = GRAY
                width = 1
            
            pygame.draw.line(surface, color, (col * NODE_WIDTH, 0), (col * NODE_WIDTH, BOARD_HEIGHT), width)
        

class Game:
    def __init__(self):
        pygame.init()
        self.win = pygame.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))
        pygame.display.set_caption("Sudoku")

        self.board = Board()

    def run(self):
        while True:
            self.board.user_input()

            self.win.fill(GHOSTWHITE)
            self.board.draw_board(self.win)
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()