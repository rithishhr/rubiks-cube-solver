# demo.py
from cube import Cube
from solver import Solver
from helper import getScramble
from visualizer import Visualizer
import pygame

# Generate a new random scramble every time the script is run
scramble = getScramble(10)
print("Scramble:", scramble)

# Create a Cube object and apply the scramble
cb = Cube()
cb.doMoves(scramble)

# Create a Visualizer instance with the cube
viz = Visualizer(cb)

# Create a Solver object and pass the visualizer
solver = Solver(cb, visualizer=viz)
solver.solveCube(optimize=True)

# Print the detailed solution moves
print("\nSolution Moves:")
moves = solver.getMoves(decorated=True)
print(moves)

# Keep the window open until the user closes it
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.time.wait(10)

pygame.quit()