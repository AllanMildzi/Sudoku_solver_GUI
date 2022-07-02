import pygame, sys, random
from settings import *


class Node:
    def __init__(self, number, pos, number_color=GRAY):
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
            self.image.fill(DARKER_GHOSTWHITE)
        else:
            self.image.fill(GHOSTWHITE)

        if self.number > 0:
            self.number_image = self.font.render(str(self.number), False, self.number_color)
            self.image.blit(self.number_image, (NODE_WIDTH / 2, NODE_HEIGHT / 2))
        
        surface.blit(self.image, self.rect)


class Board:
    def __init__(self):
        self.rows = self.columns = 9
        self.board = [[Node(0, (x * NODE_WIDTH, y * NODE_HEIGHT)) for x in range(self.columns)] for y in range(self.rows)]

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

    def backtrack(self, generate=False):
        empty_space = None
        for row in range(self.rows):
            for col in range(self.columns):
                if self.board[row][col].number == 0:
                    empty_space = (row, col)
                    break
            
            if empty_space != None:
                break
        
        if empty_space == None:
            return True

        numbers = random.sample(NUMBERS, len(NUMBERS))
        row, col = empty_space
        
        for num in numbers:
            if (self.check_row(row, num) 
                and self.check_column(col, num)
                and self.check_mini_square(row, col, num)):

                self.board[row][col].number = num
                if not generate:
                    self.draw_board(pygame.display.get_surface())
                    pygame.time.delay(50)

                if self.backtrack(generate) == True:
                    return True
                
                self.board[row][col].number = 0
                if not generate:
                    self.draw_board(pygame.display.get_surface())
                    pygame.time.delay(50)

        return False

    def remove_digits(self, digits_left):
        digit_counter = self.rows * self.columns
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        
        while digit_counter > digits_left:
            while self.board[row][col].number == 0:
                row = random.randint(0, 8)
                col = random.randint(0, 8)
            
            self.board[row][col].number = 0
            self.board[row][col].number_color = DARK_BLUE
            digit_counter -= 1
        

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
        
        pygame.display.update()
        

class Game:
    def __init__(self):
        pygame.init()
        self.win = pygame.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))
        pygame.display.set_caption("Sudoku")

        self.board = Board()
        self.active = False

    def run(self):
        font = pygame.font.SysFont("Arial", 30)
        difficulty_text = font.render("e for easy - m for medium - h for hard", False, BLACK)
        
        while not self.active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key in DIFFICULTY_INPUTS:
                    difficulty = DIFFICULTY[event.unicode]
                    self.active = True
            
            self.win.fill(DARKER_GHOSTWHITE)
            self.win.blit(difficulty_text, difficulty_text.get_rect(center = self.win.get_rect().center))
            
            pygame.display.update()

        self.board.backtrack(True)
        self.board.remove_digits(random.choice(difficulty))
        
        while True:
            self.board.user_input()

            self.win.fill(GHOSTWHITE)
            self.board.draw_board(self.win)

if __name__ == "__main__":
    game = Game()
    game.run()