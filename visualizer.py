# visualizer.py
import pygame
from cube import Cube

class Visualizer:
    def __init__(self, cube):
        self.cube = cube
        self.size = 800
        self.sticker_size = 50
        self.colors = {
            'W': (255, 255, 255),  # White
            'Y': (255, 255, 0),    # Yellow
            'G': (0, 128, 0),      # Green
            'B': (0, 0, 255),      # Blue
            'R': (255, 0, 0),      # Red
            'O': (255, 165, 0)     # Orange
        }
        # Correct face mapping based on your cube's internal representation
        self.face_positions = {
            5: (0, 1), # Yellow (Up) face
            3: (1, 0), # Red (Left) face
            0: (1, 1), # Green (Front) face
            1: (1, 2), # Orange (Right) face
            2: (1, 3), # Blue (Back) face
            4: (2, 1)  # White (Down) face
        }
        pygame.init()
        self.screen = pygame.display.set_mode((self.size, self.size))
        pygame.display.set_caption("Rubik's Cube Solver")
        self.font = pygame.font.Font(None, 24)

    def draw_cube(self):
        self.screen.fill((200, 200, 200)) # Grey background
        for face_index, (row_pos, col_pos) in self.face_positions.items():
            for r in range(3):
                for c in range(3):
                    color = self.colors.get(self.cube.cube[face_index][r][c], (100, 100, 100))
                    x = (col_pos * 3 + c) * self.sticker_size + 150
                    y = (row_pos * 3 + r) * self.sticker_size + 50
                    rect = pygame.Rect(x, y, self.sticker_size, self.sticker_size)
                    pygame.draw.rect(self.screen, color, rect, 0)
                    pygame.draw.rect(self.screen, (0, 0, 0), rect, 1) # Black border
        pygame.display.flip()

    def update(self, new_cube_state, message=""):
        self.cube.cube = new_cube_state
        self.draw_cube()
        if message:
            text_surface = self.font.render(message, True, (0, 0, 0))
            self.screen.blit(text_surface, (10, 10))
            pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
        return True

    def run(self):
        self.draw_cube()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.time.wait(10)
        pygame.quit()